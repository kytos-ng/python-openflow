"""Automate struct tests."""
import pytest

from pyof.foundation.base import GenericMessage
from tests.unit.raw_dump import RawDump


class StructTest:
    """Run tests related to struct packing and unpacking.

    Test the lib with raw dump files from an OpenFlow switch. We assume the
    raw files are valid according to the OF specs to check whether our pack and
    unpack implementations are correct.

    Also, check the minimum size of the struct by instantiating an object with
    no parameters.

    To run these tests, just extends this class and call 2 methods in the
    ``setup_method`` method like the example.

    Example:
        .. code-block:: python3

            class TestMine(StructTest):
                def setup_method(self):
                    self.set_raw_dump_file('v0x01', 'ofpt_barrier_reply')
                    # Create BarrierReply(xid=5) when needed
                    selfset_raw_dump_object(BarrierReply, xid=5)
                    # As in spec: ``OFP_ASSERT(sizeof(struct ...) == ...);``
                    self.set_minimum_size(8)

        To only test the minimum size and skip packing/unpacking:

        .. code-block:: python3
            class TestMine(TestDump):
                def setup_method(self):
                    self.set_minimum_size(8, BarrierReply)
    """

    def set_raw_dump_file(self, version, basename):
        """Set which raw dump the tests will use.

        Args:
            protocol_version (str): OpenFlow protocol version,
                e.g. ``v0x01``.
            basename (str): The raw filename without extension.
                E.g. ``ofpt_echo_reply``.
        """
        self._new_raw_dump = lambda: RawDump(version, basename)

    def get_raw_dump(self):
        """Return a new instance of :class:`.RawDump`.

        Use the parameters set in :meth:`set_raw_dump_file`.

        Returns:
            RawDump: with parameters previously set using
                :meth:`set_raw_dump_file`.

        """
        try:
            if self._new_raw_dump is None:
                raise FileNotFoundError()
        except AttributeError:
            raise FileNotFoundError()
        return self._new_raw_dump()

    def set_raw_dump_object(self, msg_self, *args, **kwargs):
        """Set how to create the object that is dumped in a raw file.

        Args:
            msg_class (:obj:`type`): The message class that is packed as a
                raw file, followed by its parameters to instantiate an
                object.

        Example:
            ``self.set_raw_dump_object(BarrierReply, xid=5)`` will create
            ``BarrierReply(xid=5)``.
        """
        self._msg_self = msg_self
        self._new_raw_object = lambda: msg_self(*args, **kwargs)

    def get_raw_object(self):
        """Create a new object of the dumped message.

        Use the class and parameters set in :meth:`set_raw_dump_object`.

        Returns:
            A new object using class and parameters priviously set through
                :meth:`set_raw_dump_object`.

        """
        pyof_obj = self._new_raw_object()
        if isinstance(pyof_obj, GenericMessage):
            pyof_obj.update_header_length()
        return pyof_obj

    def set_minimum_size(self, size, msg_self=None):
        """Set the struct minimum size.

        The minimum size can be found in OF spec. For example,
        :class:`.PhyPort` minimum size is 48 because of
        ``OFP_ASSERT(sizeof(struct ofp_phy_port) == 48);`` (spec 1.0.0).

        Args:
            size (int): The minimum size of the struct, in bytes.
            msg_self (class): The class (or function) to have its size checked.
                If None, use the same class set in :meth:`set_raw_dump_object`.
        """
        self._min_size = size
        if msg_self is not None:
            self._msg_self = msg_self

    def _test_pack(self, obj, expected_bytes):
        """Check whether packed objects equals to dump file."""
        actual_bytes = obj.pack()
        assert expected_bytes == actual_bytes

    def test_raw_dump_file(self):
        """Object pack should equal file; file unpack should equal object.

        The object to be packed is set with :method:`set_raw_object` and the
        file, with :method:`set_raw_dump_file`.
        """
        try:
            file_bytes = self.get_raw_dump().read()
        except FileNotFoundError:
            raise pytest.skip('No raw dump file found.')

        pyof_obj = self.get_raw_object()
        self._test_pack(pyof_obj, file_bytes)
        self._test_unpack(pyof_obj, file_bytes)

    def _test_unpack(self, pyof_obj, bytes2unpack=None):
        """Check whether unpacking ``bytes2unpack`` equals ``pyof_obj``.

        Args:
            pyof_obj (GenericStruct, GenericType): Object supporting (un)pack
                operations.
            bytes2unpack (bytes): If not supplied, use ``pyof_obj.pack()``.
        """
        bytes2unpack = bytes2unpack or pyof_obj.pack()

        unpacked = type(pyof_obj)()
        # If it's a GenericMessage, unpack the Header first
        if isinstance(pyof_obj, GenericMessage):
            header_bytes = bytes2unpack[:8]
            unpacked.header.unpack(header_bytes)
            bytes2unpack = bytes2unpack[8:unpacked.header.length.value]
        unpacked.unpack(bytes2unpack)

        assert pyof_obj == unpacked
        assert pyof_obj.get_size() == unpacked.get_size()

    def test_minimum_size(self):
        """Test struct minimum size."""
        obj = self._msg_self()
        if self._min_size is None:
            raise Exception(f'{self.__class__.__name__}._min_size is not set')
        assert obj.get_size() == self._min_size
