"""Defines actions that may be associated with flows packets."""
# System imports
from enum import IntEnum
from math import ceil

# Local source tree imports
from pyof.foundation.base import GenericStruct
from pyof.foundation.basic_types import (
    BinaryData, FixedTypeList, Pad, UBInt8, UBInt16, UBInt32)
from pyof.v0x04.common.flow_match import OxmTLV

# Third-party imports

__all__ = ('ActionExperimenter', 'ActionGroup', 'ActionHeader',
           'ActionCopyTTLIn', 'ActionCopyTTLOut', 'ActionDecMPLSTTL',
           'ActionSetMPLSTTL', 'ActionDecNWTTL', 'ActionSetNWTTL',
           'ActionOutput', 'ActionPopMPLS', 'ActionPopPBB', 'ActionPopVLAN',
           'ActionPush', 'ActionSetField', 'ActionSetQueue', 'ActionType',
           'ControllerMaxLen', 'ListOfActions')

# Enums


class ActionType(IntEnum):
    """Actions associated with flows and packets."""

    #: Output to switch port.
    OFPAT_OUTPUT = 0
    #: Copy TTL "outwards" -- from next-to-outermost to outermost
    OFPAT_COPY_TTL_OUT = 11
    #: Copy TTL "inwards" -- from outermost to next-to-outermost
    OFPAT_COPY_TTL_IN = 12
    #: MPLS TTL
    OFPAT_SET_MPLS_TTL = 15
    #: Decrement MPLS TTL
    OFPAT_DEC_MPLS_TTL = 16
    #: Push a new VLAN tag
    OFPAT_PUSH_VLAN = 17
    #: Pop the outer VLAN tag
    OFPAT_POP_VLAN = 18
    #: Push a new MPLS tag
    OFPAT_PUSH_MPLS = 19
    #: Pop the outer MPLS tag
    OFPAT_POP_MPLS = 20
    #: Set queue id when outputting to a port
    OFPAT_SET_QUEUE = 21
    #: Apply group.
    OFPAT_GROUP = 22
    #: IP TTL.
    OFPAT_SET_NW_TTL = 23
    #: Decrement IP TTL.
    OFPAT_DEC_NW_TTL = 24
    #: Set a header field using OXM TLV format.
    OFPAT_SET_FIELD = 25
    #: Push a new PBB service tag (I-TAG)
    OFPAT_PUSH_PBB = 26
    #: Pop the outer PBB service tag (I-TAG)
    OFPAT_POP_PBB = 27
    #: Experimenter type
    OFPAT_EXPERIMENTER = 0xffff


class ControllerMaxLen(IntEnum):
    """A max_len of OFPCML_NO_BUFFER means not to buffer.

    The packet should be sent.
    """

    #: maximum max_len value which can be used to request a specific byte
    #:     length.
    OFPCML_MAX = 0xffe5
    #: indicates that no buffering should be applied and the whole packet is to
    #:     be sent to the controller.
    OFPCML_NO_BUFFER = 0xffff


# Classes


