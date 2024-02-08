"""Feature request message tests."""
from pyof.v0x01.controller2switch.features_request import FeaturesRequest
from tests.unit.test_struct import StructTest


class TestFeaturesRequest(StructTest):
    """Feature request message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_features_request')
        self.set_raw_dump_object(FeaturesRequest, xid=3)
        self.set_minimum_size(8)
