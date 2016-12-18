"""This module contains the general information for BiosVfQpiSnoopMode ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfQpiSnoopModeConsts:
    VP_QPI_SNOOP_MODE_AUTO = "auto"
    VP_QPI_SNOOP_MODE_CLUSTER_ON_DIE = "cluster-on-die"
    VP_QPI_SNOOP_MODE_EARLY_SNOOP = "early-snoop"
    VP_QPI_SNOOP_MODE_HOME_DIRECTORY_SNOOP = "home-directory-snoop"
    VP_QPI_SNOOP_MODE_HOME_DIRECTORY_SNOOP_WITH_OSB = "home-directory-snoop-with-osb"
    VP_QPI_SNOOP_MODE_HOME_SNOOP = "home-snoop"
    VP_QPI_SNOOP_MODE_PLATFORM_DEFAULT = "platform-default"


class BiosVfQpiSnoopMode(ManagedObject):
    """This is BiosVfQpiSnoopMode class."""

    consts = BiosVfQpiSnoopModeConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfQpiSnoopMode", "biosVfQpiSnoopMode", "QPI-Snoop-Mode", VersionMeta.Version204c, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfQpiSnoopMode", "biosVfQpiSnoopMode", "QPI-Snoop-Mode", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_qpi_snoop_mode": MoPropertyMeta("vp_qpi_snoop_mode", "vpQpiSnoopMode", "string", VersionMeta.Version204c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["auto", "cluster-on-die", "early-snoop", "home-directory-snoop", "home-directory-snoop-with-osb", "home-snoop", "platform-default"], []), 
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_qpi_snoop_mode": MoPropertyMeta("vp_qpi_snoop_mode", "vpQpiSnoopMode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["auto", "cluster-on-die", "early-snoop", "home-directory-snoop", "home-directory-snoop-with-osb", "home-snoop", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpQpiSnoopMode": "vp_qpi_snoop_mode", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpQpiSnoopMode": "vp_qpi_snoop_mode", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_qpi_snoop_mode = None

        ManagedObject.__init__(self, "BiosVfQpiSnoopMode", parent_mo_or_dn, **kwargs)

