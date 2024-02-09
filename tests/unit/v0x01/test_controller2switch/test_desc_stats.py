"""Test DescStats message."""
from pyof.foundation.constants import DESC_STR_LEN
from pyof.v0x01.controller2switch.common import DescStats, StatsType
from pyof.v0x01.controller2switch.stats_reply import StatsReply
from tests.unit.test_struct import StructTest


class TestDescStats(StructTest):
    """Test class for TestDescStats."""

    def setup_method(self):
        """[Controller2Switch/DescStats] - size 1056."""
        self.set_raw_dump_file('v0x01', 'ofpt_desc_stats_reply')
        self.set_raw_dump_object(StatsReply, xid=14,
                                    body_type=StatsType.OFPST_DESC,
                                    flags=0, body=_get_desc_stats())
        self.set_minimum_size(12)


def _get_desc_stats():
    """Function used to return desc_stat used by StatsReply instance."""
    content = 'A' * DESC_STR_LEN
    return DescStats(mfr_desc=content, hw_desc=content,
                     sw_desc=content, serial_num=content,
                     dp_desc=content)
