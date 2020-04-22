"""This module contains the general information for BiosVfBootOptionNumRetry ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfBootOptionNumRetryConsts:
    VP_BOOT_OPTION_NUM_RETRY_13 = "13"
    VP_BOOT_OPTION_NUM_RETRY_5 = "5"
    VP_BOOT_OPTION_NUM_RETRY_INFINITE = "Infinite"
    VP_BOOT_OPTION_NUM_RETRY_PLATFORM_DEFAULT = "platform-default"


class BiosVfBootOptionNumRetry(ManagedObject):
    """This is BiosVfBootOptionNumRetry class."""

    consts = BiosVfBootOptionNumRetryConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfBootOptionNumRetry", "biosVfBootOptionNumRetry", "Boot-option-num-retry", VersionMeta.Version304a, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_boot_option_num_retry": MoPropertyMeta("vp_boot_option_num_retry", "vpBootOptionNumRetry", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["13", "5", "Infinite", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpBootOptionNumRetry": "vp_boot_option_num_retry", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_boot_option_num_retry = None

        ManagedObject.__init__(self, "BiosVfBootOptionNumRetry", parent_mo_or_dn, **kwargs)

