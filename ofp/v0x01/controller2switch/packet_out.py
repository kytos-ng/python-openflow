"""When the controller wishes to send a packet out through the datapath, it
uses the OFPT_PACKET_OUT message"""

# System imports

# Third-party imports

# Local source tree imports
from ..common import header as of_header
from ..foundation import base
from ..foundation import basic_types


class PacketOut(base.GenericStruct):
    """
    Send packet (controller -> datapath)

        :param header -- OpenFlow header
        :param buffer_id -- ID assigned by datapath (-1 if none)
        :param in_port -- Packet’s input port (OFPP_NONE if none)
        :param actions_len -- Size of action array in bytes
        :param data -- Packet data. The length is inferred from the length
                       field in the header. (Only meaningful if
                       buffer_id == -1.)
    """
    header = of_header.OFPHeader()
    buffer_id = basic_types.UBInt32()
    in_port = basic_types.UBInt16()
    actions_len = basic_types.UBInt16()
    data = basic_types.UBInt8Array(length=0)

    def __init__(self, header=None, buffer_id=None, in_port=None,
                 actions_len=None, data=None):

        self.header = header
        self.buffer_id = buffer_id
        self.in_port = in_port
        self.actions_len = actions_len
        self.data = data
