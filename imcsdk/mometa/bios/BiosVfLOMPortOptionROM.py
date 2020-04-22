"""This module contains the general information for BiosVfLOMPortOptionROM ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfLOMPortOptionROMConsts:
    VP_LOMPORT0_STATE_DISABLED = "Disabled"
    VP_LOMPORT0_STATE_ENABLED = "Enabled"
    VP_LOMPORT0_STATE_LEGACY_ONLY = "Legacy Only"
    VP_LOMPORT0_STATE_UEFI_ONLY = "UEFI Only"
    _VP_LOMPORT0_STATE_DISABLED = "disabled"
    _VP_LOMPORT0_STATE_ENABLED = "enabled"
    VP_LOMPORT0_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_LOMPORT1_STATE_DISABLED = "Disabled"
    VP_LOMPORT1_STATE_ENABLED = "Enabled"
    VP_LOMPORT1_STATE_LEGACY_ONLY = "Legacy Only"
    VP_LOMPORT1_STATE_UEFI_ONLY = "UEFI Only"
    _VP_LOMPORT1_STATE_DISABLED = "disabled"
    _VP_LOMPORT1_STATE_ENABLED = "enabled"
    VP_LOMPORT1_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_LOMPORT2_STATE_DISABLED = "Disabled"
    VP_LOMPORT2_STATE_ENABLED = "Enabled"
    VP_LOMPORT2_STATE_LEGACY_ONLY = "Legacy Only"
    VP_LOMPORT2_STATE_UEFI_ONLY = "UEFI Only"
    _VP_LOMPORT2_STATE_DISABLED = "disabled"
    _VP_LOMPORT2_STATE_ENABLED = "enabled"
    VP_LOMPORT2_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_LOMPORT3_STATE_DISABLED = "Disabled"
    VP_LOMPORT3_STATE_ENABLED = "Enabled"
    VP_LOMPORT3_STATE_LEGACY_ONLY = "Legacy Only"
    VP_LOMPORT3_STATE_UEFI_ONLY = "UEFI Only"
    _VP_LOMPORT3_STATE_DISABLED = "disabled"
    _VP_LOMPORT3_STATE_ENABLED = "enabled"
    VP_LOMPORT3_STATE_PLATFORM_DEFAULT = "platform-default"
    VP_LOMPORTS_ALL_STATE_DISABLED = "Disabled"
    VP_LOMPORTS_ALL_STATE_ENABLED = "Enabled"
    _VP_LOMPORTS_ALL_STATE_DISABLED = "disabled"
    _VP_LOMPORTS_ALL_STATE_ENABLED = "enabled"
    VP_LOMPORTS_ALL_STATE_PLATFORM_DEFAULT = "platform-default"


class BiosVfLOMPortOptionROM(ManagedObject):
    """This is BiosVfLOMPortOptionROM class."""

    consts = BiosVfLOMPortOptionROMConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfLOMPortOptionROM", "biosVfLOMPortOptionROM", "LOMPort-OptionROM", VersionMeta.Version151f, "InputOutput", 0x1ff, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfLOMPortOptionROM", "biosVfLOMPortOptionROM", "LOMPort-OptionROM", VersionMeta.Version2013e, "InputOutput", 0x1ff, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_lom_port0_state": MoPropertyMeta("vp_lom_port0_state", "vpLOMPort0State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []),
            "vp_lom_port1_state": MoPropertyMeta("vp_lom_port1_state", "vpLOMPort1State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []),
            "vp_lom_port2_state": MoPropertyMeta("vp_lom_port2_state", "vpLOMPort2State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []),
            "vp_lom_port3_state": MoPropertyMeta("vp_lom_port3_state", "vpLOMPort3State", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []),
            "vp_lom_ports_all_state": MoPropertyMeta("vp_lom_ports_all_state", "vpLOMPortsAllState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_lom_port0_state": MoPropertyMeta("vp_lom_port0_state", "vpLOMPort0State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []),
            "vp_lom_port1_state": MoPropertyMeta("vp_lom_port1_state", "vpLOMPort1State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []),
            "vp_lom_port2_state": MoPropertyMeta("vp_lom_port2_state", "vpLOMPort2State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []),
            "vp_lom_port3_state": MoPropertyMeta("vp_lom_port3_state", "vpLOMPort3State", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], []),
            "vp_lom_ports_all_state": MoPropertyMeta("vp_lom_ports_all_state", "vpLOMPortsAllState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpLOMPort0State": "vp_lom_port0_state", 
            "vpLOMPort1State": "vp_lom_port1_state", 
            "vpLOMPort2State": "vp_lom_port2_state", 
            "vpLOMPort3State": "vp_lom_port3_state", 
            "vpLOMPortsAllState": "vp_lom_ports_all_state", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpLOMPort0State": "vp_lom_port0_state", 
            "vpLOMPort1State": "vp_lom_port1_state", 
            "vpLOMPort2State": "vp_lom_port2_state", 
            "vpLOMPort3State": "vp_lom_port3_state", 
            "vpLOMPortsAllState": "vp_lom_ports_all_state", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_lom_port0_state = None
        self.vp_lom_port1_state = None
        self.vp_lom_port2_state = None
        self.vp_lom_port3_state = None
        self.vp_lom_ports_all_state = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfLOMPortOptionROM", parent_mo_or_dn, **kwargs)

