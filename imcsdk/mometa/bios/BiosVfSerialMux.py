"""This module contains the general information for BiosVfSerialMux ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSerialMuxConsts:
    VP_SERIAL_MUX_DISABLED = "Disabled"
    VP_SERIAL_MUX_ENABLED = "Enabled"
    _VP_SERIAL_MUX_DISABLED = "disabled"
    _VP_SERIAL_MUX_ENABLED = "enabled"
    VP_SERIAL_MUX_PLATFORM_DEFAULT = "platform-default"


class BiosVfSerialMux(ManagedObject):
    """This is BiosVfSerialMux class."""

    consts = BiosVfSerialMuxConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSerialMux", "biosVfSerialMux", "serial-mux", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_serial_mux": MoPropertyMeta("vp_serial_mux", "vpSerialMux", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSerialMux": "vp_serial_mux", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_serial_mux = None

        ManagedObject.__init__(self, "BiosVfSerialMux", parent_mo_or_dn, **kwargs)

