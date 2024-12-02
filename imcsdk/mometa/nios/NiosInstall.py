"""This module contains the general information for NiosInstall ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class NiosInstallConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    OS_BOOT_MEDIUM_NONE = "NONE"
    OS_BOOT_MEDIUM_VMEDIA = "vmedia"
    REMOTE_SHARE_TYPE_NONE = "NONE"
    REMOTE_SHARE_TYPE_SCP = "scp"
    REMOTE_SHARE_TYPE_SFTP = "sftp"
    REMOTE_SHARE_TYPE_TFTP = "tftp"
    REMOTE_SHARE_TYPE_WWW = "www"
    SCU_BOOT_MEDIUM_NONE = "NONE"
    SCU_BOOT_MEDIUM_FLEXMMC = "flexmmc"
    SCU_BOOT_MEDIUM_HTTP = "http"
    SCU_BOOT_MEDIUM_IPXE = "ipxe"
    SCU_BOOT_MEDIUM_MICROSD = "microsd"
    SCU_BOOT_MEDIUM_PXE = "pxe"
    SCU_BOOT_MEDIUM_VMEDIA = "vmedia"
    TARGET_DISK_TYPE_NONE = "NONE"
    TARGET_DISK_TYPE_DISKNAME = "diskname"
    TARGET_DISK_TYPE_FC = "fc"
    TARGET_DISK_TYPE_ISCSI = "iscsi"
    TARGET_DISK_TYPE_M2SWVDNAME = "m2swvdname"
    TARGET_DISK_TYPE_ONBOARDSATAM2SSD = "onboardsatam2ssd"
    TARGET_DISK_TYPE_PHYSICALDISK = "physicaldisk"
    TARGET_DISK_TYPE_VIRTUALDISK = "virtualdisk"
    TARGET_DISK_TYPE_VIRTUALDRIVENAME = "virtualdrivename"


class NiosInstall(ManagedObject):
    """This is NiosInstall class."""

    consts = NiosInstallConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("NiosInstall", "niosInstall", "niosinstall", VersionMeta.Version423a, "InputOutput", 0x3fff, [], ["admin"], ['osiController'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version423a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "os_boot_medium": MoPropertyMeta("os_boot_medium", "osBootMedium", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["NONE", "vmedia"], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
            "remote_share_file": MoPropertyMeta("remote_share_file", "remoteShareFile", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []),
            "remote_share_ip": MoPropertyMeta("remote_share_ip", "remoteShareIp", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, r"""((https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63})|(https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))(:([1-9]|[1-5]?[0-9]{2,4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?""", [], []),
            "remote_share_path": MoPropertyMeta("remote_share_path", "remoteSharePath", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []),
            "remote_share_type": MoPropertyMeta("remote_share_type", "remoteShareType", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["NONE", "scp", "sftp", "tftp", "www"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "scu_boot_medium": MoPropertyMeta("scu_boot_medium", "scuBootMedium", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["NONE", "flexmmc", "http", "ipxe", "microsd", "pxe", "vmedia"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "target_disk_type": MoPropertyMeta("target_disk_type", "targetDiskType", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, None, ["NONE", "diskname", "fc", "iscsi", "m2swvdname", "onboardsatam2ssd", "physicaldisk", "virtualdisk", "virtualdrivename"], []),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version423a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "osBootMedium": "os_boot_medium", 
            "password": "password", 
            "remoteShareFile": "remote_share_file", 
            "remoteShareIp": "remote_share_ip", 
            "remoteSharePath": "remote_share_path", 
            "remoteShareType": "remote_share_type", 
            "rn": "rn", 
            "scuBootMedium": "scu_boot_medium", 
            "status": "status", 
            "targetDiskType": "target_disk_type", 
            "username": "username", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.os_boot_medium = None
        self.password = None
        self.remote_share_file = None
        self.remote_share_ip = None
        self.remote_share_path = None
        self.remote_share_type = None
        self.scu_boot_medium = None
        self.status = None
        self.target_disk_type = None
        self.username = None

        ManagedObject.__init__(self, "NiosInstall", parent_mo_or_dn, **kwargs)

