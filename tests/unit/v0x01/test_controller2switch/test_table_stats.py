"""Test TableStats message."""
from pyof.foundation.constants import OFP_MAX_TABLE_NAME_LEN
from pyof.v0x01.common.flow_match import FlowWildCards
from pyof.v0x01.controller2switch.common import StatsType, TableStats
from pyof.v0x01.controller2switch.stats_reply import StatsReply
from tests.unit.test_struct import StructTest


class TestTableStats(StructTest):
    """Test class for TableStats."""

    def setup_method(self):
        """[Controller2Switch/TableStats] - size 64."""
        self.set_raw_dump_file('v0x01', 'ofpt_table_stats')
        self.set_raw_dump_object(StatsReply, xid=14,
                                    body_type=StatsType.OFPST_TABLE,
                                    flags=0, body=_get_table_stats())
        self.set_minimum_size(12)


def _get_table_stats():
    return TableStats(table_id=1,
                      name='X' * OFP_MAX_TABLE_NAME_LEN,
                      wildcards=FlowWildCards.OFPFW_TP_DST, max_entries=1,
                      active_count=10, count_lookup=10, count_matched=0)
