"""Tests for Python-openflow BasicTypes."""
import pytest

from pyof.foundation import basic_types
from pyof.foundation.exceptions import PackException
from pyof.foundation.basic_types import BinaryData


class TestUBInt8:
    """Test of UBInt8 BasicType."""

    def setup_method(self):
        """Basic test setup."""
        self.ubint8 = basic_types.UBInt8(255)

    def test_get_size(self):
        """[Foundation/BasicTypes/UBInt8] - size 1."""
        assert self.ubint8.get_size() == 1

    def test_pack(self):
        """[Foundation/BasicTypes/UBInt8] - packing."""
        assert self.ubint8.pack() == b'\xff'

    def test_unpack(self):
        """[Foundation/BasicTypes/UBInt8] - unpacking."""
        u = basic_types.UBInt8()
        u.unpack(b'\xfe')
        assert u.value == 254

    def test_pack_error(self):
        """[Foundation/BasicTypes/UBInt8] - packing exception."""
        u = basic_types.UBInt8(256)
        pytest.raises(PackException, u.pack)

    def test_cast_to_int(self):
        assert 255 == int(self.ubint8)


class TestUBInt16:
    """Test of UBInt16 BasicType."""

    def setup_method(self):
        """Basic test setup."""
        self.ubint16 = basic_types.UBInt16()

    def test_get_size(self):
        """[Foundation/BasicTypes/UBInt16] - size 2."""
        assert self.ubint16.get_size() == 2


class TestUBInt32:
    """Test of UBInt32 BasicType."""

    def setup_method(self):
        """Basic test setup."""
        self.ubint32 = basic_types.UBInt32()

    def test_get_size(self):
        """[Foundation/BasicTypes/UBInt32] - size 4."""
        assert self.ubint32.get_size() == 4


class TestUBInt64:
    """Test of UBInt64 BasicType."""

    def setup_method(self):
        """Basic test setup."""
        self.ubint64 = basic_types.UBInt64()

    def test_get_size(self):
        """[Foundation/BasicTypes/UBInt64] - size 8."""
        assert self.ubint64.get_size() == 8


class TestUBInt128:
    """Test of UBInt128 BasicType."""

    def setup_method(self):
        """Basic test setup."""
        self.ubint128 = basic_types.UBInt128()

    def test_get_size(self):
        """[Foundation/BasicTypes/UBInt128] - size 16."""
        assert self.ubint128.get_size() == 16


class TestChar:
    """Test of Char BasicType."""

    def setup_method(self):
        """Basic test setup."""
        self.char1 = basic_types.Char('foo', length=3)
        self.char2 = basic_types.Char('foo', length=5)

    def test_get_size(self):
        """[Foundation/BasicTypes/Char] - get_size."""
        assert self.char1.get_size() == 3
        assert self.char2.get_size() == 5

    def test_pack(self):
        """[Foundation/BasicTypes/Char] - packing."""
        assert self.char1.pack() == b'fo\x00'
        assert self.char2.pack() == b'foo\x00\x00'

    def test_unpack(self):
        """[Foundation/BasicTypes/Char] - unpacking."""
        char1 = basic_types.Char(length=3)
        char2 = basic_types.Char(length=5)
        char1.unpack(b'fo\x00')
        char2.unpack(b'foo\x00\x00')

        assert char1.value == 'fo'
        assert char2.value == 'foo'


class TestHWAddress:
    """Test of HWAddress BasicType."""

    def test_unpack_packed(self):
        """Testing unpack of packed HWAddress."""
        mac = '0a:d3:98:a5:30:47'
        hw_addr = basic_types.HWAddress(mac)
        packed = hw_addr.pack()
        unpacked = basic_types.HWAddress()
        unpacked.unpack(packed)
        assert mac == unpacked.value

    def test_default_value(self):
        """Testing default_value for HWAddress."""
        mac = '00:00:00:00:00:00'
        hw_addr = basic_types.HWAddress()
        packed = hw_addr.pack()
        unpacked = basic_types.HWAddress()
        unpacked.unpack(packed)
        assert mac == unpacked.value


class TestIPAddress:
    """Test of IPAddress BasicType."""

    def test_unpack_packed(self):
        """Test unpacking of packed IPAddress."""
        ip_addr = basic_types.IPAddress('192.168.0.1')
        packed = ip_addr.pack()
        unpacked = basic_types.IPAddress()
        unpacked.unpack(packed)
        assert ip_addr.value == unpacked.value

    def test_unpack_packed_with_netmask(self):
        """Testing unpack of packed IPAddress with netmask."""
        ip_addr = basic_types.IPAddress('192.168.0.1/16')
        packed = ip_addr.pack()
        unpacked = basic_types.IPAddress()
        unpacked.unpack(packed)
        assert ip_addr.value == unpacked.value

    def test_netmask(self):
        """Testing get netmask from IPAddress."""
        ip_addr = basic_types.IPAddress('192.168.0.1/24')
        assert ip_addr.netmask == 24
        ip_addr = basic_types.IPAddress('192.168.0.1/16')
        assert ip_addr.netmask == 16
        ip_addr = basic_types.IPAddress('192.168.0.1')
        assert ip_addr.netmask == 32

    def test_max_prefix(self):
        """Testing get max_prefix from IPAddress."""
        ip_addr = basic_types.IPAddress()
        assert ip_addr.max_prefix == 32
        ip_addr = basic_types.IPAddress('192.168.0.35/16')
        assert ip_addr.max_prefix == 32

    def test_get_size(self):
        """Testing get_size from IPAddress."""
        ip_addr = basic_types.IPAddress('192.168.0.1/24')
        assert ip_addr.get_size() == 4


class TestBinaryData:
    """Test Binary data type."""

    def test_default_value(self):
        """Default packed value should be an empty byte."""
        expected = b''
        actual = BinaryData().pack()
        assert expected == actual

    def test_pack_none_value(self):
        """Test packing None value."""
        expected = b''
        actual = BinaryData(None).pack()
        assert expected == actual

    def test_pack_bytes_value(self):
        """Test packing some bytes."""
        expected = b'forty two'
        actual = BinaryData(expected).pack()
        assert expected == actual

    def test_pack_empty_bytes(self):
        """Test packing empty bytes."""
        expected = b''
        actual = BinaryData(expected).pack()
        assert expected == actual

    def test_pack_packable_value(self):
        """Test packing packable value."""
        hw_addr = basic_types.HWAddress('0a:d3:98:a5:30:47')
        expected = hw_addr.pack()
        actual = BinaryData(hw_addr).pack()
        assert expected == actual

    def test_unexpected_value_as_parameter(self):
        """Should raise ValueError if pack value is not bytes."""
        data = BinaryData('Some string')
        pytest.raises(ValueError, data.pack, "can't be a string")
