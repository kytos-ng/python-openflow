"""Set Config message tests."""
from pyof.v0x01.controller2switch.common import ConfigFlag
from pyof.v0x01.controller2switch.set_config import SetConfig
from tests.unit.test_struct import StructTest


class TestSetConfig(StructTest):
    """Test the Set Config message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_set_config')
        self.set_raw_dump_object(SetConfig, xid=3,
                                    flags=ConfigFlag.OFPC_FRAG_NORMAL,
                                    miss_send_len=128)
        self.set_minimum_size(12)
