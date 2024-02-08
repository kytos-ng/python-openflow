"""Test for PortStatsRequest."""
from pyof.v0x01.controller2switch.common import PortStatsRequest, StatsType
from pyof.v0x01.controller2switch.stats_request import StatsRequest
from tests.unit.test_struct import StructTest


class TestPortStatsRequest(StructTest):
    """Test for PortStatsRequest."""

    def setup_method(self):
        """[Controller2Switch/PortStatsRequest] - size 8."""
        self.set_raw_dump_file('v0x01', 'ofpt_port_stats_request')
        self.set_raw_dump_object(StatsRequest, xid=17,
                                    body_type=StatsType.OFPST_PORT,
                                    flags=0, body=PortStatsRequest(port_no=80))
        self.set_minimum_size(12)
