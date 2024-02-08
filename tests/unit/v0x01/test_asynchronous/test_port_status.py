"""Port Status message tests."""
from pyof.foundation.basic_types import HWAddress
from pyof.v0x01.asynchronous.port_status import PortReason, PortStatus
from pyof.v0x01.common.phy_port import PhyPort, PortFeatures, PortState
from tests.unit.test_struct import StructTest


class TestPortStatus(StructTest):
    """Test the Port Status message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_port_status')
        self.set_raw_dump_object(_new_portstatus)
        self.set_minimum_size(64)


def _new_portstatus():
    """Crate new PortStatus and PhyPort instances."""
    desc_name = 's1-eth1'
    desc = PhyPort(port_no=1,
                   hw_addr=HWAddress('9a:da:11:8a:f4:0c'),
                   name=desc_name,
                   state=PortState.OFPPS_STP_LISTEN,
                   curr=PortFeatures.OFPPF_10GB_FD | PortFeatures.OFPPF_COPPER)
    return PortStatus(xid=0,
                      reason=PortReason.OFPPR_MODIFY,
                      desc=desc)
