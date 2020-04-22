"""This module contains the general information for BiosVfASPMSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfASPMSupportConsts:
    VP_ASPMSUPPORT_AUTO = "Auto"
    VP_ASPMSUPPORT_DISABLED = "Disabled"
    VP_ASPMSUPPORT_FORCE_L0S = "Force L0s"
    VP_ASPMSUPPORT_L1_ONLY = "L1 Only"
    VP_ASPMSUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfASPMSupport(ManagedObject):
    """This is BiosVfASPMSupport class."""

    consts = BiosVfASPMSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfASPMSupport", "biosVfASPMSupport", "ASPM-Support", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfASPMSupport", "biosVfASPMSupport", "ASPM-Support", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_aspm_support": MoPropertyMeta("vp_aspm_support", "vpASPMSupport", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Force L0s", "L1 Only", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_aspm_support": MoPropertyMeta("vp_aspm_support", "vpASPMSupport", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Force L0s", "L1 Only", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpASPMSupport": "vp_aspm_support", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpASPMSupport": "vp_aspm_support", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_aspm_support = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfASPMSupport", parent_mo_or_dn, **kwargs)

