"""Test VendorStats message."""
from pyof.v0x01.controller2switch.common import StatsType, VendorStats
from pyof.v0x01.controller2switch.stats_request import StatsRequest
from tests.unit.test_struct import StructTest


class TestVendorStats(StructTest):
    """Test class for TestVendorStats.

    The dump and unpacked data were provided by user bug report.
    """

    def setup_method(self):
        """[Controller2Switch/VendorStats] - size 1056."""
        self.set_raw_dump_file('v0x01', 'ofpt_vendor_stats_reply')
        self.set_raw_dump_object(StatsRequest, xid=4,
                                    body_type=StatsType.OFPST_VENDOR,
                                    flags=0, body=_get_vendor_stats())
        self.set_minimum_size(12)


def _get_vendor_stats():
    """Return vendor stats found in StatsReply.body."""
    body = b'\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\x00\xff\x00\x00\x00'
    return VendorStats(vendor=0x2320, body=body)
