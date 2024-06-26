"""Testing Error Message."""
from pyof.v0x01.asynchronous.error_msg import (
    BadRequestCode, ErrorMsg, ErrorType, FlowModFailedCode)
from tests.unit.test_struct import StructTest


class TestErrorMessage(StructTest):
    """Test the Error Message."""

    def setup_method(self):
        """Setup StructTest."""
        self.set_raw_dump_file('v0x01', 'ofpt_error_msg')
        self.set_raw_dump_object(ErrorMsg, xid=12,
                                    error_type=ErrorType.OFPET_BAD_REQUEST,
                                    code=BadRequestCode.OFPBRC_BAD_STAT,
                                    data=b'')
        self.set_minimum_size(12)

    def test_unpack_error_msg(self):
        """Test Unpack a sample ErrorMsg."""
        expected = b'\x01\x01\x00\x1b\x00\x00\x00\x18\x00\x03\x00\x02FLOW'

        error_msg = ErrorMsg(xid=24,
                             error_type=ErrorType.OFPET_FLOW_MOD_FAILED,
                             code=FlowModFailedCode.OFPFMFC_EPERM,
                             data=b'FLOW')

        actual = ErrorMsg(xid=24)
        actual.unpack(expected[8:])

        assert actual == error_msg
