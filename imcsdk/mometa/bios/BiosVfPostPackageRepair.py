"""This module contains the general information for BiosVfPostPackageRepair ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfPostPackageRepairConsts:
    VP_POST_PACKAGE_REPAIR_DISABLED = "Disabled"
    VP_POST_PACKAGE_REPAIR_HARD_PPR = "Hard PPR"
    VP_POST_PACKAGE_REPAIR_PLATFORM_DEFAULT = "platform-default"


class BiosVfPostPackageRepair(ManagedObject):
    """This is BiosVfPostPackageRepair class."""

    consts = BiosVfPostPackageRepairConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfPostPackageRepair", "biosVfPostPackageRepair", "post-package-repair", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_post_package_repair": MoPropertyMeta("vp_post_package_repair", "vpPostPackageRepair", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Hard PPR", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpPostPackageRepair": "vp_post_package_repair", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_post_package_repair = None

        ManagedObject.__init__(self, "BiosVfPostPackageRepair", parent_mo_or_dn, **kwargs)

