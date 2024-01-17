"""Test Python-openflow network types."""
import pytest
import unittest

from pyof.foundation.basic_types import BinaryData
from pyof.foundation.exceptions import UnpackException
from pyof.foundation.network_types import (
    ARP, VLAN, Ethernet, GenericTLV, IPv4, IPv6)


class TestARP:
    """Test ARP packets, without Ethernet headers."""

    def test_arp_pack(self):
        """Test pack method of ARP class."""
        arp = ARP(oper=1, sha='00:15:af:d5:38:98', spa='172.16.0.10',
                  tpa='172.16.10.20')
        packed = arp.pack()
        expected = b'\x00\x01\x08\x00\x06\x04\x00\x01\x00\x15\xaf\xd58\x98\xac'
        expected += b'\x10\x00\n\x00\x00\x00\x00\x00\x00\xac\x10\n\x14'
        assert packed == expected

    def test_arp_unpack(self):
        """Test unpack method of ARP class."""
        raw = b'\x00\x01\x08\x00\x06\x04\x00\x02\x00\x1f:>\x9a\xcf\xac\x10\n'
        raw += b'\x14\x00\x15\xaf\xd58\x98\xac\x10\x00\n'
        expected = ARP(oper=2, sha='00:1f:3a:3e:9a:cf', spa='172.16.10.20',
                       tha='00:15:af:d5:38:98', tpa='172.16.0.10')
        unpacked = ARP()
        unpacked.unpack(raw)
        assert unpacked == expected

    def test_unpack_invalid_htype(self):
        """Raise UnpackException when L2 protocol is not Ethernet."""
        raw = b'\x01\x23\x08\x00\x06\x04\x00\x02\x00\x1f:>\x9a\xcf\xac\x10\n'
        raw += b'\x14\x00\x15\xaf\xd58\x98\xac\x10\x00\n'
        arp = ARP()
        with pytest.raises(UnpackException):
            arp.unpack(raw)

    def test_unpack_invalid_ptype(self):
        """Raise UnpackException when L3 protocol is not IPv4."""
        raw = b'\x00\x01\x08\x90\x06\x04\x00\x02\x00\x1f:>\x9a\xcf\xac\x10\n'
        raw += b'\x14\x00\x15\xaf\xd58\x98\xac\x10\x00\n'
        arp = ARP()
        with pytest.raises(UnpackException):
            arp.unpack(raw)


class TestNetworkTypes:
    """Reproduce bugs found."""

    def test_gen_tlv_value_unpack(self):
        """Value attribute should be the same after unpacking."""
        value = BinaryData(b'test')
        tlv = GenericTLV(value=value)
        tlv_unpacked = GenericTLV()
        tlv_unpacked.unpack(tlv.pack())
        assert tlv.value.value == tlv_unpacked.value.value


class TestEthernet:
    """Test Ethernet frames."""

    def test_ethernet_pack(self):
        """Test pack method of Ethernet class without VLAN tag."""
        ethernet = Ethernet(destination='00:1f:3a:3e:9a:cf',
                            source='00:15:af:d5:38:98', ether_type=0x800,
                            data=b'testdata')
        packed = ethernet.pack()
        expected = b'\x00\x1f:>\x9a\xcf\x00\x15\xaf\xd58\x98\x08\x00testdata'
        assert packed == expected

    def test_ethernet_unpack(self):
        """Test pack method of Ethernet class without VLAN tag."""
        raw = b'\x00\x15\xaf\xd58\x98\x00\x1f:>\x9a\xcf\x08\x00testdata'
        expected = Ethernet(destination='00:15:af:d5:38:98',
                            source='00:1f:3a:3e:9a:cf', ether_type=0x800,
                            data=b'testdata')
        expected.pack()
        unpacked = Ethernet()
        unpacked.unpack(raw)
        assert unpacked == expected

    def test_tagged_ethernet_pack(self):
        """Test pack method of Ethernet class including VLAN tag."""
        ethernet = Ethernet(destination='00:1f:3a:3e:9a:cf',
                            source='00:15:af:d5:38:98', vlans=[VLAN(vid=200)],
                            ether_type=0x800, data=b'testdata')
        packed = ethernet.pack()
        expected = b'\x00\x1f:>\x9a\xcf\x00\x15\xaf\xd58'
        expected += b'\x98\x81\x00\x00\xc8\x08\x00testdata'
        assert packed == expected

    def test_tagged_ethernet_unpack(self):
        """Test pack method of Ethernet class including VLAN tag."""
        raw = b'\x00\x15\xaf\xd58\x98\x00\x1f:>'
        raw += b'\x9a\xcf\x81\x00!^\x08\x00testdata'
        expected = Ethernet(destination='00:15:af:d5:38:98',
                            source='00:1f:3a:3e:9a:cf', vlans=[VLAN(pcp=1,
                                                                  vid=350)],
                            ether_type=0x800, data=b'testdata')
        expected.pack()
        unpacked = Ethernet()
        unpacked.unpack(raw)
        assert unpacked == expected


