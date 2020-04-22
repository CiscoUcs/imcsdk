"""This module contains the general information for BiosVfIOHResource ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfIOHResourceConsts:
    VP_IOHRESOURCE_IOH0_24K_IOH1_40K = "IOH0 24k IOH1 40k"
    VP_IOHRESOURCE_IOH0_32K_IOH1_32K = "IOH0 32k IOH1 32k"
    VP_IOHRESOURCE_IOH0_40K_IOH1_24K = "IOH0 40k IOH1 24k"
    VP_IOHRESOURCE_IOH0_48K_IOH1_16K = "IOH0 48k IOH1 16k"
    VP_IOHRESOURCE_IOH0_56K_IOH1_8K = "IOH0 56k IOH1 8k"
    VP_IOHRESOURCE_PLATFORM_DEFAULT = "platform-default"


class BiosVfIOHResource(ManagedObject):
    """This is BiosVfIOHResource class."""

    consts = BiosVfIOHResourceConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfIOHResource", "biosVfIOHResource", "ioh-resource", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfIOHResource", "biosVfIOHResource", "ioh-resource", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_ioh_resource": MoPropertyMeta("vp_ioh_resource", "vpIOHResource", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["IOH0 24k IOH1 40k", "IOH0 32k IOH1 32k", "IOH0 40k IOH1 24k", "IOH0 48k IOH1 16k", "IOH0 56k IOH1 8k", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_ioh_resource": MoPropertyMeta("vp_ioh_resource", "vpIOHResource", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["IOH0 24k IOH1 40k", "IOH0 32k IOH1 32k", "IOH0 40k IOH1 24k", "IOH0 48k IOH1 16k", "IOH0 56k IOH1 8k", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIOHResource": "vp_ioh_resource", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIOHResource": "vp_ioh_resource", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_ioh_resource = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfIOHResource", parent_mo_or_dn, **kwargs)

