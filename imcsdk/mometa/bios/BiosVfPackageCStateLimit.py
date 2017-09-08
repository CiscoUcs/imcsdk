"""This module contains the general information for BiosVfPackageCStateLimit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPackageCStateLimitConsts:
    VP_PACKAGE_CSTATE_LIMIT_C0_C1 = "C0/C1"
    VP_PACKAGE_CSTATE_LIMIT_C2 = "C2"
    VP_PACKAGE_CSTATE_LIMIT_C6_RETENTION = "C6 Retention"
    VP_PACKAGE_CSTATE_LIMIT_C6_NON_RETENTION = "C6 non Retention"
    VP_PACKAGE_CSTATE_LIMIT_C0_STATE = "c0-state"
    VP_PACKAGE_CSTATE_LIMIT_C1_STATE = "c1-state"
    VP_PACKAGE_CSTATE_LIMIT_C3_STATE = "c3-state"
    VP_PACKAGE_CSTATE_LIMIT_C6_STATE = "c6-state"
    VP_PACKAGE_CSTATE_LIMIT_NO_LIMIT = "no-limit"
    VP_PACKAGE_CSTATE_LIMIT_PLATFORM_DEFAULT = "platform-default"
    __VP_PACKAGE_CSTATE_LIMIT_C6_NON_RETENTION = "c6-non-retention"
    __VP_PACKAGE_CSTATE_LIMIT_C6_RETENTION = "c6-retention"


class BiosVfPackageCStateLimit(ManagedObject):
    """This is BiosVfPackageCStateLimit class."""

    consts = BiosVfPackageCStateLimitConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPackageCStateLimit", "biosVfPackageCStateLimit", "Package-CState-Limit", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfPackageCStateLimit", "biosVfPackageCStateLimit", "Package-CState-Limit", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_package_c_state_limit": MoPropertyMeta("vp_package_c_state_limit", "vpPackageCStateLimit", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["C0/C1", "C2", "C6 Retention", "C6 non Retention", "c0-state", "c1-state", "c3-state", "c6-state", "no-limit", "platform-default"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_package_c_state_limit": MoPropertyMeta("vp_package_c_state_limit", "vpPackageCStateLimit", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["C0/C1", "C2", "C6 Retention", "C6 non Retention", "c0-state", "c0/c1", "c1-state", "c2", "c3-state", "c6-non-retention", "c6-retention", "c6-state", "no-limit", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPackageCStateLimit": "vp_package_c_state_limit", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPackageCStateLimit": "vp_package_c_state_limit", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_package_c_state_limit = None

        ManagedObject.__init__(self, "BiosVfPackageCStateLimit", parent_mo_or_dn, **kwargs)

