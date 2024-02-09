"""Test GetConfigRequest message."""
from pyof.v0x01.controller2switch.get_config_request import GetConfigRequest
from tests.unit.test_struct import StructTest


class TestGetConfigRequest(StructTest):
    """Test class for TestGetConfigRequest."""

    def setup_method(self):
        """[Controller2Switch/GetConfigRequest] - size 8."""
        self.set_raw_dump_file('v0x01', 'ofpt_get_config_request')
        self.set_raw_dump_object(GetConfigRequest, xid=1)
        self.set_minimum_size(8)
