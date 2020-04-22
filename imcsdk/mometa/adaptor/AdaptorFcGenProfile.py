"""This module contains the general information for AdaptorFcGenProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorFcGenProfileConsts:
    MAC_AUTO = "AUTO"
    ORDER_ANY = "ANY"
    RATE_LIMIT_OFF = "OFF"
    VHBA_TYPE_FC_INITIATOR = "fc-initiator"
    VHBA_TYPE_FC_NVME_INITIATOR = "fc-nvme-initiator"
    VHBA_TYPE_FC_NVME_TARGET = "fc-nvme-target"
    VHBA_TYPE_FC_TARGET = "fc-target"
    VLAN_NONE = "NONE"


class AdaptorFcGenProfile(ManagedObject):
    """This is AdaptorFcGenProfile class."""

    consts = AdaptorFcGenProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorFcGenProfile", "adaptorFcGenProfile", "general", VersionMeta.Version151f, "InputOutput", 0x1fff, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorFcGenProfile", "adaptorFcGenProfile", "general", VersionMeta.Version2013e, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "class_of_service": MoPropertyMeta("class_of_service", "classOfService", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[0-6]""", [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", ["AUTO"], []),
            "max_data_field_size": MoPropertyMeta("max_data_field_size", "maxDataFieldSize", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["256-2112"]),
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[0-9]|1[0-7]""", ["ANY"], []),
            "persistent_lun_bind": MoPropertyMeta("persistent_lun_bind", "persistentLunBind", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rate_limit": MoPropertyMeta("rate_limit", "rateLimit", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""(([1-9]\d?\d?\d?|10000) Mbps)""", ["OFF"], ["1-100000"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vhba_type": MoPropertyMeta("vhba_type", "vhbaType", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["fc-initiator", "fc-nvme-initiator", "fc-nvme-target", "fc-target"], []),
            "vlan": MoPropertyMeta("vlan", "vlan", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["NONE"], ["1-4094"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "pci_link": MoPropertyMeta("pci_link", "pciLink", "uint", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], ["0-1"]),
        },

        "modular": {
            "class_of_service": MoPropertyMeta("class_of_service", "classOfService", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[0-6]""", [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", ["AUTO"], []),
            "max_data_field_size": MoPropertyMeta("max_data_field_size", "maxDataFieldSize", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["256-2112"]),
            "order": MoPropertyMeta("order", "order", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[0-9]|1[0-7]""", ["ANY"], []),
            "persistent_lun_bind": MoPropertyMeta("persistent_lun_bind", "persistentLunBind", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "rate_limit": MoPropertyMeta("rate_limit", "rateLimit", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""(([1-9]\d?\d?\d?|10000) Mbps)""", ["OFF"], ["1-100000"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vhba_type": MoPropertyMeta("vhba_type", "vhbaType", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["fc-initiator", "fc-nvme-initiator", "fc-nvme-target", "fc-target"], []),
            "vlan": MoPropertyMeta("vlan", "vlan", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["NONE"], ["1-4094"]),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "pci_link": MoPropertyMeta("pci_link", "pciLink", "uint", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-1"]),
        },

    }

    prop_map = {

        "classic": {
            "classOfService": "class_of_service", 
            "dn": "dn", 
            "mac": "mac", 
            "maxDataFieldSize": "max_data_field_size", 
            "order": "order", 
            "persistentLunBind": "persistent_lun_bind", 
            "rateLimit": "rate_limit", 
            "rn": "rn", 
            "status": "status", 
            "vhbaType": "vhba_type", 
            "vlan": "vlan", 
            "childAction": "child_action", 
            "pciLink": "pci_link", 
        },

        "modular": {
            "classOfService": "class_of_service", 
            "dn": "dn", 
            "mac": "mac", 
            "maxDataFieldSize": "max_data_field_size", 
            "order": "order", 
            "persistentLunBind": "persistent_lun_bind", 
            "rateLimit": "rate_limit", 
            "rn": "rn", 
            "status": "status", 
            "vhbaType": "vhba_type", 
            "vlan": "vlan", 
            "childAction": "child_action", 
            "pciLink": "pci_link", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.class_of_service = None
        self.mac = None
        self.max_data_field_size = None
        self.order = None
        self.persistent_lun_bind = None
        self.rate_limit = None
        self.status = None
        self.vhba_type = None
        self.vlan = None
        self.child_action = None
        self.pci_link = None

        ManagedObject.__init__(self, "AdaptorFcGenProfile", parent_mo_or_dn, **kwargs)