class ActionHeader(GenericStruct):
    """Action header that is common to all actions.

    The length includes the header and any padding used to make the action
    64-bit aligned.
    NB: The length of an action *must* always be a multiple of eight.
    """

    #: One of OFPAT_*.
    action_type = UBInt16(enum_ref=ActionType)
    #: Length of action, including this header. This is the length of actions,
    #:    including any padding to make it 64-bit aligned.
    length = UBInt16()
    # Pad for 64-bit alignment.
    # This should not be implemented, as each action type has its own padding.
    # pad = Pad(4)

    _allowed_types = ()

    def __init__(self, action_type=None, length=None):
        """Create an ActionHeader with the optional parameters below.

        Args:
            action_type (~pyof.v0x04.common.action.ActionType):
                The type of the action.
            length (int): Length of action, including this header.
        """
        super().__init__()
        self.action_type = action_type
        self.length = length

    def get_size(self, value=None):
        """Return the action length including the padding (multiple of 8)."""
        if isinstance(value, ActionHeader):
            return value.get_size()
        if value is None:
            current_size = super().get_size()
            return ceil(current_size / 8) * 8
        raise ValueError(f'Invalid value "{value}" for Action*.get_size()')

    def unpack(self, buff, offset=0):
        """Unpack a binary message into this object's attributes.

        Unpack the binary value *buff* and update this object attributes based
        on the results.

        Args:
            buff (bytes): Binary data package to be unpacked.
            offset (int): Where to begin unpacking.

        Raises:
            Exception: If there is a struct unpacking error.

        """
        self.action_type = UBInt16(enum_ref=ActionType)
        self.action_type.unpack(buff, offset)

        self.length = UBInt16()
        self.length.unpack(buff, offset=offset+2)

        for cls in ActionHeader.__subclasses__():
            if self.action_type.value in cls.get_allowed_types():
                if self.action_type.value == ActionType.OFPAT_EXPERIMENTER:
                    self.__class__ = cls.get_subclass(buff, offset+4)
                else:
                    self.__class__ = cls
                break

        super().unpack(buff[:offset+self.length], offset)

    @classmethod
    def get_allowed_types(cls):
        """Return allowed types for the class."""
        return cls._allowed_types


class ActionExperimenter(ActionHeader):
    """Action structure for OFPAT_EXPERIMENTER."""

    experimenter = UBInt32()

    _allowed_types = (ActionType.OFPAT_EXPERIMENTER,)
    _allowed_ids = ()

    def __init__(self, length=None, experimenter=None):
        """Create ActionExperimenterHeader with the optional parameters below.

        Args:
            experimenter (int): The experimenter field is the Experimenter ID,
                which takes the same form as in struct ofp_experimenter.
            body(bytes): The body of the experimenter. It is vendor-defined,
                so it is left as it is.
        """
        super().__init__(action_type=ActionType.OFPAT_EXPERIMENTER)
        self.length = length
        self.experimenter = experimenter

    @classmethod
    def get_allowed_ids(cls):
        """Return Experimenter IDs handled by te class."""
        return cls._allowed_ids

    @classmethod
    def default_subclass(cls):
        """Class used when no class handles the Experimenter ID."""
        return ActionExperimenterDefault

    @classmethod
    def get_subclass(cls, buff, offset):
        """Return the right subclass.

           Subclasses must implement this method and decide which of
           its subclasses is reponsible for this action.
        """
        experimenter = UBInt32()
        experimenter.unpack(buff, offset)
        for action_cls in cls.__subclasses__():
            if experimenter.value in action_cls.get_allowed_ids():
                return action_cls.get_subclass(buff, offset+4)
        return cls.default_subclass()


class ActionExperimenterDefault(ActionExperimenter):
    """Class for unknown Experimenter."""

    body = BinaryData()

    _allowed_ids = ()

    def __init__(self, length=None, experimenter=None, body=None):
        """Create ActionExperimenterHeader with the optional parameters below.

        Args:
            experimenter (int): The experimenter field is the Experimenter ID,
                which takes the same form as in struct ofp_experimenter.
            body(bytes): The body of the experimenter. It is vendor-defined,
                so it is left as it is.
        """

        super().__init__(length=length, experimenter=experimenter)
        self.body = body

    @classmethod
    def get_subclass(cls, buff, offset):
        return cls


class ActionGroup(ActionHeader):
    """Action structure for OFPAT_GROUP."""

    group_id = UBInt32()

    _allowed_types = (ActionType.OFPAT_GROUP,)

    def __init__(self, group_id=None):
        """Create an ActionGroup with the optional parameters below.

        Args:
            group_id (int): The group_id indicates the group used to process
                this packet. The set of buckets to apply depends on the group
                type.
        """
        super().__init__(action_type=ActionType.OFPAT_GROUP, length=8)
        self.group_id = group_id


class ActionDecMPLSTTL(ActionHeader):
    """Action structure for OFPAT_DEC_MPLS_TTL."""

    pad = Pad(4)

    _allowed_types = (ActionType.OFPAT_DEC_MPLS_TTL,)

    def __init__(self):
        """Create an ActionDecMPLSTTL."""
        super().__init__(action_type=ActionType.OFPAT_DEC_MPLS_TTL, length=8)


