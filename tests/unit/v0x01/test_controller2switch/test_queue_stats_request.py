"""Test for QueueStatsRequest message."""
from pyof.v0x01.controller2switch.common import QueueStatsRequest, StatsType
from pyof.v0x01.controller2switch.stats_request import StatsRequest
from tests.unit.test_struct import StructTest


class TestQueueStatsRequest(StructTest):
    """Test for QueueStatsRequest message."""

    def setup_method(self):
        """[Controller2Switch/QueueStatsRequest] - size 8."""
        self.set_raw_dump_file('v0x01', 'ofpt_queue_stats_request')
        self.set_raw_dump_object(StatsRequest, xid=14,
                                    body_type=StatsType.OFPST_QUEUE,
                                    flags=0,
                                    body=QueueStatsRequest(port_no=80,
                                                           queue_id=5))
        self.set_minimum_size(12)
