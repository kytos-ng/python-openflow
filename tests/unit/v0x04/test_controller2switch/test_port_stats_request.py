"""Config Port Stats Request message tests."""
from pyof.v0x04.controller2switch.multipart_request import PortStatsRequest
from tests.unit.test_struct import StructTest


class TestPortStatsRequest(StructTest):
    """Config Port Stats Request message tests."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_port_stats_request')
        self.set_raw_dump_object(PortStatsRequest)
        self.set_minimum_size(8)
