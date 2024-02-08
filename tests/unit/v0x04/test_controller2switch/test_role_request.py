"""RoleRequest message tests."""
from pyof.v0x04.controller2switch.role_request import RoleRequest
from tests.unit.test_struct import StructTest


class TestRoleRequest(StructTest):
    """Test the RoleRequest message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_role_request')
        self.set_raw_dump_object(RoleRequest, xid=3, role=0,
                                    generation_id=0)
        self.set_minimum_size(24)
