"""GetAsyncReply message tests."""
from pyof.v0x04.controller2switch.get_async_reply import GetAsyncReply
from tests.unit.test_struct import StructTest


class TestGetAsyncReply(StructTest):
    """Test the GetAsyncReply message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_get_async_reply')
        self.set_raw_dump_object(GetAsyncReply, xid=3, packet_in_mask1=0,
                                    packet_in_mask2=0, port_status_mask1=0,
                                    port_status_mask2=0, flow_removed_mask1=0,
                                    flow_removed_mask2=0)
        self.set_minimum_size(32)
