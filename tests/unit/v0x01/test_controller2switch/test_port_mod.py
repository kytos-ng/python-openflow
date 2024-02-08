"""Test PortMod message."""
from pyof.v0x01.common.phy_port import PortConfig, PortFeatures
from pyof.v0x01.controller2switch.port_mod import PortMod
from tests.unit.test_struct import StructTest


class TestPortMod(StructTest):
    """Test class for PortMod."""

    def setup_method(self):
        """[Controller2Switch/PortMod] - size 32."""
        self.set_raw_dump_file('v0x01', 'ofpt_port_mod')
        self.set_raw_dump_object(PortMod, xid=3, port_no=80,
                                    hw_addr='aa:bb:cc:00:33:9f',
                                    config=PortConfig.OFPPC_PORT_DOWN,
                                    mask=PortConfig.OFPPC_NO_FWD,
                                    advertise=PortFeatures.OFPPF_FIBER)
        self.set_minimum_size(32)
