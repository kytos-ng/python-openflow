"""Testing FlowMatch structure."""
import pytest

from pyof.v0x01.common import flow_match


class TestMatch:
    """Test Match structure."""

    def setup_method(self):
        """Basic setup for test."""
        self.message = flow_match.Match()
        self.message.in_port = 22
        self.message.dl_src = [1, 2, 3, 4, 5, 6]
        self.message.dl_dst = [1, 2, 3, 4, 5, 6]
        self.message.dl_vlan = 1
        self.message.dl_vlan_pcp = 1
        self.message.dl_type = 1
        self.message.nw_tos = 1
        self.message.nw_proto = 1
        self.message.nw_src = [192, 168, 0, 1]
        self.message.nw_dst = [192, 168, 0, 2]
        self.message.tp_src = 22
        self.message.tp_dst = 22

    def test_get_size(self):
        """[Common/FlowMatch] - size 40."""
        assert self.message.get_size() == 40

    def test_pack_unpack(self):
        """[Common/FlowMatch] - packing and unpacking."""
        pack = self.message.pack()
        unpacked = flow_match.Match()
        unpacked.unpack(pack)
        assert self.message.pack() == unpacked.pack()

    @pytest.mark.skip('Not yet implemented')
    def test_pack(self):
        """[Common/FlowMatch] - packing."""
        pass

    @pytest.mark.skip('Not yet implemented')
    def test_unpack(self):
        """[Common/FlowMatch] - unpacking."""
        pass
