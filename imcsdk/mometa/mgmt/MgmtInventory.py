"""This module contains the general information for MgmtInventory ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MgmtInventoryConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    PROTO_FTP = "ftp"
    PROTO_HTTP = "http"
    PROTO_NONE = "none"
    PROTO_SCP = "scp"
    PROTO_SFTP = "sftp"
    PROTO_TFTP = "tftp"


class MgmtInventory(ManagedObject):
    """This is MgmtInventory class."""

    consts = MgmtInventoryConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("MgmtInventory", "mgmtInventory", "inventory", VersionMeta.Version301c, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['topSystem'], [], [None]),
        "modular": MoMeta("MgmtInventory", "mgmtInventory", "inventory", VersionMeta.Version301c, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['equipmentChassis'], [], [None])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []),
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,255}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "progress": MoPropertyMeta("progress", "progress", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,255}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "progress": MoPropertyMeta("progress", "progress", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "hostname": "hostname", 
            "proto": "proto", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
            "childAction": "child_action", 
            "fsmStatus": "fsm_status", 
            "progress": "progress", 
        },

        "modular": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "hostname": "hostname", 
            "proto": "proto", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
            "childAction": "child_action", 
            "fsmStatus": "fsm_status", 
            "progress": "progress", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.hostname = None
        self.proto = None
        self.pwd = None
        self.remote_file = None
        self.status = None
        self.user = None
        self.child_action = None
        self.fsm_status = None
        self.progress = None

        ManagedObject.__init__(self, "MgmtInventory", parent_mo_or_dn, **kwargs)

