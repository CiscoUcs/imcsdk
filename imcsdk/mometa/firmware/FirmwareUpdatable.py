"""This module contains the general information for FirmwareUpdatable ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class FirmwareUpdatableConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    DEPLOYMENT_BACKUP = "backup"
    DEPLOYMENT_PRIMARY = "primary"
    OPER_STATE_ACTIVATING = "activating"
    OPER_STATE_BAD_IMAGE = "bad-image"
    OPER_STATE_FAILED = "failed"
    OPER_STATE_PENDING_NEXT_BOOT = "pending-next-boot"
    OPER_STATE_READY = "ready"
    OPER_STATE_REBOOTING = "rebooting"
    OPER_STATE_SCHEDULED = "scheduled"
    OPER_STATE_SET_STARTUP = "set-startup"
    OPER_STATE_THROTTLED = "throttled"
    OPER_STATE_UPDATING = "updating"
    OPER_STATE_UPGRADING = "upgrading"
    PROTOCOL_FTP = "ftp"
    PROTOCOL_HTTP = "http"
    PROTOCOL_NONE = "none"
    PROTOCOL_SCP = "scp"
    PROTOCOL_SFTP = "sftp"
    PROTOCOL_TFTP = "tftp"
    SECURE_BOOT_DISABLED = "Disabled"
    SECURE_BOOT_ENABLED = "Enabled"
    SECURE_BOOT_DISABLE = "disable"
    _SECURE_BOOT_DISABLED = "disabled"
    SECURE_BOOT_ENABLE = "enable"
    _SECURE_BOOT_ENABLED = "enabled"
    SOURCE_REMOTE = "remote"
    SOURCE_USB = "usb"
    TYPE_ADAPTOR = "adaptor"
    TYPE_BLADE_BIOS = "blade-bios"
    TYPE_BLADE_CONTROLLER = "blade-controller"
    TYPE_DEVICE_CONNECTOR = "device-connector"
    TYPE_SAS_EXPANDER = "sas-expander"
    TYPE_SIOC = "sioc"


class FirmwareUpdatable(ManagedObject):
    """This is FirmwareUpdatable class."""

    consts = FirmwareUpdatableConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("FirmwareUpdatable", "firmwareUpdatable", "fw-updatable", VersionMeta.Version151f, "InputOutput", 0x3fff, [], ["admin", "read-only", "user"], ['biosUnit', 'mgmtController', 'systemIOController'], [], ["Get"]),
        "modular": MoMeta("FirmwareUpdatable", "firmwareUpdatable", "fw-updatable", VersionMeta.Version2013e, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['biosUnit', 'mgmtController'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, None, [], []),
            "remote_path": MoPropertyMeta("remote_path", "remotePath", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,128}""", [], []),
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "secure_boot": MoPropertyMeta("secure_boot", "secureBoot", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disable", "disabled", "enable", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["adaptor", "blade-bios", "blade-controller", "device-connector", "sas-expander", "sioc"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, 0, 256, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "deployment": MoPropertyMeta("deployment", "deployment", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["backup", "primary"], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating", "upgrading"], []),
            "progress": MoPropertyMeta("progress", "progress", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "source": MoPropertyMeta("source", "source", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["remote", "usb"], []),
            "usb_path": MoPropertyMeta("usb_path", "usbPath", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x2000, 1, 128, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{0,128}""", [], []),
            "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 256, None, [], []),
            "remote_path": MoPropertyMeta("remote_path", "remotePath", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,128}""", [], []),
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, None, [], []),
            "secure_boot": MoPropertyMeta("secure_boot", "secureBoot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disable", "disabled", "enable", "enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["adaptor", "blade-bios", "blade-controller", "device-connector", "sas-expander", "sioc"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, 0, 256, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "deployment": MoPropertyMeta("deployment", "deployment", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["backup", "primary"], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating", "upgrading"], []),
            "progress": MoPropertyMeta("progress", "progress", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remotePath": "remote_path", 
            "remoteServer": "remote_server", 
            "rn": "rn", 
            "secureBoot": "secure_boot", 
            "status": "status", 
            "type": "type", 
            "user": "user", 
            "childAction": "child_action", 
            "deployment": "deployment", 
            "description": "description", 
            "operState": "oper_state", 
            "progress": "progress", 
            "source": "source", 
            "usbPath": "usb_path", 
            "version": "version", 
        },

        "modular": {
            "adminState": "admin_state", 
            "dn": "dn", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remotePath": "remote_path", 
            "remoteServer": "remote_server", 
            "rn": "rn", 
            "secureBoot": "secure_boot", 
            "status": "status", 
            "type": "type", 
            "user": "user", 
            "childAction": "child_action", 
            "deployment": "deployment", 
            "description": "description", 
            "operState": "oper_state", 
            "progress": "progress", 
            "version": "version", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.protocol = None
        self.pwd = None
        self.remote_path = None
        self.remote_server = None
        self.secure_boot = None
        self.status = None
        self.type = None
        self.user = None
        self.child_action = None
        self.deployment = None
        self.description = None
        self.oper_state = None
        self.progress = None
        self.source = None
        self.usb_path = None
        self.version = None

        ManagedObject.__init__(self, "FirmwareUpdatable", parent_mo_or_dn, **kwargs)

