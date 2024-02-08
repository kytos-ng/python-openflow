"""Config Port Stats message tests."""
from pyof.v0x04.controller2switch.multipart_reply import PortStats
from tests.unit.test_struct import StructTest


class TestPortStats(StructTest):
    """Config Port Stats message tests."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_port_stats')
        self.set_raw_dump_object(PortStats)
        self.set_minimum_size(112)
