"""Aggregate stats request message."""
from pyof.v0x04.controller2switch.common import MultipartType
from pyof.v0x04.controller2switch.multipart_reply import (
    AggregateStatsReply, MultipartReply)
from tests.unit.test_struct import StructTest


class TestAggregateStats(StructTest):
    """Aggregate stats message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        mp_type = MultipartType.OFPMP_AGGREGATE
        self.set_raw_dump_file('v0x04', 'ofpt_aggregate_stats')
        self.set_raw_dump_object(MultipartReply, xid=1,
                                    multipart_type=mp_type,
                                    flags=0,
                                    body=_get_body())
        self.set_minimum_size(16)


def _get_body():
    """Return the body used by MultipartReply message."""
    return AggregateStatsReply(packet_count=2, byte_count=220, flow_count=2)
