"""This module contains the general information for HuuFirmwareUpdater ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class HuuFirmwareUpdaterConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    BOOT_MEDIUM_MICROSD = "microsd"
    BOOT_MEDIUM_VMEDIA = "vmedia"
    MAP_TYPE_CIFS = "cifs"
    MAP_TYPE_NFS = "nfs"
    MAP_TYPE_WWW = "www"
    UPDATE_TYPE_DELAY = "delay"
    UPDATE_TYPE_DELAY_REBOOT = "delay_reboot"
    UPDATE_TYPE_IMMEDIATE = "immediate"


class HuuFirmwareUpdater(ManagedObject):
    """This is HuuFirmwareUpdater class."""

    consts = HuuFirmwareUpdaterConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("HuuFirmwareUpdater", "huuFirmwareUpdater", "firmwareUpdater", VersionMeta.Version151f, "InputOutput", 0x3ffff, [], ["admin", "read-only", "user"], [u'huuController'], [], ["Get"]),
        "modular": MoMeta("HuuFirmwareUpdater", "huuFirmwareUpdater", "firmwareUpdater", VersionMeta.Version2013e, "InputOutput", 0x3ffff, [], ["admin", "read-only", "user"], [u'huuController'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "cimc_secure_boot": MoPropertyMeta("cimc_secure_boot", "cimcSecureBoot", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "map_type": MoPropertyMeta("map_type", "mapType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["cifs", "nfs", "www"], []), 
            "mount_option": MoPropertyMeta("mount_option", "mountOption", "string", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []), 
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []), 
            "remote_ip": MoPropertyMeta("remote_ip", "remoteIp", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []), 
            "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,255}""", [], []), 
            "remote_share_file": MoPropertyMeta("remote_share_file", "remoteShareFile", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "remote_share_path": MoPropertyMeta("remote_share_path", "remoteSharePath", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "stop_on_error": MoPropertyMeta("stop_on_error", "stopOnError", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []), 
            "time_out": MoPropertyMeta("time_out", "timeOut", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], ["30-240"]), 
            "update_component": MoPropertyMeta("update_component", "updateComponent", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, [], []), 
            "update_type": MoPropertyMeta("update_type", "updateType", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4000, 0, 510, None, ["delay", "delay_reboot", "immediate"], []), 
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], []), 
            "verify_update": MoPropertyMeta("verify_update", "verifyUpdate", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []), 
            "boot_medium": MoPropertyMeta("boot_medium", "bootMedium", "string", VersionMeta.Version311d, MoPropertyMeta.READ_WRITE, 0x20000, 0, 510, None, ["microsd", "vmedia"], []), 
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "cimc_secure_boot": MoPropertyMeta("cimc_secure_boot", "cimcSecureBoot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "no", "yes"], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "map_type": MoPropertyMeta("map_type", "mapType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["cifs", "nfs", "www"], []), 
            "mount_option": MoPropertyMeta("mount_option", "mountOption", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []), 
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], []), 
            "remote_ip": MoPropertyMeta("remote_ip", "remoteIp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, r"""([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []), 
            "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,255}""", [], []), 
            "remote_share_file": MoPropertyMeta("remote_share_file", "remoteShareFile", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "remote_share_path": MoPropertyMeta("remote_share_path", "remoteSharePath", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "stop_on_error": MoPropertyMeta("stop_on_error", "stopOnError", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["No", "Yes", "no", "yes"], []), 
            "time_out": MoPropertyMeta("time_out", "timeOut", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, [], ["30-240"]), 
            "update_component": MoPropertyMeta("update_component", "updateComponent", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, [], []), 
            "update_type": MoPropertyMeta("update_type", "updateType", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4000, 0, 510, None, ["delay", "delay_reboot", "immediate"], []), 
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], []), 
            "verify_update": MoPropertyMeta("verify_update", "verifyUpdate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, ["No", "Yes", "no", "yes"], []), 
            "cmc_secure_boot": MoPropertyMeta("cmc_secure_boot", "cmcSecureBoot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20000, None, None, None, ["No", "Yes", "no", "yes"], []), 
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "cimcSecureBoot": "cimc_secure_boot", 
            "dn": "dn", 
            "mapType": "map_type", 
            "mountOption": "mount_option", 
            "password": "password", 
            "remoteIp": "remote_ip", 
            "remoteShare": "remote_share", 
            "remoteShareFile": "remote_share_file", 
            "remoteSharePath": "remote_share_path", 
            "rn": "rn", 
            "status": "status", 
            "stopOnError": "stop_on_error", 
            "timeOut": "time_out", 
            "updateComponent": "update_component", 
            "updateType": "update_type", 
            "username": "username", 
            "verifyUpdate": "verify_update", 
            "bootMedium": "boot_medium", 
        },

        "modular": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "cimcSecureBoot": "cimc_secure_boot", 
            "dn": "dn", 
            "mapType": "map_type", 
            "mountOption": "mount_option", 
            "password": "password", 
            "remoteIp": "remote_ip", 
            "remoteShare": "remote_share", 
            "remoteShareFile": "remote_share_file", 
            "remoteSharePath": "remote_share_path", 
            "rn": "rn", 
            "status": "status", 
            "stopOnError": "stop_on_error", 
            "timeOut": "time_out", 
            "updateComponent": "update_component", 
            "updateType": "update_type", 
            "username": "username", 
            "verifyUpdate": "verify_update", 
            "cmcSecureBoot": "cmc_secure_boot", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.cimc_secure_boot = None
        self.map_type = None
        self.mount_option = None
        self.password = None
        self.remote_ip = None
        self.remote_share = None
        self.remote_share_file = None
        self.remote_share_path = None
        self.status = None
        self.stop_on_error = None
        self.time_out = None
        self.update_component = None
        self.update_type = None
        self.username = None
        self.verify_update = None
        self.boot_medium = None
        self.cmc_secure_boot = None

        ManagedObject.__init__(self, "HuuFirmwareUpdater", parent_mo_or_dn, **kwargs)

