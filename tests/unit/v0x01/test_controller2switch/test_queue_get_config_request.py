"""Test for QueueGetConfigRequest message."""
from pyof.v0x01.common.phy_port import Port
from pyof.v0x01.controller2switch import queue_get_config_request as request
from tests.unit.test_struct import StructTest


class TestQueueGetConfigRequest(StructTest):
    """Test for QueueGetConfigRequest message."""

    def setup_method(self):
        """[Controller2Switch/QueueGetConfigRequest] - size 12."""
        self.set_raw_dump_file('v0x01', 'ofpt_queue_get_config_request')
        self.set_raw_dump_object(request.QueueGetConfigRequest,
                                    xid=1, port=Port.OFPP_MAX)
        self.set_minimum_size(12)
