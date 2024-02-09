"""Echo request message tests."""
from pyof.v0x04.symmetric.echo_request import EchoRequest
from tests.unit.test_struct import StructTest


class TestEchoRequest(StructTest):
    """Echo request message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_echo_request')
        self.set_raw_dump_object(EchoRequest, xid=0)
        self.set_minimum_size(8)