class ActionSetMPLSTTL(ActionHeader):
    """Action structure for OFPAT_SET_MPLS_TTL."""

    mpls_ttl = UBInt8()
    pad = Pad(3)

    _allowed_types = (ActionType.OFPAT_SET_MPLS_TTL,)

    def __init__(self, mpls_ttl=None):
        """Create an ActionSetMPLSTTL with the optional parameters below.

        Args:
            mpls_ttl (int): The mpls_ttl field is the MPLS TTL to set.
        """
        super().__init__(action_type=ActionType.OFPAT_SET_MPLS_TTL, length=8)
        self.mpls_ttl = mpls_ttl


class ActionCopyTTLIn(ActionHeader):
    """Action structure for OFPAT_COPY_TTL_IN."""

    pad = Pad(4)

    _allowed_types = (ActionType.OFPAT_COPY_TTL_IN,)

    def __init__(self):
        """Create an ActionCopyTTLIn."""
        super().__init__(action_type=ActionType.OFPAT_COPY_TTL_IN, length=8)


class ActionCopyTTLOut(ActionHeader):
    """Action structure for OFPAT_COPY_TTL_OUT."""

    pad = Pad(4)

    _allowed_types = (ActionType.OFPAT_COPY_TTL_OUT,)

    def __init__(self):
        """Create an ActionCopyTTLOut."""
        super().__init__(action_type=ActionType.OFPAT_COPY_TTL_OUT, length=8)


class ActionPopVLAN(ActionHeader):
    """Action structure for OFPAT_POP_VLAN."""

    pad = Pad(4)

    _allowed_types = (ActionType.OFPAT_POP_VLAN,)

    def __init__(self):
        """Create an ActionPopVLAN."""
        super().__init__(action_type=ActionType.OFPAT_POP_VLAN, length=8)


class ActionPopPBB(ActionHeader):
    """Action structure for OFPAT_POP_PBB."""

    pad = Pad(4)

    _allowed_types = (ActionType.OFPAT_POP_PBB,)

    def __init__(self):
        """Create an ActionPopPBB."""
        super().__init__(action_type=ActionType.OFPAT_POP_PBB, length=8)


class ActionDecNWTTL(ActionHeader):
    """Action structure for OFPAT_DEC_NW_TTL."""

    pad = Pad(4)

    _allowed_types = (ActionType.OFPAT_DEC_NW_TTL,)

    def __init__(self):
        """Create a ActionDecNWTTL."""
        super().__init__(action_type=ActionType.OFPAT_DEC_NW_TTL, length=8)


class ActionSetNWTTL(ActionHeader):
    """Action structure for OFPAT_SET_NW_TTL."""

    nw_ttl = UBInt8()
    pad = Pad(3)

    _allowed_types = (ActionType.OFPAT_SET_NW_TTL,)

    def __init__(self, nw_ttl=None):
        """Create an ActionSetNWTTL with the optional parameters below.

        Args:
            nw_ttl (int): the TTL address to set in the IP header.
        """
        super().__init__(action_type=ActionType.OFPAT_SET_NW_TTL, length=8)
        self.nw_ttl = nw_ttl


class ActionOutput(ActionHeader):
    """Defines the actions output.

    Action structure for :attr:`ActionType.OFPAT_OUTPUT`, which sends packets
    out :attr:`port`. When the :attr:`port` is the
    :attr:`.Port.OFPP_CONTROLLER`, :attr:`max_length` indicates the max number
    of bytes to send. A :attr:`max_length` of zero means no bytes of the packet
    should be sent.
    """

    port = UBInt32()
    max_length = UBInt16()
    pad = Pad(6)

    _allowed_types = (ActionType.OFPAT_OUTPUT,)

    def __init__(self, port=None,
                 max_length=ControllerMaxLen.OFPCML_NO_BUFFER):
        """Create a ActionOutput with the optional parameters below.

        Args:
            port (:class:`Port` or :class:`int`): Output port.
            max_length (int): Max length to send to controller.
        """
        super().__init__(action_type=ActionType.OFPAT_OUTPUT, length=16)
        self.port = port
        self.max_length = max_length

    def __repr__(self):
        return f"{type(self).__name__}(port={self.port})"


