"""RoleReply message tests."""
from pyof.v0x04.controller2switch.role_reply import RoleReply
from tests.unit.test_struct import StructTest


class TestRoleReply(StructTest):
    """Test the RoleReply message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_role_reply')
        self.set_raw_dump_object(RoleReply, xid=3, role=0,
                                    generation_id=0)
        self.set_minimum_size(24)
