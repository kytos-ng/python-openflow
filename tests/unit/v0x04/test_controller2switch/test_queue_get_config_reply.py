"""Testing QueueGetConfigReply message."""
from pyof.v0x04.common.queue import ListOfQueues, PacketQueue
from pyof.v0x04.controller2switch.queue_get_config_reply import (
    QueueGetConfigReply)
from tests.unit.test_struct import StructTest


class TestQueueGetConfigReply(StructTest):
    """Test the QueueGetConfigReply message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_queue_get_config_reply')
        self.set_raw_dump_object(QueueGetConfigReply, xid=1, port=1,
                                    queues=_new_list_of_queues())
        self.set_minimum_size(16)


def _new_list_of_queues():
    """Crate new ListOfQueues."""
    queue = PacketQueue(1, 2, 3)
    loq = ListOfQueues([queue, queue])
    return loq
