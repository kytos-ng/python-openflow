"""Test for StatsRequest message."""
from pyof.v0x01.controller2switch.common import StatsType
from pyof.v0x01.controller2switch.stats_request import StatsRequest
from tests.unit.test_struct import StructTest


class TestStatsRequest(StructTest):
    """Test for StatsRequest message."""

    def setup_method(self):
        """[Controller2Switch/StatsRequest] - size 12."""
        self.set_raw_dump_file('v0x01', 'ofpt_stats_request')
        self.set_raw_dump_object(StatsRequest, xid=1,
                                    body_type=StatsType.OFPST_FLOW,
                                    flags=1, body=b'')
        self.set_minimum_size(12)
