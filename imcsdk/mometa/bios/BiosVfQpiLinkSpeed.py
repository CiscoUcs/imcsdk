"""This module contains the general information for BiosVfQpiLinkSpeed ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfQpiLinkSpeedConsts:
    VP_QPI_LINK_SPEED_10_4_GT_S = "10.4GT/s"
    VP_QPI_LINK_SPEED_11_2_GT_S = "11.2GT/s"
    VP_QPI_LINK_SPEED_9_6_GT_S = "9.6GT/s"
    VP_QPI_LINK_SPEED_AUTO = "Auto"
    VP_QPI_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"


class BiosVfQpiLinkSpeed(ManagedObject):
    """This is BiosVfQpiLinkSpeed class."""

    consts = BiosVfQpiLinkSpeedConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfQpiLinkSpeed", "biosVfQpiLinkSpeed", "UPI-Link-Frequency-Select", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfQpiLinkSpeed", "biosVfQpiLinkSpeed", "UPI-Link-Frequency-Select", VersionMeta.Version412a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_qpi_link_speed": MoPropertyMeta("vp_qpi_link_speed", "vpQpiLinkSpeed", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["10.4GT/s", "11.2GT/s", "9.6GT/s", "Auto", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_qpi_link_speed": MoPropertyMeta("vp_qpi_link_speed", "vpQpiLinkSpeed", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["10.4GT/s", "9.6GT/s", "Auto", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpQpiLinkSpeed": "vp_qpi_link_speed", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpQpiLinkSpeed": "vp_qpi_link_speed", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_qpi_link_speed = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfQpiLinkSpeed", parent_mo_or_dn, **kwargs)

