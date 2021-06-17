"""This module contains the general information for HuuFirmwareUpdater ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class HuuFirmwareUpdaterConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    BOOT_MEDIUM_FLEX_MMC = "FlexMMC"
    BOOT_MEDIUM_MICROSD = "microsd"
    BOOT_MEDIUM_PXEBOOT = "pxeboot"
    BOOT_MEDIUM_SD = "sd"
    BOOT_MEDIUM_VMEDIA = "vmedia"
    DO_FORCE_DOWN_NO = "no"
    DO_FORCE_DOWN_YES = "yes"
    MAP_TYPE_CIFS = "cifs"
    MAP_TYPE_EMMC = "emmc"
    MAP_TYPE_NFS = "nfs"
    MAP_TYPE_WWW = "www"
    SKIP_MEMORY_TEST_DISABLED = "Disabled"
    SKIP_MEMORY_TEST_ENABLED = "Enabled"
    UPDATE_TYPE_DELAY = "delay"
    UPDATE_TYPE_DELAY_REBOOT = "delay_reboot"
    UPDATE_TYPE_IMMEDIATE = "immediate"


class HuuFirmwareUpdater(ManagedObject):
    """This is HuuFirmwareUpdater class."""

    consts = HuuFirmwareUpdaterConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("HuuFirmwareUpdater", "huuFirmwareUpdater", "firmwareUpdater", VersionMeta.Version151f, "InputOutput", 0x1fffff, [], ["admin", "read-only", "user"], ['huuController'], [], ["Get"]),
        "modular": MoMeta("HuuFirmwareUpdater", "huuFirmwareUpdater", "firmwareUpdater", VersionMeta.Version2013e, "InputOutput", 0x1fffff, [], ["admin", "read-only", "user"], ['huuController'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "cimc_secure_boot": MoPropertyMeta("cimc_secure_boot", "cimcSecureBoot", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "do_force_down": MoPropertyMeta("do_force_down", "doForceDown", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["no", "yes"], []),
            "graceful_timeout": MoPropertyMeta("graceful_timeout", "gracefulTimeout", "uint", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-60"]),
            "map_type": MoPropertyMeta("map_type", "mapType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["cifs", "emmc", "nfs", "www"], []),
            "mount_option": MoPropertyMeta("mount_option", "mountOption", "string", VersionMeta.Version208d, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], []),
            "remote_ip": MoPropertyMeta("remote_ip", "remoteIp", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, r"""((https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63})|(https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))(:([1-9]|[1-5]?[0-9]{2,4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?""", [], []),
            "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, r"""[ !#$=%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,255}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
            "skip_memory_test": MoPropertyMeta("skip_memory_test", "skipMemoryTest", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x1000, 0, 10, None, ["Disabled", "Enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "stop_on_error": MoPropertyMeta("stop_on_error", "stopOnError", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "time_out": MoPropertyMeta("time_out", "timeOut", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], ["30-240"]),
            "update_component": MoPropertyMeta("update_component", "updateComponent", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, [], []),
            "update_type": MoPropertyMeta("update_type", "updateType", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20000, 0, 510, None, ["delay", "delay_reboot", "immediate"], []),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, [], []),
            "verify_update": MoPropertyMeta("verify_update", "verifyUpdate", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "boot_medium": MoPropertyMeta("boot_medium", "bootMedium", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x100000, 0, 510, None, ["FlexMMC", "microsd", "pxeboot", "sd", "vmedia"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "remote_share_file": MoPropertyMeta("remote_share_file", "remoteShareFile", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remote_share_path": MoPropertyMeta("remote_share_path", "remoteSharePath", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "cimc_secure_boot": MoPropertyMeta("cimc_secure_boot", "cimcSecureBoot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "no", "yes"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "do_force_down": MoPropertyMeta("do_force_down", "doForceDown", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["no", "yes"], []),
            "graceful_timeout": MoPropertyMeta("graceful_timeout", "gracefulTimeout", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-60"]),
            "map_type": MoPropertyMeta("map_type", "mapType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["cifs", "nfs", "www"], []),
            "mount_option": MoPropertyMeta("mount_option", "mountOption", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], []),
            "remote_ip": MoPropertyMeta("remote_ip", "remoteIp", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, r"""((https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))(:([1-9]|[1-5]?[0-9]{2,4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?""", [], []),
            "remote_share": MoPropertyMeta("remote_share", "remoteShare", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, 0, 510, r"""[ !#$=%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,255}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
            "skip_memory_test": MoPropertyMeta("skip_memory_test", "skipMemoryTest", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x1000, 0, 10, None, ["Disabled", "Enabled"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "stop_on_error": MoPropertyMeta("stop_on_error", "stopOnError", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, ["No", "Yes", "no", "yes"], []),
            "time_out": MoPropertyMeta("time_out", "timeOut", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8000, None, None, None, [], ["30-240"]),
            "update_component": MoPropertyMeta("update_component", "updateComponent", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10000, None, None, None, [], []),
            "update_type": MoPropertyMeta("update_type", "updateType", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20000, 0, 510, None, ["delay", "delay_reboot", "immediate"], []),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, [], []),
            "verify_update": MoPropertyMeta("verify_update", "verifyUpdate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, ["No", "Yes", "no", "yes"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "cmc_secure_boot": MoPropertyMeta("cmc_secure_boot", "cmcSecureBoot", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100000, None, None, None, ["No", "Yes", "no", "yes"], []),
            "remote_share_file": MoPropertyMeta("remote_share_file", "remoteShareFile", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "remote_share_path": MoPropertyMeta("remote_share_path", "remoteSharePath", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "cimcSecureBoot": "cimc_secure_boot", 
            "dn": "dn", 
            "doForceDown": "do_force_down", 
            "gracefulTimeout": "graceful_timeout", 
            "mapType": "map_type", 
            "mountOption": "mount_option", 
            "password": "password", 
            "remoteIp": "remote_ip", 
            "remoteShare": "remote_share", 
            "rn": "rn", 
            "skipMemoryTest": "skip_memory_test", 
            "status": "status", 
            "stopOnError": "stop_on_error", 
            "timeOut": "time_out", 
            "updateComponent": "update_component", 
            "updateType": "update_type", 
            "username": "username", 
            "verifyUpdate": "verify_update", 
            "bootMedium": "boot_medium", 
            "childAction": "child_action", 
            "remoteShareFile": "remote_share_file", 
            "remoteSharePath": "remote_share_path", 
        },

        "modular": {
            "adminState": "admin_state", 
            "cimcSecureBoot": "cimc_secure_boot", 
            "dn": "dn", 
            "doForceDown": "do_force_down", 
            "gracefulTimeout": "graceful_timeout", 
            "mapType": "map_type", 
            "mountOption": "mount_option", 
            "password": "password", 
            "remoteIp": "remote_ip", 
            "remoteShare": "remote_share", 
            "rn": "rn", 
            "skipMemoryTest": "skip_memory_test", 
            "status": "status", 
            "stopOnError": "stop_on_error", 
            "timeOut": "time_out", 
            "updateComponent": "update_component", 
            "updateType": "update_type", 
            "username": "username", 
            "verifyUpdate": "verify_update", 
            "childAction": "child_action", 
            "cmcSecureBoot": "cmc_secure_boot", 
            "remoteShareFile": "remote_share_file", 
            "remoteSharePath": "remote_share_path", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.cimc_secure_boot = None
        self.do_force_down = None
        self.graceful_timeout = None
        self.map_type = None
        self.mount_option = None
        self.password = None
        self.remote_ip = None
        self.remote_share = None
        self.skip_memory_test = None
        self.status = None
        self.stop_on_error = None
        self.time_out = None
        self.update_component = None
        self.update_type = None
        self.username = None
        self.verify_update = None
        self.boot_medium = None
        self.child_action = None
        self.remote_share_file = None
        self.remote_share_path = None
        self.cmc_secure_boot = None

        ManagedObject.__init__(self, "HuuFirmwareUpdater", parent_mo_or_dn, **kwargs)

