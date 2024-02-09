"""Config Reply message tests."""
from pyof.v0x04.controller2switch.get_config_reply import GetConfigReply
from tests.unit.test_struct import StructTest


class TestGetConfigReply(StructTest):
    """Config Reply message tests."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_get_config_reply')
        self.set_raw_dump_object(GetConfigReply, xid=1)
        self.set_minimum_size(12)
