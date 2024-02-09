"""Echo reply message tests."""
from pyof.v0x01.symmetric.echo_reply import EchoReply
from tests.unit.test_struct import StructTest


class TestEchoReply(StructTest):
    """Echo reply message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_echo_reply')
        self.set_raw_dump_object(EchoReply, xid=0)
        self.set_minimum_size(8)
