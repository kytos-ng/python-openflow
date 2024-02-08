"""Stats queue message."""
from pyof.v0x04.controller2switch.multipart_reply import QueueStats
from tests.unit.test_struct import StructTest


class TestQueueStats(StructTest):
    """Stats queue message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_queue_stats')
        self.set_raw_dump_object(QueueStats)
        self.set_minimum_size(40)
