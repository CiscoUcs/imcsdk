"""This module contains the general information for BiosVfOnboardStorageSWStack ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfOnboardStorageSWStackConsts:
    VP_ONBOARD_SCUSTORAGE_SWSTACK_INTEL_RSTE = "Intel RSTe"
    VP_ONBOARD_SCUSTORAGE_SWSTACK_LSI_SW_RAID = "LSI SW RAID"
    VP_ONBOARD_SCUSTORAGE_SWSTACK_PLATFORM_DEFAULT = "platform-default"


class BiosVfOnboardStorageSWStack(ManagedObject):
    """This is BiosVfOnboardStorageSWStack class."""

    consts = BiosVfOnboardStorageSWStackConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfOnboardStorageSWStack", "biosVfOnboardStorageSWStack", "Onboard-SCU-Storage-SWStack", VersionMeta.Version151x, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfOnboardStorageSWStack", "biosVfOnboardStorageSWStack", "Onboard-SCU-Storage-SWStack", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_onboard_scu_storage_sw_stack": MoPropertyMeta("vp_onboard_scu_storage_sw_stack", "vpOnboardSCUStorageSWStack", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Intel RSTe", "LSI SW RAID", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_onboard_scu_storage_sw_stack": MoPropertyMeta("vp_onboard_scu_storage_sw_stack", "vpOnboardSCUStorageSWStack", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Intel RSTe", "LSI SW RAID", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOnboardSCUStorageSWStack": "vp_onboard_scu_storage_sw_stack", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOnboardSCUStorageSWStack": "vp_onboard_scu_storage_sw_stack", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_onboard_scu_storage_sw_stack = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfOnboardStorageSWStack", parent_mo_or_dn, **kwargs)

