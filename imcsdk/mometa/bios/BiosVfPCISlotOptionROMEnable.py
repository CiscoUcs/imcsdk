"""This module contains the general information for BiosVfPCISlotOptionROMEnable ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPCISlotOptionROMEnableConsts:
    VP_SLOT10_LINK_SPEED_AUTO = "Auto"
    VP_SLOT10_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT10_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT10_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT10_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT10_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT10_STATE_DISABLED = "Disabled"
    VP_SLOT10_STATE_ENABLED = "Enabled"
    VP_SLOT10_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT10_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT10_STATE_DISABLED = "disabled"
    _VP_SLOT10_STATE_ENABLED = "enabled"
    VP_SLOT10_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT1_LINK_SPEED_AUTO = "Auto"
    VP_SLOT1_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT1_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT1_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT1_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT1_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT1_STATE_DISABLED = "Disabled"
    VP_SLOT1_STATE_ENABLED = "Enabled"
    VP_SLOT1_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT1_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT1_STATE_DISABLED = "disabled"
    _VP_SLOT1_STATE_ENABLED = "enabled"
    VP_SLOT1_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT2_LINK_SPEED_AUTO = "Auto"
    VP_SLOT2_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT2_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT2_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT2_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT2_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT2_STATE_DISABLED = "Disabled"
    VP_SLOT2_STATE_ENABLED = "Enabled"
    VP_SLOT2_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT2_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT2_STATE_DISABLED = "disabled"
    _VP_SLOT2_STATE_ENABLED = "enabled"
    VP_SLOT2_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT3_LINK_SPEED_AUTO = "Auto"
    VP_SLOT3_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT3_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT3_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT3_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT3_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT3_STATE_DISABLED = "Disabled"
    VP_SLOT3_STATE_ENABLED = "Enabled"
    VP_SLOT3_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT3_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT3_STATE_DISABLED = "disabled"
    _VP_SLOT3_STATE_ENABLED = "enabled"
    VP_SLOT3_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT4_LINK_SPEED_AUTO = "Auto"
    VP_SLOT4_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT4_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT4_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT4_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT4_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT4_STATE_DISABLED = "Disabled"
    VP_SLOT4_STATE_ENABLED = "Enabled"
    VP_SLOT4_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT4_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT4_STATE_DISABLED = "disabled"
    _VP_SLOT4_STATE_ENABLED = "enabled"
    VP_SLOT4_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT5_LINK_SPEED_AUTO = "Auto"
    VP_SLOT5_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT5_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT5_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT5_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT5_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT5_STATE_DISABLED = "Disabled"
    VP_SLOT5_STATE_ENABLED = "Enabled"
    VP_SLOT5_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT5_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT5_STATE_DISABLED = "disabled"
    _VP_SLOT5_STATE_ENABLED = "enabled"
    VP_SLOT5_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT6_LINK_SPEED_AUTO = "Auto"
    VP_SLOT6_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT6_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT6_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT6_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT6_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT6_STATE_DISABLED = "Disabled"
    VP_SLOT6_STATE_ENABLED = "Enabled"
    VP_SLOT6_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT6_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT6_STATE_DISABLED = "disabled"
    _VP_SLOT6_STATE_ENABLED = "enabled"
    VP_SLOT6_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT7_LINK_SPEED_AUTO = "Auto"
    VP_SLOT7_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT7_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT7_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT7_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT7_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT7_STATE_DISABLED = "Disabled"
    VP_SLOT7_STATE_ENABLED = "Enabled"
    VP_SLOT7_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT7_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT7_STATE_DISABLED = "disabled"
    _VP_SLOT7_STATE_ENABLED = "enabled"
    VP_SLOT7_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT8_LINK_SPEED_AUTO = "Auto"
    VP_SLOT8_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT8_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT8_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT8_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT8_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT8_STATE_DISABLED = "Disabled"
    VP_SLOT8_STATE_ENABLED = "Enabled"
    VP_SLOT8_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT8_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT8_STATE_DISABLED = "disabled"
    _VP_SLOT8_STATE_ENABLED = "enabled"
    VP_SLOT8_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT9_LINK_SPEED_AUTO = "Auto"
    VP_SLOT9_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT9_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT9_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT9_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT9_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT9_STATE_DISABLED = "Disabled"
    VP_SLOT9_STATE_ENABLED = "Enabled"
    VP_SLOT9_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT9_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT9_STATE_DISABLED = "disabled"
    _VP_SLOT9_STATE_ENABLED = "enabled"
    VP_SLOT9_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_FLOMLINK_SPEED_AUTO = "Auto"
    VP_SLOT_FLOMLINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_FLOMLINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_FLOMLINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_FLOMLINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_FLOMLINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_FRONT_SLOT5_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_FRONT_SLOT5_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_FRONT_SLOT5_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_FRONT_SLOT5_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_FRONT_SLOT5_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_FRONT_SLOT5_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_FRONT_SLOT6_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_FRONT_SLOT6_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_FRONT_SLOT6_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_FRONT_SLOT6_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_FRONT_SLOT6_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_FRONT_SLOT6_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_HBALINK_SPEED_AUTO = "Auto"
    VP_SLOT_HBALINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_HBALINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_HBALINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_HBALINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_HBALINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_HBASTATE_DISABLED = "Disabled"
    VP_SLOT_HBASTATE_ENABLED = "Enabled"
    VP_SLOT_HBASTATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_HBASTATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT_HBASTATE_DISABLED = "disabled"
    _VP_SLOT_HBASTATE_ENABLED = "enabled"
    VP_SLOT_HBASTATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_MLOMLINK_SPEED_AUTO = "Auto"
    VP_SLOT_MLOMLINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_MLOMLINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_MLOMLINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_MLOMLINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_MLOMLINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_MLOMSTATE_DISABLED = "Disabled"
    VP_SLOT_MLOMSTATE_ENABLED = "Enabled"
    VP_SLOT_MLOMSTATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_MLOMSTATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT_MLOMSTATE_DISABLED = "disabled"
    _VP_SLOT_MLOMSTATE_ENABLED = "enabled"
    VP_SLOT_MLOMSTATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_MEZZ_STATE_DISABLED = "Disabled"
    VP_SLOT_MEZZ_STATE_ENABLED = "Enabled"
    VP_SLOT_MEZZ_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_MEZZ_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT_MEZZ_STATE_DISABLED = "disabled"
    _VP_SLOT_MEZZ_STATE_ENABLED = "enabled"
    VP_SLOT_MEZZ_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_N1_STATE_DISABLED = "Disabled"
    VP_SLOT_N1_STATE_ENABLED = "Enabled"
    VP_SLOT_N1_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_N1_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT_N1_STATE_DISABLED = "disabled"
    _VP_SLOT_N1_STATE_ENABLED = "enabled"
    VP_SLOT_N1_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_N2_STATE_DISABLED = "Disabled"
    VP_SLOT_N2_STATE_ENABLED = "Enabled"
    VP_SLOT_N2_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_N2_STATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT_N2_STATE_DISABLED = "disabled"
    _VP_SLOT_N2_STATE_ENABLED = "enabled"
    VP_SLOT_N2_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_RISER1_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_RISER1_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_RISER1_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_RISER1_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_RISER1_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_RISER1_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_RISER1_SLOT1_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_RISER1_SLOT1_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_RISER1_SLOT1_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_RISER1_SLOT1_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_RISER1_SLOT1_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_RISER1_SLOT1_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_RISER1_SLOT2_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_RISER1_SLOT2_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_RISER1_SLOT2_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_RISER1_SLOT2_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_RISER1_SLOT2_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_RISER1_SLOT2_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_RISER1_SLOT3_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_RISER1_SLOT3_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_RISER1_SLOT3_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_RISER1_SLOT3_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_RISER1_SLOT3_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_RISER1_SLOT3_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_RISER2_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_RISER2_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_RISER2_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_RISER2_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_RISER2_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_RISER2_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_RISER2_SLOT4_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_RISER2_SLOT4_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_RISER2_SLOT4_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_RISER2_SLOT4_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_RISER2_SLOT4_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_RISER2_SLOT4_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_RISER2_SLOT5_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_RISER2_SLOT5_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_RISER2_SLOT5_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_RISER2_SLOT5_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_RISER2_SLOT5_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_RISER2_SLOT5_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_RISER2_SLOT6_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_RISER2_SLOT6_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_RISER2_SLOT6_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_RISER2_SLOT6_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_RISER2_SLOT6_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_RISER2_SLOT6_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_SASSTATE_DISABLED = "Disabled"
    VP_SLOT_SASSTATE_ENABLED = "Enabled"
    VP_SLOT_SASSTATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_SASSTATE_UEFI_ONLY = "UEFI Only"
    _VP_SLOT_SASSTATE_DISABLED = "disabled"
    _VP_SLOT_SASSTATE_ENABLED = "enabled"
    VP_SLOT_SASSTATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_SSDSLOT1_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_SSDSLOT1_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_SSDSLOT1_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_SSDSLOT1_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_SSDSLOT1_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_SSDSLOT1_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_SSDSLOT2_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_SSDSLOT2_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_SSDSLOT2_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_SSDSLOT2_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_SSDSLOT2_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_SSDSLOT2_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_IOESLOT1_STATE_DISABLED = "Disabled"
    VP_IOESLOT1_STATE_ENABLED = "Enabled"
    VP_IOESLOT1_STATE_LEGACY_ONLY = "Legacy Only"
    VP_IOESLOT1_STATE_UEFI_ONLY = "UEFI Only"
    VP_IOESLOT1_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_IOESLOT2_STATE_DISABLED = "Disabled"
    VP_IOESLOT2_STATE_ENABLED = "Enabled"
    VP_IOESLOT2_STATE_LEGACY_ONLY = "Legacy Only"
    VP_IOESLOT2_STATE_UEFI_ONLY = "UEFI Only"
    VP_IOESLOT2_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_IOEMEZZ1_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_IOEMEZZ1_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_IOEMEZZ1_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_IOEMEZZ1_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_IOEMEZZ1_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_IOEMEZZ1_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_IOEMEZZ1_STATE_DISABLED = "Disabled"
    VP_SLOT_IOEMEZZ1_STATE_ENABLED = "Enabled"
    VP_SLOT_IOEMEZZ1_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_IOEMEZZ1_STATE_UEFI_ONLY = "UEFI Only"
    VP_SLOT_IOEMEZZ1_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_IOENVME1_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_IOENVME1_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_IOENVME1_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_IOENVME1_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_IOENVME1_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_IOENVME1_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_IOENVME1_STATE_DISABLED = "Disabled"
    VP_SLOT_IOENVME1_STATE_ENABLED = "Enabled"
    VP_SLOT_IOENVME1_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_IOENVME1_STATE_UEFI_ONLY = "UEFI Only"
    VP_SLOT_IOENVME1_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_IOENVME2_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_IOENVME2_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_IOENVME2_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_IOENVME2_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_IOENVME2_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_IOENVME2_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_IOENVME2_STATE_DISABLED = "Disabled"
    VP_SLOT_IOENVME2_STATE_ENABLED = "Enabled"
    VP_SLOT_IOENVME2_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_IOENVME2_STATE_UEFI_ONLY = "UEFI Only"
    VP_SLOT_IOENVME2_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_IOESLOT1_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_IOESLOT1_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_IOESLOT1_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_IOESLOT1_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_IOESLOT1_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_IOESLOT1_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_IOESLOT2_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_IOESLOT2_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_IOESLOT2_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_IOESLOT2_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_IOESLOT2_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_IOESLOT2_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_MLINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_MLINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_MLINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_MLINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_MLINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_SBMEZZ1_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_SBMEZZ1_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_SBMEZZ1_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_SBMEZZ1_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_SBMEZZ1_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_SBMEZZ1_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_SBMEZZ1_STATE_DISABLED = "Disabled"
    VP_SLOT_SBMEZZ1_STATE_ENABLED = "Enabled"
    VP_SLOT_SBMEZZ1_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_SBMEZZ1_STATE_UEFI_ONLY = "UEFI Only"
    VP_SLOT_SBMEZZ1_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_SBNVME1_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_SBNVME1_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_SBNVME1_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_SBNVME1_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_SBNVME1_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_SBNVME1_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_SBNVME1_STATE_DISABLED = "Disabled"
    VP_SLOT_SBNVME1_STATE_ENABLED = "Enabled"
    VP_SLOT_SBNVME1_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_SBNVME1_STATE_UEFI_ONLY = "UEFI Only"
    VP_SLOT_SBNVME1_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_SIOC1_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_SIOC1_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_SIOC1_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_SIOC1_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_SIOC1_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_SIOC1_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_SIOC1_STATE_DISABLED = "Disabled"
    VP_SLOT_SIOC1_STATE_ENABLED = "Enabled"
    VP_SLOT_SIOC1_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_SIOC1_STATE_UEFI_ONLY = "UEFI Only"
    VP_SLOT_SIOC1_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_SIOC2_LINK_SPEED_AUTO = "Auto"
    VP_SLOT_SIOC2_LINK_SPEED_DISABLED = "Disabled"
    VP_SLOT_SIOC2_LINK_SPEED_GEN1 = "GEN1"
    VP_SLOT_SIOC2_LINK_SPEED_GEN2 = "GEN2"
    VP_SLOT_SIOC2_LINK_SPEED_GEN3 = "GEN3"
    VP_SLOT_SIOC2_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    VP_SLOT_SIOC2_STATE_DISABLED = "Disabled"
    VP_SLOT_SIOC2_STATE_ENABLED = "Enabled"
    VP_SLOT_SIOC2_STATE_LEGACY_ONLY = "Legacy Only"
    VP_SLOT_SIOC2_STATE_UEFI_ONLY = "UEFI Only"
    VP_SLOT_SIOC2_STATE_PLATFORM_DEFAULT = "platform-default"


class BiosVfPCISlotOptionROMEnable(ManagedObject):
    """This is BiosVfPCISlotOptionROMEnable class."""

    consts = BiosVfPCISlotOptionROMEnableConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPCISlotOptionROMEnable", "biosVfPCISlotOptionROMEnable", "PCI-Slot-OptionROM-Enable", VersionMeta.Version151f, "InputOutput", 0x1fffffffffff, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfPCISlotOptionROMEnable", "biosVfPCISlotOptionROMEnable", "PCI-Slot-OptionROM-Enable", VersionMeta.Version2013e, "InputOutput", 0x1ffffffffffff, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_slot10_link_speed": MoPropertyMeta("vp_slot10_link_speed", "vpSlot10LinkSpeed", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot10_state": MoPropertyMeta("vp_slot10_state", "vpSlot10State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot1_link_speed": MoPropertyMeta("vp_slot1_link_speed", "vpSlot1LinkSpeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot1_state": MoPropertyMeta("vp_slot1_state", "vpSlot1State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot2_link_speed": MoPropertyMeta("vp_slot2_link_speed", "vpSlot2LinkSpeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot2_state": MoPropertyMeta("vp_slot2_state", "vpSlot2State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot3_link_speed": MoPropertyMeta("vp_slot3_link_speed", "vpSlot3LinkSpeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot3_state": MoPropertyMeta("vp_slot3_state", "vpSlot3State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot4_link_speed": MoPropertyMeta("vp_slot4_link_speed", "vpSlot4LinkSpeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot4_state": MoPropertyMeta("vp_slot4_state", "vpSlot4State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot5_link_speed": MoPropertyMeta("vp_slot5_link_speed", "vpSlot5LinkSpeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot5_state": MoPropertyMeta("vp_slot5_state", "vpSlot5State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot6_link_speed": MoPropertyMeta("vp_slot6_link_speed", "vpSlot6LinkSpeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot6_state": MoPropertyMeta("vp_slot6_state", "vpSlot6State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot7_link_speed": MoPropertyMeta("vp_slot7_link_speed", "vpSlot7LinkSpeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot7_state": MoPropertyMeta("vp_slot7_state", "vpSlot7State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot8_link_speed": MoPropertyMeta("vp_slot8_link_speed", "vpSlot8LinkSpeed", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x100000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot8_state": MoPropertyMeta("vp_slot8_state", "vpSlot8State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot9_link_speed": MoPropertyMeta("vp_slot9_link_speed", "vpSlot9LinkSpeed", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x400000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot9_state": MoPropertyMeta("vp_slot9_state", "vpSlot9State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_hba_state": MoPropertyMeta("vp_slot_hba_state", "vpSlotHBAState", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x1000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_mlom_state": MoPropertyMeta("vp_slot_mlom_state", "vpSlotMLOMState", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_mezz_state": MoPropertyMeta("vp_slot_mezz_state", "vpSlotMezzState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_n1_state": MoPropertyMeta("vp_slot_n1_state", "vpSlotN1State", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x8000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_n2_state": MoPropertyMeta("vp_slot_n2_state", "vpSlotN2State", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x10000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_sas_state": MoPropertyMeta("vp_slot_sas_state", "vpSlotSASState", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x20000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_flom_link_speed": MoPropertyMeta("vp_slot_flom_link_speed", "vpSlotFLOMLinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x40000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_front_slot5_link_speed": MoPropertyMeta("vp_slot_front_slot5_link_speed", "vpSlotFrontSlot5LinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x80000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_front_slot6_link_speed": MoPropertyMeta("vp_slot_front_slot6_link_speed", "vpSlotFrontSlot6LinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x100000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_hba_link_speed": MoPropertyMeta("vp_slot_hba_link_speed", "vpSlotHBALinkSpeed", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x200000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_mlom_link_speed": MoPropertyMeta("vp_slot_mlom_link_speed", "vpSlotMLOMLinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x400000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_riser1_link_speed": MoPropertyMeta("vp_slot_riser1_link_speed", "vpSlotRiser1LinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x800000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_riser1_slot1_link_speed": MoPropertyMeta("vp_slot_riser1_slot1_link_speed", "vpSlotRiser1Slot1LinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x1000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_riser1_slot2_link_speed": MoPropertyMeta("vp_slot_riser1_slot2_link_speed", "vpSlotRiser1Slot2LinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x2000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_riser1_slot3_link_speed": MoPropertyMeta("vp_slot_riser1_slot3_link_speed", "vpSlotRiser1Slot3LinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x4000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_riser2_link_speed": MoPropertyMeta("vp_slot_riser2_link_speed", "vpSlotRiser2LinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x8000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_riser2_slot4_link_speed": MoPropertyMeta("vp_slot_riser2_slot4_link_speed", "vpSlotRiser2Slot4LinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x10000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_riser2_slot5_link_speed": MoPropertyMeta("vp_slot_riser2_slot5_link_speed", "vpSlotRiser2Slot5LinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x20000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_riser2_slot6_link_speed": MoPropertyMeta("vp_slot_riser2_slot6_link_speed", "vpSlotRiser2Slot6LinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x40000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_ssd_slot1_link_speed": MoPropertyMeta("vp_slot_ssd_slot1_link_speed", "vpSlotSSDSlot1LinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x80000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_ssd_slot2_link_speed": MoPropertyMeta("vp_slot_ssd_slot2_link_speed", "vpSlotSSDSlot2LinkSpeed", "string", VersionMeta.Version2010b, MoPropertyMeta.READ_WRITE, 0x100000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_slot10_link_speed": MoPropertyMeta("vp_slot10_link_speed", "vpSlot10LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot10_state": MoPropertyMeta("vp_slot10_state", "vpSlot10State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot1_link_speed": MoPropertyMeta("vp_slot1_link_speed", "vpSlot1LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot1_state": MoPropertyMeta("vp_slot1_state", "vpSlot1State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot2_link_speed": MoPropertyMeta("vp_slot2_link_speed", "vpSlot2LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot2_state": MoPropertyMeta("vp_slot2_state", "vpSlot2State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot3_link_speed": MoPropertyMeta("vp_slot3_link_speed", "vpSlot3LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot3_state": MoPropertyMeta("vp_slot3_state", "vpSlot3State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot4_link_speed": MoPropertyMeta("vp_slot4_link_speed", "vpSlot4LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot4_state": MoPropertyMeta("vp_slot4_state", "vpSlot4State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot5_link_speed": MoPropertyMeta("vp_slot5_link_speed", "vpSlot5LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot5_state": MoPropertyMeta("vp_slot5_state", "vpSlot5State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot6_link_speed": MoPropertyMeta("vp_slot6_link_speed", "vpSlot6LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot6_state": MoPropertyMeta("vp_slot6_state", "vpSlot6State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot7_link_speed": MoPropertyMeta("vp_slot7_link_speed", "vpSlot7LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot7_state": MoPropertyMeta("vp_slot7_state", "vpSlot7State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot8_link_speed": MoPropertyMeta("vp_slot8_link_speed", "vpSlot8LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot8_state": MoPropertyMeta("vp_slot8_state", "vpSlot8State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot9_link_speed": MoPropertyMeta("vp_slot9_link_speed", "vpSlot9LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot9_state": MoPropertyMeta("vp_slot9_state", "vpSlot9State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_hba_state": MoPropertyMeta("vp_slot_hba_state", "vpSlotHBAState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_mlom_state": MoPropertyMeta("vp_slot_mlom_state", "vpSlotMLOMState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_mezz_state": MoPropertyMeta("vp_slot_mezz_state", "vpSlotMezzState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_n1_state": MoPropertyMeta("vp_slot_n1_state", "vpSlotN1State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_n2_state": MoPropertyMeta("vp_slot_n2_state", "vpSlotN2State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_sas_state": MoPropertyMeta("vp_slot_sas_state", "vpSlotSASState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_ioe_slot1_state": MoPropertyMeta("vp_ioe_slot1_state", "vpIOESlot1State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_ioe_slot2_state": MoPropertyMeta("vp_ioe_slot2_state", "vpIOESlot2State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_ioe_mezz1_link_speed": MoPropertyMeta("vp_slot_ioe_mezz1_link_speed", "vpSlotIOEMezz1LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_ioe_mezz1_state": MoPropertyMeta("vp_slot_ioe_mezz1_state", "vpSlotIOEMezz1State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_ioenv_me1_link_speed": MoPropertyMeta("vp_slot_ioenv_me1_link_speed", "vpSlotIOENVMe1LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_ioenv_me1_state": MoPropertyMeta("vp_slot_ioenv_me1_state", "vpSlotIOENVMe1State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_ioenv_me2_link_speed": MoPropertyMeta("vp_slot_ioenv_me2_link_speed", "vpSlotIOENVMe2LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_ioenv_me2_state": MoPropertyMeta("vp_slot_ioenv_me2_state", "vpSlotIOENVMe2State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_ioe_slot1_link_speed": MoPropertyMeta("vp_slot_ioe_slot1_link_speed", "vpSlotIOESlot1LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_ioe_slot2_link_speed": MoPropertyMeta("vp_slot_ioe_slot2_link_speed", "vpSlotIOESlot2LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_m_link_speed": MoPropertyMeta("vp_slot_m_link_speed", "vpSlotMLinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000000000, None, None, None, ["Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_sb_mezz1_link_speed": MoPropertyMeta("vp_slot_sb_mezz1_link_speed", "vpSlotSBMezz1LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_sb_mezz1_state": MoPropertyMeta("vp_slot_sb_mezz1_state", "vpSlotSBMezz1State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40000000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_sbnv_me1_link_speed": MoPropertyMeta("vp_slot_sbnv_me1_link_speed", "vpSlotSBNVMe1LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_sbnv_me1_state": MoPropertyMeta("vp_slot_sbnv_me1_state", "vpSlotSBNVMe1State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100000000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_sio_c1_link_speed": MoPropertyMeta("vp_slot_sio_c1_link_speed", "vpSlotSIOC1LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_sio_c1_state": MoPropertyMeta("vp_slot_sio_c1_state", "vpSlotSIOC1State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400000000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
            "vp_slot_sio_c2_link_speed": MoPropertyMeta("vp_slot_sio_c2_link_speed", "vpSlotSIOC2LinkSpeed", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800000000000, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], []), 
            "vp_slot_sio_c2_state": MoPropertyMeta("vp_slot_sio_c2_state", "vpSlotSIOC2State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000000000000, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSlot10LinkSpeed": "vp_slot10_link_speed", 
            "vpSlot10State": "vp_slot10_state", 
            "vpSlot1LinkSpeed": "vp_slot1_link_speed", 
            "vpSlot1State": "vp_slot1_state", 
            "vpSlot2LinkSpeed": "vp_slot2_link_speed", 
            "vpSlot2State": "vp_slot2_state", 
            "vpSlot3LinkSpeed": "vp_slot3_link_speed", 
            "vpSlot3State": "vp_slot3_state", 
            "vpSlot4LinkSpeed": "vp_slot4_link_speed", 
            "vpSlot4State": "vp_slot4_state", 
            "vpSlot5LinkSpeed": "vp_slot5_link_speed", 
            "vpSlot5State": "vp_slot5_state", 
            "vpSlot6LinkSpeed": "vp_slot6_link_speed", 
            "vpSlot6State": "vp_slot6_state", 
            "vpSlot7LinkSpeed": "vp_slot7_link_speed", 
            "vpSlot7State": "vp_slot7_state", 
            "vpSlot8LinkSpeed": "vp_slot8_link_speed", 
            "vpSlot8State": "vp_slot8_state", 
            "vpSlot9LinkSpeed": "vp_slot9_link_speed", 
            "vpSlot9State": "vp_slot9_state", 
            "vpSlotHBAState": "vp_slot_hba_state", 
            "vpSlotMLOMState": "vp_slot_mlom_state", 
            "vpSlotMezzState": "vp_slot_mezz_state", 
            "vpSlotN1State": "vp_slot_n1_state", 
            "vpSlotN2State": "vp_slot_n2_state", 
            "vpSlotSASState": "vp_slot_sas_state", 
            "vpSlotFLOMLinkSpeed": "vp_slot_flom_link_speed", 
            "vpSlotFrontSlot5LinkSpeed": "vp_slot_front_slot5_link_speed", 
            "vpSlotFrontSlot6LinkSpeed": "vp_slot_front_slot6_link_speed", 
            "vpSlotHBALinkSpeed": "vp_slot_hba_link_speed", 
            "vpSlotMLOMLinkSpeed": "vp_slot_mlom_link_speed", 
            "vpSlotRiser1LinkSpeed": "vp_slot_riser1_link_speed", 
            "vpSlotRiser1Slot1LinkSpeed": "vp_slot_riser1_slot1_link_speed", 
            "vpSlotRiser1Slot2LinkSpeed": "vp_slot_riser1_slot2_link_speed", 
            "vpSlotRiser1Slot3LinkSpeed": "vp_slot_riser1_slot3_link_speed", 
            "vpSlotRiser2LinkSpeed": "vp_slot_riser2_link_speed", 
            "vpSlotRiser2Slot4LinkSpeed": "vp_slot_riser2_slot4_link_speed", 
            "vpSlotRiser2Slot5LinkSpeed": "vp_slot_riser2_slot5_link_speed", 
            "vpSlotRiser2Slot6LinkSpeed": "vp_slot_riser2_slot6_link_speed", 
            "vpSlotSSDSlot1LinkSpeed": "vp_slot_ssd_slot1_link_speed", 
            "vpSlotSSDSlot2LinkSpeed": "vp_slot_ssd_slot2_link_speed", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSlot10LinkSpeed": "vp_slot10_link_speed", 
            "vpSlot10State": "vp_slot10_state", 
            "vpSlot1LinkSpeed": "vp_slot1_link_speed", 
            "vpSlot1State": "vp_slot1_state", 
            "vpSlot2LinkSpeed": "vp_slot2_link_speed", 
            "vpSlot2State": "vp_slot2_state", 
            "vpSlot3LinkSpeed": "vp_slot3_link_speed", 
            "vpSlot3State": "vp_slot3_state", 
            "vpSlot4LinkSpeed": "vp_slot4_link_speed", 
            "vpSlot4State": "vp_slot4_state", 
            "vpSlot5LinkSpeed": "vp_slot5_link_speed", 
            "vpSlot5State": "vp_slot5_state", 
            "vpSlot6LinkSpeed": "vp_slot6_link_speed", 
            "vpSlot6State": "vp_slot6_state", 
            "vpSlot7LinkSpeed": "vp_slot7_link_speed", 
            "vpSlot7State": "vp_slot7_state", 
            "vpSlot8LinkSpeed": "vp_slot8_link_speed", 
            "vpSlot8State": "vp_slot8_state", 
            "vpSlot9LinkSpeed": "vp_slot9_link_speed", 
            "vpSlot9State": "vp_slot9_state", 
            "vpSlotHBAState": "vp_slot_hba_state", 
            "vpSlotMLOMState": "vp_slot_mlom_state", 
            "vpSlotMezzState": "vp_slot_mezz_state", 
            "vpSlotN1State": "vp_slot_n1_state", 
            "vpSlotN2State": "vp_slot_n2_state", 
            "vpSlotSASState": "vp_slot_sas_state", 
            "vpIOESlot1State": "vp_ioe_slot1_state", 
            "vpIOESlot2State": "vp_ioe_slot2_state", 
            "vpSlotIOEMezz1LinkSpeed": "vp_slot_ioe_mezz1_link_speed", 
            "vpSlotIOEMezz1State": "vp_slot_ioe_mezz1_state", 
            "vpSlotIOENVMe1LinkSpeed": "vp_slot_ioenv_me1_link_speed", 
            "vpSlotIOENVMe1State": "vp_slot_ioenv_me1_state", 
            "vpSlotIOENVMe2LinkSpeed": "vp_slot_ioenv_me2_link_speed", 
            "vpSlotIOENVMe2State": "vp_slot_ioenv_me2_state", 
            "vpSlotIOESlot1LinkSpeed": "vp_slot_ioe_slot1_link_speed", 
            "vpSlotIOESlot2LinkSpeed": "vp_slot_ioe_slot2_link_speed", 
            "vpSlotMLinkSpeed": "vp_slot_m_link_speed", 
            "vpSlotSBMezz1LinkSpeed": "vp_slot_sb_mezz1_link_speed", 
            "vpSlotSBMezz1State": "vp_slot_sb_mezz1_state", 
            "vpSlotSBNVMe1LinkSpeed": "vp_slot_sbnv_me1_link_speed", 
            "vpSlotSBNVMe1State": "vp_slot_sbnv_me1_state", 
            "vpSlotSIOC1LinkSpeed": "vp_slot_sio_c1_link_speed", 
            "vpSlotSIOC1State": "vp_slot_sio_c1_state", 
            "vpSlotSIOC2LinkSpeed": "vp_slot_sio_c2_link_speed", 
            "vpSlotSIOC2State": "vp_slot_sio_c2_state", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_slot10_link_speed = None
        self.vp_slot10_state = None
        self.vp_slot1_link_speed = None
        self.vp_slot1_state = None
        self.vp_slot2_link_speed = None
        self.vp_slot2_state = None
        self.vp_slot3_link_speed = None
        self.vp_slot3_state = None
        self.vp_slot4_link_speed = None
        self.vp_slot4_state = None
        self.vp_slot5_link_speed = None
        self.vp_slot5_state = None
        self.vp_slot6_link_speed = None
        self.vp_slot6_state = None
        self.vp_slot7_link_speed = None
        self.vp_slot7_state = None
        self.vp_slot8_link_speed = None
        self.vp_slot8_state = None
        self.vp_slot9_link_speed = None
        self.vp_slot9_state = None
        self.vp_slot_hba_state = None
        self.vp_slot_mlom_state = None
        self.vp_slot_mezz_state = None
        self.vp_slot_n1_state = None
        self.vp_slot_n2_state = None
        self.vp_slot_sas_state = None
        self.vp_slot_flom_link_speed = None
        self.vp_slot_front_slot5_link_speed = None
        self.vp_slot_front_slot6_link_speed = None
        self.vp_slot_hba_link_speed = None
        self.vp_slot_mlom_link_speed = None
        self.vp_slot_riser1_link_speed = None
        self.vp_slot_riser1_slot1_link_speed = None
        self.vp_slot_riser1_slot2_link_speed = None
        self.vp_slot_riser1_slot3_link_speed = None
        self.vp_slot_riser2_link_speed = None
        self.vp_slot_riser2_slot4_link_speed = None
        self.vp_slot_riser2_slot5_link_speed = None
        self.vp_slot_riser2_slot6_link_speed = None
        self.vp_slot_ssd_slot1_link_speed = None
        self.vp_slot_ssd_slot2_link_speed = None
        self.vp_ioe_slot1_state = None
        self.vp_ioe_slot2_state = None
        self.vp_slot_ioe_mezz1_link_speed = None
        self.vp_slot_ioe_mezz1_state = None
        self.vp_slot_ioenv_me1_link_speed = None
        self.vp_slot_ioenv_me1_state = None
        self.vp_slot_ioenv_me2_link_speed = None
        self.vp_slot_ioenv_me2_state = None
        self.vp_slot_ioe_slot1_link_speed = None
        self.vp_slot_ioe_slot2_link_speed = None
        self.vp_slot_m_link_speed = None
        self.vp_slot_sb_mezz1_link_speed = None
        self.vp_slot_sb_mezz1_state = None
        self.vp_slot_sbnv_me1_link_speed = None
        self.vp_slot_sbnv_me1_state = None
        self.vp_slot_sio_c1_link_speed = None
        self.vp_slot_sio_c1_state = None
        self.vp_slot_sio_c2_link_speed = None
        self.vp_slot_sio_c2_state = None

        ManagedObject.__init__(self, "BiosVfPCISlotOptionROMEnable", parent_mo_or_dn, **kwargs)

