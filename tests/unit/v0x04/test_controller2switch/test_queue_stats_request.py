"""Queue Stat Request message."""
from pyof.v0x04.controller2switch.multipart_request import QueueStatsRequest
from tests.unit.test_struct import StructTest


class TestQueueStatsRequest(StructTest):
    """Queue Stat Request message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_queue_stats_request')
        self.set_raw_dump_object(QueueStatsRequest)
        self.set_minimum_size(8)
