"""This module contains the general information for BiosVfAdvancedMemTest ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfAdvancedMemTestConsts:
    VP_ADVANCED_MEM_TEST_AUTO = "Auto"
    VP_ADVANCED_MEM_TEST_DISABLED = "Disabled"
    VP_ADVANCED_MEM_TEST_ENABLED = "Enabled"
    _VP_ADVANCED_MEM_TEST_DISABLED = "disabled"
    _VP_ADVANCED_MEM_TEST_ENABLED = "enabled"
    VP_ADVANCED_MEM_TEST_PLATFORM_DEFAULT = "platform-default"


class BiosVfAdvancedMemTest(ManagedObject):
    """This is BiosVfAdvancedMemTest class."""

    consts = BiosVfAdvancedMemTestConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfAdvancedMemTest", "biosVfAdvancedMemTest", "Advanced-Memory-Test", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfAdvancedMemTest", "biosVfAdvancedMemTest", "Advanced-Memory-Test", VersionMeta.Version413a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_advanced_mem_test": MoPropertyMeta("vp_advanced_mem_test", "vpAdvancedMemTest", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_advanced_mem_test": MoPropertyMeta("vp_advanced_mem_test", "vpAdvancedMemTest", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version413a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAdvancedMemTest": "vp_advanced_mem_test", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpAdvancedMemTest": "vp_advanced_mem_test", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_advanced_mem_test = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfAdvancedMemTest", parent_mo_or_dn, **kwargs)

