"""This module contains the general information for EnableSecuredRsyslog ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class EnableSecuredRsyslogConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"


class EnableSecuredRsyslog(ManagedObject):
    """This is EnableSecuredRsyslog class."""

    consts = EnableSecuredRsyslogConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("EnableSecuredRsyslog", "enableSecuredRsyslog", "enableSecuredRsyslog", VersionMeta.Version422a, "InputOutput", 0x3f, [], ["admin", "read-only", "user"], ['commSyslog'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version422a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "select_server": MoPropertyMeta("select_server", "selectServer", "uint", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["0-2"]),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "selectServer": "select_server", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.select_server = None
        self.status = None

        ManagedObject.__init__(self, "EnableSecuredRsyslog", parent_mo_or_dn, **kwargs)