class TestVLAN:
    """Test VLAN headers."""

    def test_vlan_pack(self):
        """Test pack method of VLAN class."""
        vlan = VLAN(pcp=3, vid=20)
        packed = vlan.pack()
        expected = b'\x81\x00`\x14'
        assert packed == expected

    def test_vlan_unpack(self):
        """Test unpack method of VLAN class."""
        raw = b'\x81\x00\xa0{'
        expected = VLAN(pcp=5, vid=123)
        unpacked = VLAN()
        unpacked.unpack(raw)
        assert unpacked == expected

    def test_unpack_wrong_tpid(self):
        """Raise UnpackException if the tpid is not VLAN_TPID."""
        raw = b'\x12\x34\xa0{'
        vlan = VLAN()
        with pytest.raises(UnpackException):
            vlan.unpack(raw)


class TestIPv4:
    """Test IPv4 packets."""

    def test_ipv4_pack(self):
        """Test pack/unpack of IPv4 class."""
        packet = IPv4(dscp=10, ttl=64, protocol=17, source="192.168.0.10",
                      destination="172.16.10.30", options=b'1000',
                      data=b'testdata')
        packed = packet.pack()
        expected = b'F(\x00 \x00\x00\x00\x00@\x11\x02'
        expected += b'\xc5\xc0\xa8\x00\n\xac\x10\n\x1e1000testdata'
        assert packed == expected

    def test_ipv4_unpack(self):
        """Test unpack of IPv4 binary packet."""
        raw = b'FP\x00$\x00\x00\x00\x00\x80\x06W'
        raw += b'\xf4\n\x9aN\x81\xc0\xa8\xc7\xcc1000somemoredata'
        expected = IPv4(dscp=20, ttl=128, protocol=6, source="10.154.78.129",
                        destination="192.168.199.204", options=b'1000',
                        data=b'somemoredata')
        expected.pack()
        unpacked = IPv4()
        unpacked.unpack(raw)
        assert unpacked == expected

    def test_ipv4_size(self):
        """Test Header size for IPv4 packet."""
        packet = IPv4()
        packet.pack()
        assert 20 == packet.get_size()
        assert 20 == packet.length
        assert 20 == packet.ihl * 4

    def test_ipv4_checksum(self):
        """Test if the IPv4 checksum is being calculated correclty."""
        packet = IPv4(dscp=10, ttl=64, protocol=17, source="192.168.0.10",
                      destination="172.16.10.30", options=b'1000',
                      data=b'testdata')
        packet.pack()
        assert packet.checksum == 709


class TestIPv6:
    """Test IPv6 packets."""

    def test_ipv6_pack(self):
        """Test pack/unpack of IPv6 class."""
        packet = IPv6(next_header=6, hop_limit=64, source="::1",
                      destination="::2", data=b'testdata')
        packed = packet.pack()
        expected = b'`\x00\x00\x00\x00\x08\x06@\x00\x00'
        expected += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        expected += b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        expected += b'\x00\x00\x00\x02testdata'
        assert packed == expected

    def test_ipv6_unpack(self):
        """Test unpack of IPv6 binary packet."""
        raw = b'`\x00\x00\x00\x00\x0c\x06@\x00\x00'
        raw += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        raw += b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        raw += b'\x00\x00\x00\x01somemoredata'
        expected = IPv6(next_header=6, hop_limit=64, source="::2",
                        destination="::1", data=b'somemoredata')
        expected.pack()
        unpacked = IPv6()
        unpacked.unpack(raw)
        assert unpacked == expected
