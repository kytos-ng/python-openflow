"""Barrier reply message tests."""
from pyof.v0x01.controller2switch.barrier_reply import BarrierReply
from tests.unit.test_struct import StructTest


class TestBarrierReply(StructTest):
    """Barrier reply message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_barrier_reply')
        self.set_raw_dump_object(BarrierReply, xid=5)
        self.set_minimum_size(8)
