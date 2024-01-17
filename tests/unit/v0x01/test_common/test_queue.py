"""Testing Queue structure."""
import pytest
import unittest

from pyof.v0x01.common import queue


class TestQueuePropHeader:
    """Test QueuePropHeader."""

    def setup_method(self):
        """Basic setup for test."""
        self.message = queue.QueuePropHeader()
        self.message.queue_property = queue.QueueProperties.OFPQT_MIN_RATE
        self.message.length = 12

    def test_get_size(self):
        """[Common/QueuePropHeader] - size 8."""
        assert self.message.get_size() == 8

    @pytest.mark.skip('Not yet implemented')
    def test_pack(self):
        """[Common/QueuePropHeader] - packing."""
        pass

    @pytest.mark.skip('Not yet implemented')
    def test_unpack(self):
        """[Common/QueuePropHeader] - unpacking."""
        pass


class TestPacketQueue:
    """TestPacketQueue."""

    def setup_method(self):
        """Basic setup for test."""
        self.message = queue.PacketQueue()
        self.message.queue_id = 1
        self.message.length = 8

    def test_get_size(self):
        """[Common/PacketQueue] - size 8."""
        assert self.message.get_size() == 8

    @pytest.mark.skip('Not yet implemented')
    def test_pack(self):
        """[Common/PacketQueue] - packing."""
        pass

    @pytest.mark.skip('Not yet implemented')
    def test_unpack(self):
        """[Common/PacketQueue] - unpacking."""
        pass


class TestQueuePropMinRate:
    """Test QueuePropMinRate."""

    def setup_method(self):
        """Basic setup for test."""
        self.message = queue.QueuePropMinRate()
        self.message.rate = 1000

    def test_get_size(self):
        """[Common/PropMinRate] - size 16."""
        assert self.message.get_size() == 16

    @pytest.mark.skip('Not yet implemented')
    def test_pack(self):
        """[Common/PropMinRate] - packing."""
        pass

    @pytest.mark.skip('Not yet implemented')
    def test_unpack(self):
        """[Common/PropMinRate] - unpacking."""
        pass
