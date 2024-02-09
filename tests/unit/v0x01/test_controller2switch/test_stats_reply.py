"""Test for StatsReply message."""
from pyof.v0x01.controller2switch.common import StatsType
from pyof.v0x01.controller2switch.stats_reply import StatsReply
from tests.unit.test_struct import StructTest


class TestStatsReply(StructTest):
    """Test for StatsReply message."""

    def setup_method(self):
        """[Controller2Switch/StatsReply] - size 12."""
        self.set_raw_dump_file('v0x01', 'ofpt_stats_reply')
        self.set_raw_dump_object(StatsReply, xid=1,
                                    body_type=StatsType.OFPST_FLOW,
                                    flags=0x0001, body=b'')
        self.set_minimum_size(12)
