"""Packet out message tests."""
from pyof.foundation.exceptions import ValidationError
from pyof.v0x04.common.action import ActionOutput
from pyof.v0x04.common.constants import OFP_NO_BUFFER
from pyof.v0x04.common.port import PortNo
from pyof.v0x04.controller2switch.packet_out import PacketOut
from tests.unit.test_struct import StructTest
import pytest
NO_RAW = 'No raw dump file found.'


class TestPacketOut(StructTest):
    """Packet out message tests (also those in :class:`.TestDump`).

    Attributes:
        message (PacketOut): The message configured in :meth:`setUpClass`.

    """

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x04', 'ofpt_packet_out')
        self.set_raw_dump_object(PacketOut, xid=2544740805,
                                    buffer_id=OFP_NO_BUFFER,
                                    in_port=PortNo.OFPP_CONTROLLER,
                                    actions=_get_actions(), data=_get_data())
        self.set_minimum_size(24)

    @pytest.mark.parametrize("port", 
        [
            PortNo.OFPP_LOCAL,
            PortNo.OFPP_CONTROLLER,
            PortNo.OFPP_ANY
        ]
    )
    def test_valid_virtual_in_ports(self, port):
        """Valid virtual ports as defined in 1.3.0 spec."""
        msg = PacketOut(in_port=port)
        assert msg.is_valid(), f'{port.name} should be a valid in_port'

    def test_invalid_virtual_in_ports(self):
        """Invalid virtual ports as defined in 1.3.0 spec."""
        try:
            msg = self.get_raw_dump().read()
        except FileNotFoundError:
            raise self.skipTest(NO_RAW)
        else:
            invalid = (PortNo.OFPP_IN_PORT, PortNo.OFPP_TABLE,
                       PortNo.OFPP_NORMAL, PortNo.OFPP_FLOOD, PortNo.OFPP_ALL)
            msg = self.get_raw_object()
            for in_port in invalid:
                msg.in_port = in_port
                assert not msg.is_valid()
                pytest.raises(ValidationError, msg.validate)

    def test_valid_physical_in_ports(self):
        """Physical port limits from 1.3.0 spec."""
        try:
            msg = self.get_raw_dump().read()
        except FileNotFoundError:
            raise self.skipTest(NO_RAW)
        else:
            max_valid = int(PortNo.OFPP_MAX.value) - 1
            msg = self.get_raw_object()
            for in_port in (1, max_valid):
                msg.in_port = in_port
                assert msg.is_valid()


def _get_actions():
    """Return a list of actions used by packetout instance."""
    action = ActionOutput(port=1)
    return [action]


def _get_data():
    """Return a BinaryData used by packetout instance."""
    data = b'\x01\x80\xc2\x00\x00\x0e\x4e\xbf\xca\x27\x8e\xca\x81\x00\x0e'
    data += b'\xd7\x88\xcc\x02\x09\x07\x00\x00\x00\x00\x00\x00\x00\x01\x04'
    data += b'\x05\x07\x00\x00\x00\x01\x06\x02\x00\x78\x00\x00'
    return data
