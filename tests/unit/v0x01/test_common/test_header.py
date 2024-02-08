"""Testing Header structure."""
import os
from unittest.mock import patch

import pytest

from pyof.v0x01.common.header import Header, Type


class TestHeader:
    """Test the message Header."""

    def setup_method(self):
        """Setup the TestHeader Class instantiating a HELLO header."""
        self.message = Header()
        self.message.message_type = Type.OFPT_HELLO
        self.message.xid = 1
        self.message.length = 0

    def test_size(self):
        """[Common/Header] - size 8."""
        assert self.message.get_size() == 8

    @pytest.mark.xfail
    def test_pack_empty(self):
        """[Common/Header] - packing empty header."""
        pytest.raises(TypeError,
                          Header().pack())

    def test_pack(self):
        """[Common/Header] - packing Hello."""
        packed_header = b'\x01\x00\x00\x00\x00\x00\x00\x01'
        assert self.message.pack() == packed_header

    def test_unpack(self):
        """[Common/Header] - unpacking Hello."""
        filename = os.path.join(os.path.dirname(os.path.realpath('__file__')),
                                'raw/v0x01/ofpt_hello.dat')
        f = open(filename, 'rb')
        self.message.unpack(f.read(8))

        assert self.message.length == 8
        assert self.message.xid == 1
        assert self.message.message_type == Type.OFPT_HELLO
        assert self.message.version == 1

        f.close()
