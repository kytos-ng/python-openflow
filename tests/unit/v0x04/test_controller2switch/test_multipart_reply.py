"""MultipartReply message test."""

from pyof.v0x04.controller2switch.common import MultipartType
from pyof.v0x04.controller2switch.multipart_reply import (
    Desc, MultipartReply, MultipartReplyFlags)
from tests.unit.v0x04.test_struct import StructTest


class TestMultipartReply(StructTest):
    """Test MultipartReply."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_message(MultipartReply, xid=16,
                            multipart_type=MultipartType.OFPMP_METER_CONFIG,
                            flags=MultipartReplyFlags.OFPMPF_REPLY_MORE,
                            body=b'')
        self.set_minimum_size(16)

    @staticmethod
    def get_attributes(multipart_type=MultipartType.OFPMP_DESC,
                       flags=MultipartReplyFlags.OFPMPF_REPLY_MORE,
                       body=b''):
        """Method used to return a dict with instance paramenters."""
        return {'xid': 32, 'multipart_type': multipart_type, 'flags': flags,
                'body': body}

    def test_pack_unpack_desc(self):
        """Testing multipart_type with OFPMP_DESC."""
        instances = Desc(mfr_desc="MANUFACTURER DESCRIPTION",
                         hw_desc="HARDWARE DESCRIPTION",
                         sw_desc="SOFTWARE DESCRIPTION",
                         serial_num="SERIAL NUMBER",
                         dp_desc="DATAPATH DESCRIPTION")
        options = TestMultipartReply.get_attributes(
            multipart_type=MultipartType.OFPMP_DESC, body=instances)
        self._test_pack_unpack(**options)
