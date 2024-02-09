"""Experimenter message tests."""
from pyof.v0x04.symmetric.experimenter import ExperimenterHeader
from tests.unit.test_struct import StructTest


class TestExperimenter(StructTest):
    """Experimenter message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_experimenter')
        self.set_raw_dump_object(ExperimenterHeader, xid=1, experimenter=1,
                                    exp_type=0)
        self.set_minimum_size(16)
