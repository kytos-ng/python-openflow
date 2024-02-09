"""Automate struct tests."""
from pyof.v0x04.common.header import Header
from pyof.v0x04.common.utils import new_message_from_header


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
                    # Create BarrierReply(xid=5)
                    self.set_message(BarrierReply, xid=5)
                    # As in spec: ``OFP_ASSERT(sizeof(struct ...) == ...);``
                    self.set_minimum_size(8)

        To only test the minimum size and skip packing/unpacking:

        .. code-block:: python3
            class TestMine(StructTest):
                def setup_method(self):
                    self.set_message(BarrierReply)
                    self.set_minimum_size(8)
    """

    def setup_method(self):
        """This parent class will not perform tests because its name does not
        start with "Test".

        The tests in this class are executed through the child, so there's no
        no need for them to be executed once more through the parent.
        """
        self._msg_self = None
        self._msg_params = None
        self._min_size = None

    def set_message(self, msg_self, *args, **kwargs):
        """Set how to create the message object.

        Args:
            msg_class (:obj:`type`): The message class followed by its
                parameters to instantiate an object.

        Example:
            ``self.set_message(BarrierReply, xid=5)`` will create
            ``BarrierReply(xid=5)``.
        """
        self._msg_self = msg_self
        self._msg_params = (args, kwargs)

    def set_minimum_size(self, size):
        """Set the struct minimum size (from spec).

        The minimum size can be found in OF spec. For example,
        :class:`.PhyPort` minimum size is 48 because of
        ``OFP_ASSERT(sizeof(struct ofp_phy_port) == 48);`` (spec 1.0.0).

        Args:
            size (int): The minimum size of the struct, in bytes.
        """
        self._min_size = size

    def test_pack_unpack(self):
        """Pack the message, unpack and check whether they are the same."""
        if self._msg_self:
            args, kwargs = self._msg_params
            self._test_pack_unpack(*args, **kwargs)

    def _test_pack_unpack(self, *args, **kwargs):
        """Pack the message, unpack and check whether they are the same.

        Call this method multiple times if you want to test more than one
        object.
        """
        obj = self._msg_self(*args, **kwargs)
        packed = obj.pack()
        header = Header()
        header_size = header.get_size()
        header.unpack(packed[:header_size])
        unpacked = new_message_from_header(header)
        unpacked.unpack(packed[header_size:])

        assert packed == unpacked.pack()

    def test_minimum_size(self):
        """Test struct minimum size."""
        if self._min_size is None:
            raise self.skipTest('minimum size was not set.')
        obj = self._msg_self()
        assert obj.get_size() == self._min_size
