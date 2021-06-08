"""This module contains the general information for BiosVfSerialPortAEnable ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSerialPortAEnableConsts:
    VP_SERIAL_PORT_AENABLE_DISABLED = "Disabled"
    VP_SERIAL_PORT_AENABLE_ENABLED = "Enabled"
    _VP_SERIAL_PORT_AENABLE_DISABLED = "disabled"
    _VP_SERIAL_PORT_AENABLE_ENABLED = "enabled"
    VP_SERIAL_PORT_AENABLE_PLATFORM_DEFAULT = "platform-default"


class BiosVfSerialPortAEnable(ManagedObject):
    """This is BiosVfSerialPortAEnable class."""

    consts = BiosVfSerialPortAEnableConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSerialPortAEnable", "biosVfSerialPortAEnable", "Serial-port-A-enable", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfSerialPortAEnable", "biosVfSerialPortAEnable", "Serial-port-A-enable", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_serial_port_a_enable": MoPropertyMeta("vp_serial_port_a_enable", "vpSerialPortAEnable", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_serial_port_a_enable": MoPropertyMeta("vp_serial_port_a_enable", "vpSerialPortAEnable", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSerialPortAEnable": "vp_serial_port_a_enable", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpSerialPortAEnable": "vp_serial_port_a_enable", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_serial_port_a_enable = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfSerialPortAEnable", parent_mo_or_dn, **kwargs)

