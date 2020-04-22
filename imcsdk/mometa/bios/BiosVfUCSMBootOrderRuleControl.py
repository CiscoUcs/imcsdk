"""This module contains the general information for BiosVfUCSMBootOrderRuleControl ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfUCSMBootOrderRuleControlConsts:
    VP_UCSMBOOT_ORDER_RULE_LOOSE = "Loose"
    VP_UCSMBOOT_ORDER_RULE_STRICT = "Strict"
    VP_UCSMBOOT_ORDER_RULE_PLATFORM_DEFAULT = "platform-default"


class BiosVfUCSMBootOrderRuleControl(ManagedObject):
    """This is BiosVfUCSMBootOrderRuleControl class."""

    consts = BiosVfUCSMBootOrderRuleControlConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfUCSMBootOrderRuleControl", "biosVfUCSMBootOrderRuleControl", "Boot-Order-Rules", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfUCSMBootOrderRuleControl", "biosVfUCSMBootOrderRuleControl", "Boot-Order-Rules", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_ucsm_boot_order_rule": MoPropertyMeta("vp_ucsm_boot_order_rule", "vpUCSMBootOrderRule", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Loose", "Strict", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_ucsm_boot_order_rule": MoPropertyMeta("vp_ucsm_boot_order_rule", "vpUCSMBootOrderRule", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Loose", "Strict", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpUCSMBootOrderRule": "vp_ucsm_boot_order_rule", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpUCSMBootOrderRule": "vp_ucsm_boot_order_rule", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_ucsm_boot_order_rule = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfUCSMBootOrderRuleControl", parent_mo_or_dn, **kwargs)

