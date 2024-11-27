"""This module contains the general information for BiosVfRuntimePostPackageRepair ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfRuntimePostPackageRepairConsts:
    VP_RUNTIME_POST_PACKAGE_REPAIR_DISABLED = "Disabled"
    VP_RUNTIME_POST_PACKAGE_REPAIR_ENABLED = "Enabled"
    _VP_RUNTIME_POST_PACKAGE_REPAIR_DISABLED = "disabled"
    _VP_RUNTIME_POST_PACKAGE_REPAIR_ENABLED = "enabled"
    VP_RUNTIME_POST_PACKAGE_REPAIR_PLATFORM_DEFAULT = "platform-default"


class BiosVfRuntimePostPackageRepair(ManagedObject):
    """This is BiosVfRuntimePostPackageRepair class."""

    consts = BiosVfRuntimePostPackageRepairConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfRuntimePostPackageRepair", "biosVfRuntimePostPackageRepair", "runtime-post-package-repair", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_runtime_post_package_repair": MoPropertyMeta("vp_runtime_post_package_repair", "vpRuntimePostPackageRepair", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpRuntimePostPackageRepair": "vp_runtime_post_package_repair", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_runtime_post_package_repair = None

        ManagedObject.__init__(self, "BiosVfRuntimePostPackageRepair", parent_mo_or_dn, **kwargs)

