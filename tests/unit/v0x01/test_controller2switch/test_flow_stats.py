"""Test FlowStats message."""
from pyof.v0x01.common.flow_match import Match
from pyof.v0x01.controller2switch.common import FlowStats, StatsType
from pyof.v0x01.controller2switch.stats_reply import StatsReply
from tests.unit.test_struct import StructTest


class TestFlowStats(StructTest):
    """Test class for TestFlowStats."""

    def setup_method(self):
        """[Controller2Switch/FlowStats] - size 88."""
        self.set_raw_dump_file('v0x01', 'ofpt_flow_stats_reply')
        self.set_raw_dump_object(StatsReply, xid=12,
                                    body_type=StatsType.OFPST_FLOW,
                                    flags=0, body=_get_flow_stats())
        self.set_minimum_size(12)


def _get_flow_stats():
    """Function used to return a FlowStats instance."""
    return FlowStats(length=160, table_id=1,
                     match=_get_match(), duration_sec=60,
                     duration_nsec=10000, priority=1,
                     idle_timeout=300, hard_timeout=6000,
                     cookie=1, packet_count=1, byte_count=1)


def _get_match():
    """Function used to return a Match instance."""
    return Match(in_port=80, dl_src='01:02:03:04:05:06',
                 dl_dst='01:02:03:04:05:06', dl_vlan=1,
                 dl_vlan_pcp=1, dl_type=1,
                 nw_tos=1, nw_proto=1,
                 nw_src='192.168.0.1', nw_dst='192.168.0.1',
                 tp_src=80, tp_dst=80)
