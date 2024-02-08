"""Set Config message tests."""
from pyof.v0x04.common.action import ControllerMaxLen
from pyof.v0x04.controller2switch.common import ConfigFlag
from pyof.v0x04.controller2switch.set_config import SetConfig
from tests.unit.test_struct import StructTest


class TestSetConfig(StructTest):
    """Test the Set Config message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        buffer = ControllerMaxLen.OFPCML_NO_BUFFER
        self.set_raw_dump_file('v0x04', 'ofpt_set_config')
        self.set_raw_dump_object(SetConfig, xid=1201346349,
                                    flags=ConfigFlag.OFPC_FRAG_NORMAL,
                                    miss_send_len=buffer)
        self.set_minimum_size(12)
