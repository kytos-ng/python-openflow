"""Testing Port structures."""
from pyof.v0x01.common.action import (
    ActionDLAddr, ActionEnqueue, ActionNWAddr, ActionNWTos, ActionOutput,
    ActionTPPort, ActionType, ActionVendorHeader, ActionVlanPCP, ActionVlanVid)
from pyof.v0x01.common.phy_port import Port
from tests.unit.test_struct import StructTest


class TestActionOutput(StructTest):
    """ActionOutput message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_action_output')
        self.set_raw_dump_object(ActionOutput, port=Port.OFPP_CONTROLLER,
                                    max_length=8)
        self.set_minimum_size(8)


class TestActionEnqueue(StructTest):
    """ActionEnqueue message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_action_enqueue')
        self.set_raw_dump_object(ActionEnqueue, port=Port.OFPP_CONTROLLER,
                                    queue_id=4)
        self.set_minimum_size(16)


class TestActionVlanVid(StructTest):
    """ActionVlanVid message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_action_vlan_vid')
        self.set_raw_dump_object(ActionVlanVid, vlan_id=5)
        self.set_minimum_size(8)


class TestActionVlanPCP(StructTest):
    """ActionVlanPCP message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_action_vlan_pcp')
        self.set_raw_dump_object(ActionVlanPCP, vlan_pcp=2)
        self.set_minimum_size(8)


class TestActionDLAddr(StructTest):
    """ActionDLAddr message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_action_dl_addr')
        self.set_raw_dump_object(ActionDLAddr,
                                    action_type=ActionType.OFPAT_SET_DL_SRC,
                                    dl_addr=[12, 12, 12, 12, 12, 12])
        self.set_minimum_size(16)


class TestActionNWAddr(StructTest):
    """ActionNWAddr message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_action_nw_addr')
        self.set_raw_dump_object(ActionNWAddr,
                                    action_type=ActionType.OFPAT_SET_NW_SRC,
                                    nw_addr=[12, 12, 12, 12, 12, 12])
        self.set_minimum_size(8)


class TestActionNWTos(StructTest):
    """ActionNWTos message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_action_nw_tos')
        self.set_raw_dump_object(ActionNWTos,
                                    action_type=ActionType.OFPAT_SET_NW_SRC,
                                    nw_tos=123456)
        self.set_minimum_size(8)


class TestActionTPPort(StructTest):
    """ActionTPPort message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_action_tp_port')
        self.set_raw_dump_object(ActionTPPort,
                                    action_type=ActionType.OFPAT_SET_TP_SRC,
                                    tp_port=8888)
        self.set_minimum_size(8)


class TestActionVendorHeader(StructTest):
    """ActionVendorHeader message tests (also those in :class:`.TestDump`)."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        self.set_raw_dump_file('v0x01', 'ofpt_action_vendor_header')
        self.set_raw_dump_object(ActionVendorHeader, length=16, vendor=1)
        self.set_minimum_size(8)
