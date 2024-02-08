"""Test for QueueStats."""
from pyof.v0x01.controller2switch.common import QueueStats, StatsType
from pyof.v0x01.controller2switch.stats_reply import StatsReply
from tests.unit.test_struct import StructTest


class TestQueueStats(StructTest):
    """Test for QueueStats."""

    def setup_method(self):
        """[Controller2Switch/QueueStats] - size 32."""
        self.set_raw_dump_file('v0x01', 'ofpt_queue_stats')
        self.set_raw_dump_object(StatsReply, xid=7,
                                    body_type=StatsType.OFPST_QUEUE,
                                    flags=0, body=_get_queue_stats())
        self.set_minimum_size(12)


def _get_queue_stats():
    """Function used to return a QueueStats instance."""
    return QueueStats(port_no=80, queue_id=5, tx_bytes=1,
                      tx_packets=3, tx_errors=2)
