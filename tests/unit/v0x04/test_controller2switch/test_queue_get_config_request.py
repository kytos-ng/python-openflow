"""Testing QueueGetConfigRequest message."""
from pyof.v0x04.controller2switch.queue_get_config_request import (
    QueueGetConfigRequest)
from tests.unit.test_struct import StructTest


class TestQueueGetConfigRequest(StructTest):
    """Test the QueueGetConfigRequest message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_queue_get_config_request')
        self.set_raw_dump_object(QueueGetConfigRequest, xid=1, port=1)
        self.set_minimum_size(16)
