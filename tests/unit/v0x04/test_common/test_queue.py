"""Test of v0x04 queue module."""
from pyof.v0x04.common.queue import (
    PacketQueue, QueuePropExperimenter, QueuePropHeader, QueuePropMaxRate,
    QueuePropMinRate)
from tests.unit.test_struct import StructTest


class TestPacketQueue(StructTest):
    """Packet Queue structure tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'packet_queue')
        self.set_raw_dump_object(PacketQueue)
        self.set_minimum_size(16)


class TestQueuePropExperimenter(StructTest):
    """QueuePropExperimenter tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'queue_prop_experimenter')
        self.set_raw_dump_object(QueuePropExperimenter)
        self.set_minimum_size(16)


class TestQueuePropHeader(StructTest):
    """QueuePropHeader structure tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'queue_prop_header')
        self.set_raw_dump_object(QueuePropHeader)
        self.set_minimum_size(8)


class TestQueuePropMaxRate(StructTest):
    """QueuePropMaxRate structure tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'queue_prop_max_rate')
        self.set_raw_dump_object(QueuePropMaxRate)
        self.set_minimum_size(16)


class TestQueuePropMinRate(StructTest):
    """QueuePropMinRate structure tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'queue_prop_min_rate')
        self.set_raw_dump_object(QueuePropMinRate)
        self.set_minimum_size(16)
