"""This module contains the general information for BiosVfOutOfBandMgmtPort ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfOutOfBandMgmtPortConsts:
    VP_OUT_OF_BAND_MGMT_PORT_DISABLED = "Disabled"
    VP_OUT_OF_BAND_MGMT_PORT_ENABLED = "Enabled"
    _VP_OUT_OF_BAND_MGMT_PORT_DISABLED = "disabled"
    _VP_OUT_OF_BAND_MGMT_PORT_ENABLED = "enabled"
    VP_OUT_OF_BAND_MGMT_PORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfOutOfBandMgmtPort(ManagedObject):
    """This is BiosVfOutOfBandMgmtPort class."""

    consts = BiosVfOutOfBandMgmtPortConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfOutOfBandMgmtPort", "biosVfOutOfBandMgmtPort", "OoB-MgmtPort", VersionMeta.Version154, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfOutOfBandMgmtPort", "biosVfOutOfBandMgmtPort", "OoB-MgmtPort", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version154, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version154, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version154, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_out_of_band_mgmt_port": MoPropertyMeta("vp_out_of_band_mgmt_port", "vpOutOfBandMgmtPort", "string", VersionMeta.Version154, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_out_of_band_mgmt_port": MoPropertyMeta("vp_out_of_band_mgmt_port", "vpOutOfBandMgmtPort", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOutOfBandMgmtPort": "vp_out_of_band_mgmt_port", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOutOfBandMgmtPort": "vp_out_of_band_mgmt_port", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_out_of_band_mgmt_port = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfOutOfBandMgmtPort", parent_mo_or_dn, **kwargs)

