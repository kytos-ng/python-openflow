"""Table stats message."""
from pyof.v0x04.controller2switch.multipart_reply import TableStats
from tests.unit.test_struct import StructTest


class TestTableStats(StructTest):
    """Table stats message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_table_stats')
        self.set_raw_dump_object(TableStats)
        self.set_minimum_size(24)
