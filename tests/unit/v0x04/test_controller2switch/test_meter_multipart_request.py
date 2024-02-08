"""MultipartRequest message test."""
from pyof.v0x04.controller2switch.multipart_request import (
    MeterMultipartRequest, MultipartRequest, MultipartType)
from tests.unit.test_struct import StructTest


class TestMeterMultipartRequest(StructTest):
    """Test the MultipartRequest message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        mp_type = MultipartType.OFPMP_METER
        self.set_raw_dump_file('v0x04', 'ofpt_meter_multipart_request')
        self.set_raw_dump_object(MultipartRequest, xid=1,
                                    multipart_type=mp_type,
                                    flags=0, body=_get_body())
        self.set_minimum_size(16)


def _get_body():
    """Return the body used by MultipartRequest message."""
    return MeterMultipartRequest()
