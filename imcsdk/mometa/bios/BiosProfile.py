"""This module contains the general information for BiosProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosProfileConsts:
    ADMIN_ACTION_ACTIVATE = "activate"
    ADMIN_ACTION_DELETE = "delete"
    ADMIN_ACTION_EXPORT = "export"
    BACKUP_ON_ACTIVATE_FALSE = "false"
    BACKUP_ON_ACTIVATE_NO = "no"
    BACKUP_ON_ACTIVATE_TRUE = "true"
    BACKUP_ON_ACTIVATE_YES = "yes"
    PROTOCOL_FTP = "ftp"
    PROTOCOL_HTTP = "http"
    PROTOCOL_NONE = "none"
    PROTOCOL_SCP = "scp"
    PROTOCOL_SFTP = "sftp"
    PROTOCOL_TFTP = "tftp"
    REBOOT_ON_ACTIVATE_FALSE = "false"
    REBOOT_ON_ACTIVATE_NO = "no"
    REBOOT_ON_ACTIVATE_TRUE = "true"
    REBOOT_ON_ACTIVATE_YES = "yes"


class BiosProfile(ManagedObject):
    """This is BiosProfile class."""

    consts = BiosProfileConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("BiosProfile", "biosProfile", "bios-profile-[name]", VersionMeta.Version301c, "InputOutput", 0x1fff, [], ["admin", "read-only", "user"], ['biosProfileManagement'], ['biosProfileToken'], ["Get", "Set"]),
        "modular": MoMeta("BiosProfile", "biosProfile", "bios-profile-[name]", VersionMeta.Version301c, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['biosProfileManagement'], ['biosProfileToken'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["activate", "delete", "export"], []),
            "backup_on_activate": MoPropertyMeta("backup_on_activate", "backupOnActivate", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "enabled": MoPropertyMeta("enabled", "enabled", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "reboot_on_activate": MoPropertyMeta("reboot_on_activate", "rebootOnActivate", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version301c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[^\[\]\{\}#\?\\]{1,255}""", [], []),
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x1000, 0, 255, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["activate", "delete"], []),
            "backup_on_activate": MoPropertyMeta("backup_on_activate", "backupOnActivate", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "no", "yes"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "enabled": MoPropertyMeta("enabled", "enabled", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "no", "yes"], []),
            "reboot_on_activate": MoPropertyMeta("reboot_on_activate", "rebootOnActivate", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["No", "Yes", "no", "yes"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version301c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "backupOnActivate": "backup_on_activate", 
            "dn": "dn", 
            "enabled": "enabled", 
            "rebootOnActivate": "reboot_on_activate", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "description": "description", 
            "id": "id", 
            "name": "name", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "remoteServer": "remote_server", 
            "user": "user", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "backupOnActivate": "backup_on_activate", 
            "dn": "dn", 
            "enabled": "enabled", 
            "rebootOnActivate": "reboot_on_activate", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "description": "description", 
            "id": "id", 
            "name": "name", 
        },

    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_action = None
        self.backup_on_activate = None
        self.enabled = None
        self.reboot_on_activate = None
        self.status = None
        self.child_action = None
        self.description = None
        self.id = None
        self.protocol = None
        self.pwd = None
        self.remote_file = None
        self.remote_server = None
        self.user = None

        ManagedObject.__init__(self, "BiosProfile", parent_mo_or_dn, **kwargs)

