"""PortMod tests."""
import unittest

from pyof.v0x04.controller2switch.port_mod import PortMod


class TestPortMod:
    """PortMod test."""

    def test_min_size(self):
        """Test minimum message size."""
        assert 40 == PortMod().get_size()
