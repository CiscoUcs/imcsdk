"""This module contains the general information for BiosBootDevPrecision ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosBootDevPrecisionConsts:
    SUBTYPE_ANY = "Any"
    SUBTYPE_CIMC_MAPPED_DVD = "cimc-mapped-dvd"
    SUBTYPE_CIMC_MAPPED_HDD = "cimc-mapped-hdd"
    SUBTYPE_FLEX_FLASH = "flex-flash"
    SUBTYPE_FLEX_UTIL = "flex-util"
    SUBTYPE_FLEXMMC_MAPPED_DVD = "flexmmc-mapped-dvd"
    SUBTYPE_FLEXMMC_MAPPED_HDD = "flexmmc-mapped-hdd"
    SUBTYPE_KVM_MAPPED_DVD = "kvm-mapped-dvd"
    SUBTYPE_KVM_MAPPED_FDD = "kvm-mapped-fdd"
    SUBTYPE_KVM_MAPPED_HDD = "kvm-mapped-hdd"
    SUBTYPE_USB_CD = "usb-cd"
    SUBTYPE_USB_FDD = "usb-fdd"
    SUBTYPE_USB_HDD = "usb-hdd"
    TYPE_ = ""
    TYPE_EFI = "EFI"
    TYPE_FLEX_MMC = "FlexMMC"
    TYPE_HDD = "HDD"
    TYPE_HTTP = "HTTP"
    TYPE_ISCSI = "ISCSI"
    TYPE_NVME = "NVMe"
    TYPE_PCHSTORAGE = "PCHSTORAGE"
    TYPE_PXE = "PXE"
    TYPE_SAN = "SAN"
    TYPE_SDCARD = "SDCARD"
    TYPE_USB = "USB"
    TYPE_VMEDIA = "VMEDIA"


class BiosBootDevPrecision(ManagedObject):
    """This is BiosBootDevPrecision class."""

    consts = BiosBootDevPrecisionConsts()
    naming_props = set(['order'])

    mo_meta = {
        "classic": MoMeta("BiosBootDevPrecision", "biosBootDevPrecision", "bdvp-[order]", VersionMeta.Version201a, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosBOT'], [], ["Get"]),
        "modular": MoMeta("BiosBootDevPrecision", "biosBootDevPrecision", "bdvp-[order]", VersionMeta.Version2013e, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], ['biosBOT'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "lun": MoPropertyMeta("lun", "lun", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version201a, MoPropertyMeta.NAMING, None, None, None, None, [], ["1-255"]),
            "port": MoPropertyMeta("port", "port", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "subtype": MoPropertyMeta("subtype", "subtype", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Any", "cimc-mapped-dvd", "cimc-mapped-hdd", "flex-flash", "flex-util", "flexmmc-mapped-dvd", "flexmmc-mapped-hdd", "kvm-mapped-dvd", "kvm-mapped-fdd", "kvm-mapped-hdd", "usb-cd", "usb-fdd", "usb-hdd"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "EFI", "FlexMMC", "HDD", "HTTP", "ISCSI", "NVMe", "PCHSTORAGE", "PXE", "SAN", "SDCARD", "USB", "VMEDIA"], []),
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []),
            "lun": MoPropertyMeta("lun", "lun", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []),
            "order": MoPropertyMeta("order", "order", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, None, None, None, None, [], ["1-255"]),
            "port": MoPropertyMeta("port", "port", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []),
            "slot": MoPropertyMeta("slot", "slot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
            "subtype": MoPropertyMeta("subtype", "subtype", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cimc-mapped-dvd", "cimc-mapped-hdd", "kvm-mapped-dvd", "kvm-mapped-fdd", "kvm-mapped-hdd", "usb-cd", "usb-fdd", "usb-hdd"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "EFI", "HDD", "HTTP", "ISCSI", "NVMe", "PCHSTORAGE", "PXE", "SAN", "SDCARD", "USB", "VMEDIA"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "descr": "descr", 
            "dn": "dn", 
            "lun": "lun", 
            "name": "name", 
            "order": "order", 
            "port": "port", 
            "rn": "rn", 
            "slot": "slot", 
            "status": "status", 
            "subtype": "subtype", 
            "type": "type", 
        },

        "modular": {
            "childAction": "child_action", 
            "descr": "descr", 
            "dn": "dn", 
            "lun": "lun", 
            "name": "name", 
            "order": "order", 
            "port": "port", 
            "rn": "rn", 
            "slot": "slot", 
            "status": "status", 
            "subtype": "subtype", 
            "type": "type", 
        },

    }

    def __init__(self, parent_mo_or_dn, order, **kwargs):
        self._dirty_mask = 0
        self.order = order
        self.child_action = None
        self.descr = None
        self.lun = None
        self.name = None
        self.port = None
        self.slot = None
        self.status = None
        self.subtype = None
        self.type = None

        ManagedObject.__init__(self, "BiosBootDevPrecision", parent_mo_or_dn, **kwargs)

