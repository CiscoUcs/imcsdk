"""This module contains the general information for BiosVfCkeLowPolicy ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCkeLowPolicyConsts:
    VP_CKE_LOW_POLICY_AUTO = "auto"
    VP_CKE_LOW_POLICY_DISABLED = "disabled"
    VP_CKE_LOW_POLICY_FAST = "fast"
    VP_CKE_LOW_POLICY_PLATFORM_DEFAULT = "platform-default"
    VP_CKE_LOW_POLICY_SLOW = "slow"


class BiosVfCkeLowPolicy(ManagedObject):
    """This is BiosVfCkeLowPolicy class."""

    consts = BiosVfCkeLowPolicyConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCkeLowPolicy", "biosVfCkeLowPolicy", "Cke-Low-Policy", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfCkeLowPolicy", "biosVfCkeLowPolicy", "Cke-Low-Policy", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cke_low_policy": MoPropertyMeta("vp_cke_low_policy", "vpCkeLowPolicy", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["auto", "disabled", "fast", "platform-default", "slow"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cke_low_policy": MoPropertyMeta("vp_cke_low_policy", "vpCkeLowPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["auto", "disabled", "fast", "platform-default", "slow"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCkeLowPolicy": "vp_cke_low_policy", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCkeLowPolicy": "vp_cke_low_policy", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_cke_low_policy = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfCkeLowPolicy", parent_mo_or_dn, **kwargs)

