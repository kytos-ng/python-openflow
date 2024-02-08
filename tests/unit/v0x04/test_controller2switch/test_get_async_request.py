"""GetAsyncRequest message tests."""
from pyof.v0x04.controller2switch.get_async_request import GetAsyncRequest
from tests.unit.test_struct import StructTest


class TestGetAsyncRequest(StructTest):
    """Test the GetAsyncRequest message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_get_async_request')
        self.set_raw_dump_object(GetAsyncRequest, xid=3)
        self.set_minimum_size(8)
