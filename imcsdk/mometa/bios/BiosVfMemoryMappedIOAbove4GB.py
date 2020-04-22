"""This module contains the general information for BiosVfMemoryMappedIOAbove4GB ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfMemoryMappedIOAbove4GBConsts:
    VP_MEMORY_MAPPED_IOABOVE4_GB_DISABLED = "Disabled"
    VP_MEMORY_MAPPED_IOABOVE4_GB_ENABLED = "Enabled"
    _VP_MEMORY_MAPPED_IOABOVE4_GB_DISABLED = "disabled"
    _VP_MEMORY_MAPPED_IOABOVE4_GB_ENABLED = "enabled"
    VP_MEMORY_MAPPED_IOABOVE4_GB_PLATFORM_DEFAULT = "platform-default"


class BiosVfMemoryMappedIOAbove4GB(ManagedObject):
    """This is BiosVfMemoryMappedIOAbove4GB class."""

    consts = BiosVfMemoryMappedIOAbove4GBConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfMemoryMappedIOAbove4GB", "biosVfMemoryMappedIOAbove4GB", "Memory-mapped-IO-above-4GB", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfMemoryMappedIOAbove4GB", "biosVfMemoryMappedIOAbove4GB", "Memory-mapped-IO-above-4GB", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_memory_mapped_io_above4_gb": MoPropertyMeta("vp_memory_mapped_io_above4_gb", "vpMemoryMappedIOAbove4GB", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_memory_mapped_io_above4_gb": MoPropertyMeta("vp_memory_mapped_io_above4_gb", "vpMemoryMappedIOAbove4GB", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMemoryMappedIOAbove4GB": "vp_memory_mapped_io_above4_gb", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpMemoryMappedIOAbove4GB": "vp_memory_mapped_io_above4_gb", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_memory_mapped_io_above4_gb = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfMemoryMappedIOAbove4GB", parent_mo_or_dn, **kwargs)

