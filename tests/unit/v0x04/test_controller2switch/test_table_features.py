"""TableFeatures message tests."""

from pyof.v0x04.common.action import ActionExperimenter, ActionHeader, ActionType
from pyof.v0x04.common.flow_instructions import Instruction, InstructionType
from pyof.v0x04.common.flow_match import OxmOfbMatchField, OxmTLV
from pyof.v0x04.controller2switch.common import (
    ActionsProperty,
    InstructionsProperty,
    NextTablesProperty,
    OxmProperty,
    TableFeaturePropType,
    TableFeatures,
)
from tests.unit.test_struct import StructTest as PyofStructTest


class StructTest(PyofStructTest):
    """Wrapper class to temporary skip unpack tests."""

    def test_raw_dump_file(self):
        """Overwrite test_raw_dump_file to skip unpack test."""
        file_bytes = self.get_raw_dump().read()
        pyof_obj = self.get_raw_object()
        self._test_pack(pyof_obj, file_bytes)
        # self._test_unpack(pyof_obj, file_bytes)


class TestTableFeatures(StructTest):
    """Test the TableFeatures message."""

    def setup_method(self):
        """Configure raw file and its object in parent class (TestDump)."""
        attrs = self._prepare_table_features()
        self.set_raw_dump_file("v0x04", "ofp_table_features")
        self.set_raw_dump_object(TableFeatures, **attrs)
        self.set_minimum_size(64)

    # pylint: disable=too-many-locals
    def _prepare_table_features(self):
        tb_props = []

        #################################################
        ## Table Features Properties - Instructions
        #################################################
        insts = [
            InstructionType.OFPIT_GOTO_TABLE,
            InstructionType.OFPIT_WRITE_METADATA,
            InstructionType.OFPIT_WRITE_ACTIONS,
            InstructionType.OFPIT_APPLY_ACTIONS,
            InstructionType.OFPIT_CLEAR_ACTIONS,
            InstructionType.OFPIT_METER,
        ]
        inst_ids = []
        for inst in insts:
            inst_ids.append(Instruction(instruction_type=inst))
        inst_prop_types = [
            TableFeaturePropType.OFPTFPT_INSTRUCTIONS,
            TableFeaturePropType.OFPTFPT_INSTRUCTIONS_MISS,
        ]
        for inst_prop_type in inst_prop_types:
            tb_props.append(
                InstructionsProperty(
                    property_type=inst_prop_type, instruction_ids=inst_ids
                )
            )

        #################################################
        ## Table Features Properties - NextTable
        #################################################
        next_tb_prop_types = [
            TableFeaturePropType.OFPTFPT_NEXT_TABLES,
            TableFeaturePropType.OFPTFPT_NEXT_TABLES_MISS,
        ]
        for next_tb_prop_type in next_tb_prop_types:
            tb_props.append(
                NextTablesProperty(
                    property_type=next_tb_prop_type,
                    next_table_ids=[1, 2, 3, 4, 5, 6, 7],
                )
            )

        #################################################
        ## Table Features Properties - Actions
        #################################################
        actions = [
            ActionType.OFPAT_OUTPUT,
            ActionType.OFPAT_COPY_TTL_OUT,
            ActionType.OFPAT_COPY_TTL_IN,
            ActionType.OFPAT_SET_MPLS_TTL,
            ActionType.OFPAT_DEC_MPLS_TTL,
            ActionType.OFPAT_PUSH_VLAN,
            ActionType.OFPAT_POP_VLAN,
            ActionType.OFPAT_PUSH_MPLS,
            ActionType.OFPAT_POP_MPLS,
            ActionType.OFPAT_SET_QUEUE,
            ActionType.OFPAT_GROUP,
            ActionType.OFPAT_SET_NW_TTL,
            ActionType.OFPAT_DEC_NW_TTL,
            ActionType.OFPAT_SET_FIELD,
            ActionType.OFPAT_PUSH_PBB,
            ActionType.OFPAT_POP_PBB,
        ]
        action_ids = []
        for action in actions:
            action_ids.append(ActionHeader(action_type=action, length=4))
        action_ids.append(ActionExperimenter(length=8, experimenter=0xFF000002))
        action_prop_types = [
            TableFeaturePropType.OFPTFPT_WRITE_ACTIONS,
            TableFeaturePropType.OFPTFPT_WRITE_ACTIONS_MISS,
            TableFeaturePropType.OFPTFPT_APPLY_ACTIONS,
            TableFeaturePropType.OFPTFPT_APPLY_ACTIONS_MISS,
        ]
        for action_prop_type in action_prop_types:
            tb_props.append(
                ActionsProperty(property_type=action_prop_type, action_ids=action_ids)
            )

        #################################################
        ## Table Features Properties - OXM
        #################################################
        oxms = [
            OxmOfbMatchField.OFPXMT_OFB_IN_PORT,
            OxmOfbMatchField.OFPXMT_OFB_ETH_DST,
            OxmOfbMatchField.OFPXMT_OFB_ETH_SRC,
            OxmOfbMatchField.OFPXMT_OFB_ETH_TYPE,
            OxmOfbMatchField.OFPXMT_OFB_VLAN_VID,
            OxmOfbMatchField.OFPXMT_OFB_VLAN_PCP,
            OxmOfbMatchField.OFPXMT_OFB_IP_PROTO,
            OxmOfbMatchField.OFPXMT_OFB_IPV4_SRC,
            OxmOfbMatchField.OFPXMT_OFB_IPV4_DST,
            OxmOfbMatchField.OFPXMT_OFB_TCP_SRC,
            OxmOfbMatchField.OFPXMT_OFB_TCP_DST,
            OxmOfbMatchField.OFPXMT_OFB_UDP_SRC,
            OxmOfbMatchField.OFPXMT_OFB_UDP_DST,
            OxmOfbMatchField.OFPXMT_OFB_SCTP_SRC,
            OxmOfbMatchField.OFPXMT_OFB_SCTP_DST,
        ]
        # pylint: disable=fixme
        # XXX: some of the hasmask below are actually wrong according to the OF
        # spec, but it was left that way to match actual packet capture
        match_fields_size_mask = {
            OxmOfbMatchField.OFPXMT_OFB_IN_PORT.value: (4, False),
            OxmOfbMatchField.OFPXMT_OFB_ETH_TYPE.value: (2, False),
            OxmOfbMatchField.OFPXMT_OFB_IP_PROTO.value: (1, False),
            OxmOfbMatchField.OFPXMT_OFB_VLAN_VID.value: (2, True),
            OxmOfbMatchField.OFPXMT_OFB_VLAN_PCP.value: (1, True),
            OxmOfbMatchField.OFPXMT_OFB_ETH_SRC.value: (6, True),
            OxmOfbMatchField.OFPXMT_OFB_ETH_DST.value: (6, True),
            OxmOfbMatchField.OFPXMT_OFB_IPV4_SRC.value: (4, True),
            OxmOfbMatchField.OFPXMT_OFB_IPV4_DST.value: (4, True),
            OxmOfbMatchField.OFPXMT_OFB_IP_DSCP.value: (1, True),
            OxmOfbMatchField.OFPXMT_OFB_TCP_SRC.value: (2, True),
            OxmOfbMatchField.OFPXMT_OFB_TCP_DST.value: (2, True),
            OxmOfbMatchField.OFPXMT_OFB_UDP_SRC.value: (2, True),
            OxmOfbMatchField.OFPXMT_OFB_UDP_DST.value: (2, True),
            OxmOfbMatchField.OFPXMT_OFB_ICMPV4_TYPE.value: (1, True),
            OxmOfbMatchField.OFPXMT_OFB_IPV6_SRC.value: (16, True),
            OxmOfbMatchField.OFPXMT_OFB_IPV6_DST.value: (16, True),
            OxmOfbMatchField.OFPXMT_OFB_ICMPV6_TYPE.value: (1, True),
            OxmOfbMatchField.OFPXMT_OFB_SCTP_SRC.value: (2, True),
            OxmOfbMatchField.OFPXMT_OFB_SCTP_DST.value: (2, True),
        }
        oxm_ids = []
        for oxm in oxms:
            s, m = match_fields_size_mask[oxm.value]
            oxm_ids.append(OxmTLV(oxm_field=oxm, oxm_hasmask=m, oxm_length=s))
        tb_props.append(
            OxmProperty(
                property_type=TableFeaturePropType.OFPTFPT_MATCH, oxm_ids=oxm_ids
            )
        )
        oxm_ids = []
        for oxm in oxms:
            s, m = match_fields_size_mask[oxm.value]
            oxm_ids.append(OxmTLV(oxm_field=oxm, oxm_hasmask=False, oxm_length=s))
        tb_props.append(
            OxmProperty(
                property_type=TableFeaturePropType.OFPTFPT_WILDCARDS, oxm_ids=oxm_ids
            )
        )
        #################################################
        ## Table Features Properties - SETFIELD OXM
        #################################################
        setfield_oxms = [
            OxmOfbMatchField.OFPXMT_OFB_ETH_DST,
            OxmOfbMatchField.OFPXMT_OFB_ETH_SRC,
            OxmOfbMatchField.OFPXMT_OFB_ETH_TYPE,
            OxmOfbMatchField.OFPXMT_OFB_VLAN_VID,
            OxmOfbMatchField.OFPXMT_OFB_VLAN_PCP,
            OxmOfbMatchField.OFPXMT_OFB_IP_DSCP,
            OxmOfbMatchField.OFPXMT_OFB_IP_ECN,
            OxmOfbMatchField.OFPXMT_OFB_IP_PROTO,
            OxmOfbMatchField.OFPXMT_OFB_IPV4_SRC,
            OxmOfbMatchField.OFPXMT_OFB_IPV4_DST,
            OxmOfbMatchField.OFPXMT_OFB_TCP_SRC,
            OxmOfbMatchField.OFPXMT_OFB_TCP_DST,
            OxmOfbMatchField.OFPXMT_OFB_UDP_SRC,
            OxmOfbMatchField.OFPXMT_OFB_UDP_DST,
            OxmOfbMatchField.OFPXMT_OFB_SCTP_SRC,
            OxmOfbMatchField.OFPXMT_OFB_SCTP_DST,
            OxmOfbMatchField.OFPXMT_OFB_ICMPV4_TYPE,
            OxmOfbMatchField.OFPXMT_OFB_ICMPV4_CODE,
            OxmOfbMatchField.OFPXMT_OFB_ARP_OP,
            OxmOfbMatchField.OFPXMT_OFB_ARP_SPA,
            OxmOfbMatchField.OFPXMT_OFB_ARP_TPA,
            OxmOfbMatchField.OFPXMT_OFB_ARP_SHA,
            OxmOfbMatchField.OFPXMT_OFB_ARP_THA,
            OxmOfbMatchField.OFPXMT_OFB_IPV6_SRC,
            OxmOfbMatchField.OFPXMT_OFB_IPV6_DST,
            OxmOfbMatchField.OFPXMT_OFB_IPV6_FLABEL,
            OxmOfbMatchField.OFPXMT_OFB_ICMPV6_TYPE,
            OxmOfbMatchField.OFPXMT_OFB_ICMPV6_CODE,
            OxmOfbMatchField.OFPXMT_OFB_IPV6_ND_TARGET,
            OxmOfbMatchField.OFPXMT_OFB_IPV6_ND_SLL,
            OxmOfbMatchField.OFPXMT_OFB_IPV6_ND_TLL,
            OxmOfbMatchField.OFPXMT_OFB_MPLS_LABEL,
            OxmOfbMatchField.OFPXMT_OFB_MPLS_TC,
            OxmOfbMatchField.OFPXMT_OFP_MPLS_BOS,
            OxmOfbMatchField.OFPXMT_OFB_PBB_ISID,
            OxmOfbMatchField.OFPXMT_OFB_TUNNEL_ID,
            OxmOfbMatchField.OFPXMT_OFB_PBB_UCA,
        ]
        setfield_oxm_prop_types = [
            TableFeaturePropType.OFPTFPT_WRITE_SETFIELD,
            TableFeaturePropType.OFPTFPT_WRITE_SETFIELD_MISS,
            TableFeaturePropType.OFPTFPT_APPLY_SETFIELD,
            TableFeaturePropType.OFPTFPT_APPLY_SETFIELD_MISS,
        ]
        oxm_ids = []
        for oxm in setfield_oxms:
            oxm_ids.append(OxmTLV(oxm_field=oxm, oxm_hasmask=False, oxm_length=0))
        for oxm_prop_type in setfield_oxm_prop_types:
            tb_oxm_ids = oxm_ids
            tb_props.append(
                OxmProperty(property_type=oxm_prop_type, oxm_ids=tb_oxm_ids)
            )

        return {
            "table_id": 0,
            "name": "novi_table_0",
            "metadata_match": 0x00000000FFFFFFFF,
            "metadata_write": 0x00000000FFFFFFFF,
            "config": 0,
            "max_entries": 1023,
            "properties": tb_props,
        }
