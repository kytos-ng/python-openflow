"""Test of Port class from common module."""
from pyof.v0x04.common.port import Port
from tests.unit.test_struct import StructTest


class TestPort(StructTest):
    """Port structure tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'port')
        self.set_raw_dump_object(Port)
        self.set_minimum_size(64)
