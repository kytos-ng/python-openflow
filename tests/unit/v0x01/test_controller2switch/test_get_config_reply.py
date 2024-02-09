"""Test GetConfigReply message."""
from pyof.v0x01.controller2switch.common import ConfigFlag
from pyof.v0x01.controller2switch.get_config_reply import GetConfigReply
from tests.unit.test_struct import StructTest


class TestGetConfigReply(StructTest):
    """Test class for TestGetConfigReply."""

    def setup_method(self):
        """[Controller2Switch/GetConfigReply] - size 12."""
        self.set_raw_dump_file('v0x01', 'ofpt_get_config_reply')
        self.set_raw_dump_object(GetConfigReply, xid=13,
                                    flags=ConfigFlag.OFPC_FRAG_REASM,
                                    miss_send_len=1024)
        self.set_minimum_size(12)
