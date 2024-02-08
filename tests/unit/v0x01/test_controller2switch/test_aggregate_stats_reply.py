"""Test for AggregateStatsReply message."""
from pyof.v0x01.controller2switch.common import AggregateStatsReply, StatsType
from pyof.v0x01.controller2switch.stats_reply import StatsReply
from tests.unit.test_struct import StructTest


class TestAggregateStatsReply(StructTest):
    """Test for AggregateStatsReply message."""

    def setup_method(self):
        """[Controller2Switch/AggregateStatsReply] - size 24."""
        aggregate_stats_reply = AggregateStatsReply(packet_count=5,
                                                    byte_count=1, flow_count=8)
        self.set_raw_dump_file('v0x01', 'ofpt_aggregate_stats_reply')
        self.set_raw_dump_object(StatsReply, xid=17,
                                    body_type=StatsType.OFPST_AGGREGATE,
                                    flags=0, body=aggregate_stats_reply)
        self.set_minimum_size(12)
