"""Barrier request message tests."""
from pyof.v0x04.controller2switch.barrier_request import BarrierRequest
from tests.unit.test_struct import StructTest


class TestBarrierRequest(StructTest):
    """Barrier reply message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_barrier_request')
        self.set_raw_dump_object(BarrierRequest, xid=5)
        self.set_minimum_size(8)
