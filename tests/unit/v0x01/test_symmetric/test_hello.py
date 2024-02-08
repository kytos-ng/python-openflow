"""Hello message tests."""
from pyof.v0x01.symmetric.hello import Hello
from tests.unit.test_struct import StructTest


class TestHello(StructTest):
    """Hello message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_hello')
        self.set_raw_dump_object(Hello, xid=1)
        self.set_minimum_size(8)
