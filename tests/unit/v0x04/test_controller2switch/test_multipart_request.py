"""MultipartRequest message test."""
from pyof.v0x04.controller2switch.multipart_request import (
    MultipartRequest, MultipartRequestFlags, MultipartType, PortStatsRequest,
    TableFeatures)
from tests.unit.v0x04.test_struct import StructTest


class TestMultipartRequest(StructTest):
    """Test the MultipartRequest message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_message(MultipartRequest, xid=16,
                            multipart_type=MultipartType.OFPMP_TABLE_FEATURES,
                            flags=MultipartRequestFlags.OFPMPF_REQ_MORE,
                            body=b'')
        self.set_minimum_size(16)

    @staticmethod
    def get_attributes(multipart_type=MultipartType.OFPMP_DESC,
                       flags=MultipartRequestFlags.OFPMPF_REQ_MORE,
                       body=b''):
        """Method used to return a dict with instance paramenters."""
        return {'xid': 32, 'multipart_type': multipart_type, 'flags': flags,
                'body': body}

    def test_pack_unpack_desc(self):
        """Testing multipart_type with OFPMP_DESC."""
        options = TestMultipartRequest.get_attributes(
            multipart_type=MultipartType.OFPMP_DESC)
        self._test_pack_unpack(**options)

    def test_pack_unpack_table(self):
        """Testing multipart_type with OFPMP_TABLE."""
        options = TestMultipartRequest.get_attributes(
            multipart_type=MultipartType.OFPMP_TABLE)
        self._test_pack_unpack(**options)

    def test_pack_unpack__port_stats_request(self):
        """Testing multipart_type with OFPMP_PORT_STATS."""
        options = TestMultipartRequest.get_attributes(
            multipart_type=MultipartType.OFPMP_PORT_STATS,
            body=PortStatsRequest(port_no=33))
        self._test_pack_unpack(**options)

    def test_pack_unpack_port_desc(self):
        """Testing multipart_type with OFPMP_PORT_DESC."""
        options = TestMultipartRequest.get_attributes(
            multipart_type=MultipartType.OFPMP_PORT_DESC)
        self._test_pack_unpack(**options)

    def test_pack_unpack_table_features(self):
        """Testing multipart_type with OFPMP_TABLE_FEATURES."""
        instance = [TableFeatures(table_id=2),
                    TableFeatures(table_id=6),
                    TableFeatures(table_id=4)]
        options = TestMultipartRequest.get_attributes(
            multipart_type=MultipartType.OFPMP_TABLE_FEATURES,
            body=instance)
        self._test_pack_unpack(**options)
