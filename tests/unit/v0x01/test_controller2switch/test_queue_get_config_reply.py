"""Test for QueueGetConfigReply message."""
from pyof.v0x01.common.phy_port import Port
from pyof.v0x01.common.queue import (
    PacketQueue, QueueProperties, QueuePropHeader)
from pyof.v0x01.controller2switch import queue_get_config_reply
from tests.unit.test_struct import StructTest


class TestQueueGetConfigReply(StructTest):
    """Test for QueueGetConfigReply message."""

    def setup_method(self):
        """[Controller2Switch/QueueGetConfigReply] - size 16."""
        self.set_raw_dump_file('v0x01', 'ofpt_queue_get_config_reply')
        self.set_raw_dump_object(queue_get_config_reply.QueueGetConfigReply,
                                    xid=1, port=Port.OFPP_ALL,
                                    queues=_get_packet_queue())
        self.set_minimum_size(16)


def _get_packet_queue():
    """Function used to return a PacketQueue instance."""
    packets = []
    packets.append(PacketQueue(queue_id=1, length=8,
                               properties=_get_queue_properties()))
    return packets


def _get_queue_properties():
    """Function used to return a list of queue properties."""
    properties = []
    properties.append(QueuePropHeader(
        queue_property=QueueProperties.OFPQT_MIN_RATE, length=12))
    return properties