class ActionPopMPLS(ActionHeader):
    """Action structure for OFPAT_POP_MPLS."""

    ethertype = UBInt16()
    pad = Pad(2)

    _allowed_types = (ActionType.OFPAT_POP_MPLS,)

    def __init__(self, ethertype=None):
        """Create an ActionPopMPLS with the optional parameters below.

        Args:
            ethertype (int): indicates the Ethertype of the payload.
        """
        super().__init__(action_type=ActionType.OFPAT_POP_MPLS)
        self.ethertype = ethertype


class ActionPush(ActionHeader):
    """Action structure for OFPAT_PUSH_[VLAN/MPLS/PBB]."""

    ethertype = UBInt16()
    pad = Pad(2)

    _allowed_types = (ActionType.OFPAT_PUSH_VLAN, ActionType.OFPAT_PUSH_MPLS,
                      ActionType.OFPAT_PUSH_PBB)

    def __init__(self, action_type=None, ethertype=None):
        """Create a ActionPush with the optional parameters below.

        Args:
            action_type (:class:`ActionType`): indicates which tag will be
                pushed (VLAN, MPLS, PBB).
            ethertype (int): indicates the Ethertype of the new tag.
        """
        super().__init__(action_type, length=8)
        self.ethertype = ethertype


class ActionSetField(ActionHeader):
    """Action structure for OFPAT_SET_FIELD."""

    field = OxmTLV()

    _allowed_types = (ActionType.OFPAT_SET_FIELD,)

    def __init__(self, field=None):
        """Create a ActionSetField with the optional parameters below.

        Args:
            length (int): length padded to 64 bits, followed by exactly
                          oxm_len bytes containing a single OXM TLV, then
                          exactly ((oxm_len + 4) + 7)/8*8 - (oxm_len + 4)
                          (between 0 and 7) bytes of all-zero bytes
            field (:class:`OxmTLV`): OXM field and value.
        """
        super().__init__(action_type=ActionType.OFPAT_SET_FIELD)
        self.field = OxmTLV() if field is None else field

    def __repr__(self):
        return (f"{type(self).__name__}({self.field.oxm_field!s}, "
                f"{self.field.oxm_value})")

    def pack(self, value=None):
        """Pack this structure updating the length and padding it."""
        self._update_length()
        packet = super().pack()
        return self._complete_last_byte(packet)

    def _update_length(self):
        """Update the length field of the struct."""
        action_length = 4 + len(self.field.pack())
        overflow = action_length % 8
        self.length = action_length
        if overflow:
            self.length = action_length + 8 - overflow

    def _complete_last_byte(self, packet):
        """Pad until the packet length is a multiple of 8 (bytes)."""
        padded_size = self.length
        padding_bytes = padded_size - len(packet)
        if padding_bytes > 0:
            packet += Pad(padding_bytes).pack()
        return packet


class ActionSetQueue(ActionHeader):
    """Action structure for OFPAT_SET_QUEUE."""

    queue_id = UBInt32()

    _allowed_types = (ActionType.OFPAT_SET_QUEUE,)

    def __init__(self, queue_id=None):
        """Create an ActionSetQueue with the optional parameters below.

        Args:
            queue_id (int): The queue_id send packets to given queue on port.
        """
        super().__init__(action_type=ActionType.OFPAT_SET_QUEUE, length=8)
        self.queue_id = queue_id


class ListOfActions(FixedTypeList):
    """List of actions.

    Represented by instances of ActionHeader and used on ActionHeader objects.
    """

    def __init__(self, items=None):
        """Create a ListOfActions with the optional parameters below.

        Args:
            items (~pyof.v0x04.common.action.ActionHeader):
                Instance or a list of instances.
        """
        super().__init__(pyof_class=ActionHeader, items=items)
