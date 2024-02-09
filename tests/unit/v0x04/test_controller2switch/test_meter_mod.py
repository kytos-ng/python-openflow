"""MeterMod tests."""
from pyof.v0x04.controller2switch.meter_mod import (
    MeterBandDrop, MeterBandDscpRemark, MeterBandExperimenter, MeterBandHeader,
    MeterMod)


class TestMeterMod:
    """MeterMod test."""

    def test_min_size(self):
        """Test minimum message size."""
        assert 16 == MeterMod().get_size()


class TestMeterBandHeader:
    """MeterBandHeader test."""

    def test_min_size(self):
        """Test minimum message size."""
        assert 12 == MeterBandHeader().get_size()


class TestMeterBandDrop:
    """MeterBandDrop test."""

    def test_min_size(self):
        """Test minimum message size."""
        assert 16 == MeterBandDrop().get_size()


class TestMeterBandDscpRemark:
    """MeterBandDscpRemark test."""

    def test_min_size(self):
        """Test minimum message size."""
        assert 16 == MeterBandDscpRemark().get_size()


class TestMeterBandExperimenter:
    """MeterBandExperimenter test."""

    def test_min_size(self):
        """Test minimum message size."""
        assert 16 == MeterBandExperimenter().get_size()
