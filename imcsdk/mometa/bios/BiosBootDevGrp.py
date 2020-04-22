"""This module contains the general information for BiosBootDevGrp ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosBootDevGrpConsts:
    TYPE_BEV_ORDER = "bev-order"
    TYPE_CD_ORDER = "cd-order"
    TYPE_FDD_ORDER = "fdd-order"
    TYPE_HDD_ORDER = "hdd-order"
    TYPE_INTERNAL_EFI_SHELL = "internal-efi-shell"
    TYPE_NETWORK_DEVICE_ORDER = "network-device-order"
    TYPE_SYSTEM_BOOT_ORDER = "system-boot-order"


class BiosBootDevGrp(ManagedObject):
    """This is BiosBootDevGrp class."""

    consts = BiosBootDevGrpConsts()
    naming_props = set(['order'])

    mo_meta = {
        "classic": MoMeta("BiosBootDevGrp", "biosBootDevGrp", "bdg-[order]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosBOT'], ['biosBootDev'], ["Get"]),
        "modular": MoMeta("BiosBootDevGrp", "biosBootDevGrp", "bdg-[order]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosBOT'], ['biosBootDev'], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bev-order", "cd-order", "fdd-order", "hdd-order", "internal-efi-shell", "network-device-order", "system-boot-order"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bev-order", "cd-order", "fdd-order", "hdd-order", "internal-efi-shell", "network-device-order", "system-boot-order"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "descr": "descr", 
            "dn": "dn", 
            "order": "order", 
            "rn": "rn", 
            "status": "status", 
            "type": "type", 
        },

        "modular": {
            "childAction": "child_action", 
            "descr": "descr", 
            "dn": "dn", 
            "order": "order", 
            "rn": "rn", 
            "status": "status", 
            "type": "type", 
        },

    }

    def __init__(self, parent_mo_or_dn, order, **kwargs):
        self._dirty_mask = 0
        self.order = order
        self.child_action = None
        self.descr = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "BiosBootDevGrp", parent_mo_or_dn, **kwargs)

