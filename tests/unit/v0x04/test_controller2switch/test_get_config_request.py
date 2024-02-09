"""Config Request message tests."""
from pyof.v0x04.controller2switch.get_config_request import GetConfigRequest
from tests.unit.test_struct import StructTest


class TestGetConfigRequest(StructTest):
    """Config Request message tests."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_get_config_request')
        self.set_raw_dump_object(GetConfigRequest)
        self.set_minimum_size(8)
