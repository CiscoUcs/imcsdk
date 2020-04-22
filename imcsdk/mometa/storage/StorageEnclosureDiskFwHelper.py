"""This module contains the general information for StorageEnclosureDiskFwHelper ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageEnclosureDiskFwHelperConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    PROTOCOL_FTP = "ftp"
    PROTOCOL_HTTP = "http"
    PROTOCOL_NONE = "none"
    PROTOCOL_SCP = "scp"
    PROTOCOL_SFTP = "sftp"
    PROTOCOL_TFTP = "tftp"


class StorageEnclosureDiskFwHelper(ManagedObject):
    """This is StorageEnclosureDiskFwHelper class."""

    consts = StorageEnclosureDiskFwHelperConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("StorageEnclosureDiskFwHelper", "storageEnclosureDiskFwHelper", "drive-fw-update", VersionMeta.Version2013e, "InputOutput", 0x7ff, [], ["admin"], ['storageEnclosure'], [], ["Get", "Set"])
    }


    prop_meta = {

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, None, [], []),
            "remote_path": MoPropertyMeta("remote_path", "remotePath", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,128}""", [], []),
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "slot_list": MoPropertyMeta("slot_list", "slotList", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 1, 512, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, 0, 256, None, [], []),
        },

    }

    prop_map = {

        "modular": {
            "adminState": "admin_state", 
            "description": "description", 
            "dn": "dn", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remotePath": "remote_path", 
            "remoteServer": "remote_server", 
            "rn": "rn", 
            "slotList": "slot_list", 
            "status": "status", 
            "user": "user", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.description = None
        self.protocol = None
        self.pwd = None
        self.remote_path = None
        self.remote_server = None
        self.slot_list = None
        self.status = None
        self.user = None

        ManagedObject.__init__(self, "StorageEnclosureDiskFwHelper", parent_mo_or_dn, **kwargs)

