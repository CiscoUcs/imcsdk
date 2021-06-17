"""This module contains the general information for OsiStart ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class OsiStartConsts:
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGERED = "triggered"
    ANSWER_FILE_SHARE_TYPE_SCP = "scp"
    ANSWER_FILE_SHARE_TYPE_SFTP = "sftp"
    ANSWER_FILE_SHARE_TYPE_TFTP = "tftp"
    ANSWER_FILE_SHARE_TYPE_WWW = "www"
    BOOT_MEDIUM_FLEXMMC = "flexmmc"
    BOOT_MEDIUM_MICROSD = "microsd"
    BOOT_MEDIUM_PXE = "pxe"
    BOOT_MEDIUM_VMEDIA = "vmedia"
    CONFIG_SHARE_TYPE_SCP = "scp"
    CONFIG_SHARE_TYPE_SFTP = "sftp"
    CONFIG_SHARE_TYPE_TFTP = "tftp"
    CONFIG_SHARE_TYPE_WWW = "www"
    ISO_SHARE_TYPE_CIFS = "cifs"
    ISO_SHARE_TYPE_NFS = "nfs"
    ISO_SHARE_TYPE_SD = "sd"
    ISO_SHARE_TYPE_WWW = "www"
    REMOTE_SHARE_TYPE_SCP = "scp"
    REMOTE_SHARE_TYPE_SFTP = "sftp"
    REMOTE_SHARE_TYPE_TFTP = "tftp"


class OsiStart(ManagedObject):
    """This is OsiStart class."""

    consts = OsiStartConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("OsiStart", "osiStart", "osiStart", VersionMeta.Version301c, "InputOutput", 0x7fffffff, [], ["admin"], ['osiController'], [], ["Get"]),
        "modular": MoMeta("OsiStart", "osiStart", "osiStart", VersionMeta.Version301c, "InputOutput", 0x7fffffff, [], ["admin"], ['osiController'], [], ["Get"])
    }


    prop_meta = {

        "classic": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "answer_file_password": MoPropertyMeta("answer_file_password", "answerFilePassword", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []),
            "answer_file_share_file": MoPropertyMeta("answer_file_share_file", "answerFileShareFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []),
            "answer_file_share_ip": MoPropertyMeta("answer_file_share_ip", "answerFileShareIp", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""((https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63})|(https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))(:([1-9]|[1-5]?[0-9]{2,4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?""", [], []),
            "answer_file_share_path": MoPropertyMeta("answer_file_share_path", "answerFileSharePath", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []),
            "answer_file_share_type": MoPropertyMeta("answer_file_share_type", "answerFileShareType", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["scp", "sftp", "tftp", "www"], []),
            "answer_file_username": MoPropertyMeta("answer_file_username", "answerFileUsername", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
            "boot_medium": MoPropertyMeta("boot_medium", "bootMedium", "string", VersionMeta.Version402c, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, ["flexmmc", "microsd", "pxe", "vmedia"], []),
            "config_share_file": MoPropertyMeta("config_share_file", "configShareFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, [], []),
            "config_share_ip": MoPropertyMeta("config_share_ip", "configShareIp", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, r"""((https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63})|(https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))(:([1-9]|[1-5]?[0-9]{2,4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?""", [], []),
            "config_share_password": MoPropertyMeta("config_share_password", "configSharePassword", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], []),
            "config_share_path": MoPropertyMeta("config_share_path", "configSharePath", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x1000, 0, 510, None, [], []),
            "config_share_type": MoPropertyMeta("config_share_type", "configShareType", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["scp", "sftp", "tftp", "www"], []),
            "config_share_username": MoPropertyMeta("config_share_username", "configShareUsername", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8000, 0, 255, None, [], []),
            "iso_share": MoPropertyMeta("iso_share", "isoShare", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10000, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,255}""", [], []),
            "iso_share_ip": MoPropertyMeta("iso_share_ip", "isoShareIp", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20000, 0, 255, r"""((https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63})|(https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))(:([1-9]|[1-5]?[0-9]{2,4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?""", [], []),
            "iso_share_type": MoPropertyMeta("iso_share_type", "isoShareType", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, ["cifs", "nfs", "sd", "www"], []),
            "mount_option": MoPropertyMeta("mount_option", "mountOption", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x100000, None, None, None, [], []),
            "remote_share_file": MoPropertyMeta("remote_share_file", "remoteShareFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x200000, 0, 510, None, [], []),
            "remote_share_ip": MoPropertyMeta("remote_share_ip", "remoteShareIp", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x400000, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []),
            "remote_share_password": MoPropertyMeta("remote_share_password", "remoteSharePassword", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x800000, None, None, None, [], []),
            "remote_share_path": MoPropertyMeta("remote_share_path", "remoteSharePath", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x1000000, 0, 510, None, [], []),
            "remote_share_type": MoPropertyMeta("remote_share_type", "remoteShareType", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2000000, None, None, None, ["scp", "sftp", "tftp"], []),
            "remote_share_username": MoPropertyMeta("remote_share_username", "remoteShareUsername", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4000000, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8000000, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10000000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "time_out": MoPropertyMeta("time_out", "timeOut", "uint", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20000000, None, None, None, [], ["30-240"]),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40000000, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "iso_share_file": MoPropertyMeta("iso_share_file", "isoShareFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "iso_share_path": MoPropertyMeta("iso_share_path", "isoSharePath", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["trigger", "triggered"], []),
            "answer_file_password": MoPropertyMeta("answer_file_password", "answerFilePassword", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []),
            "answer_file_share_file": MoPropertyMeta("answer_file_share_file", "answerFileShareFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []),
            "answer_file_share_ip": MoPropertyMeta("answer_file_share_ip", "answerFileShareIp", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""((https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))(:([1-9]|[1-5]?[0-9]{2,4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?""", [], []),
            "answer_file_share_path": MoPropertyMeta("answer_file_share_path", "answerFileSharePath", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []),
            "answer_file_share_type": MoPropertyMeta("answer_file_share_type", "answerFileShareType", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["scp", "sftp", "tftp", "www"], []),
            "answer_file_username": MoPropertyMeta("answer_file_username", "answerFileUsername", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []),
            "boot_medium": MoPropertyMeta("boot_medium", "bootMedium", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, ["microsd", "pxe", "vmedia"], []),
            "config_share_file": MoPropertyMeta("config_share_file", "configShareFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x200, 0, 510, None, [], []),
            "config_share_ip": MoPropertyMeta("config_share_ip", "configShareIp", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, r"""((https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))(:([1-9]|[1-5]?[0-9]{2,4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?""", [], []),
            "config_share_password": MoPropertyMeta("config_share_password", "configSharePassword", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], []),
            "config_share_path": MoPropertyMeta("config_share_path", "configSharePath", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x1000, 0, 510, None, [], []),
            "config_share_type": MoPropertyMeta("config_share_type", "configShareType", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2000, None, None, None, ["scp", "sftp", "tftp", "www"], []),
            "config_share_username": MoPropertyMeta("config_share_username", "configShareUsername", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4000, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8000, 0, 255, None, [], []),
            "iso_share": MoPropertyMeta("iso_share", "isoShare", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10000, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,255}""", [], []),
            "iso_share_ip": MoPropertyMeta("iso_share_ip", "isoShareIp", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20000, 0, 255, r"""((https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(https?://)?(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))(:([1-9]|[1-5]?[0-9]{2,4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?""", [], []),
            "iso_share_type": MoPropertyMeta("iso_share_type", "isoShareType", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40000, None, None, None, ["cifs", "nfs", "sd", "www"], []),
            "mount_option": MoPropertyMeta("mount_option", "mountOption", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x80000, None, None, None, [], []),
            "password": MoPropertyMeta("password", "password", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x100000, None, None, None, [], []),
            "remote_share_file": MoPropertyMeta("remote_share_file", "remoteShareFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x200000, 0, 510, None, [], []),
            "remote_share_ip": MoPropertyMeta("remote_share_ip", "remoteShareIp", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x400000, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "remote_share_password": MoPropertyMeta("remote_share_password", "remoteSharePassword", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x800000, None, None, None, [], []),
            "remote_share_path": MoPropertyMeta("remote_share_path", "remoteSharePath", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x1000000, 0, 510, None, [], []),
            "remote_share_type": MoPropertyMeta("remote_share_type", "remoteShareType", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2000000, None, None, None, ["scp", "sftp", "tftp"], []),
            "remote_share_username": MoPropertyMeta("remote_share_username", "remoteShareUsername", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4000000, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8000000, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10000000, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "time_out": MoPropertyMeta("time_out", "timeOut", "uint", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20000000, None, None, None, [], ["30-240"]),
            "username": MoPropertyMeta("username", "username", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40000000, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "iso_share_file": MoPropertyMeta("iso_share_file", "isoShareFile", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "iso_share_path": MoPropertyMeta("iso_share_path", "isoSharePath", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminState": "admin_state", 
            "answerFilePassword": "answer_file_password", 
            "answerFileShareFile": "answer_file_share_file", 
            "answerFileShareIp": "answer_file_share_ip", 
            "answerFileSharePath": "answer_file_share_path", 
            "answerFileShareType": "answer_file_share_type", 
            "answerFileUsername": "answer_file_username", 
            "bootMedium": "boot_medium", 
            "configShareFile": "config_share_file", 
            "configShareIp": "config_share_ip", 
            "configSharePassword": "config_share_password", 
            "configSharePath": "config_share_path", 
            "configShareType": "config_share_type", 
            "configShareUsername": "config_share_username", 
            "dn": "dn", 
            "isoShare": "iso_share", 
            "isoShareIp": "iso_share_ip", 
            "isoShareType": "iso_share_type", 
            "mountOption": "mount_option", 
            "password": "password", 
            "remoteShareFile": "remote_share_file", 
            "remoteShareIp": "remote_share_ip", 
            "remoteSharePassword": "remote_share_password", 
            "remoteSharePath": "remote_share_path", 
            "remoteShareType": "remote_share_type", 
            "remoteShareUsername": "remote_share_username", 
            "rn": "rn", 
            "status": "status", 
            "timeOut": "time_out", 
            "username": "username", 
            "childAction": "child_action", 
            "isoShareFile": "iso_share_file", 
            "isoSharePath": "iso_share_path", 
        },

        "modular": {
            "adminState": "admin_state", 
            "answerFilePassword": "answer_file_password", 
            "answerFileShareFile": "answer_file_share_file", 
            "answerFileShareIp": "answer_file_share_ip", 
            "answerFileSharePath": "answer_file_share_path", 
            "answerFileShareType": "answer_file_share_type", 
            "answerFileUsername": "answer_file_username", 
            "bootMedium": "boot_medium", 
            "configShareFile": "config_share_file", 
            "configShareIp": "config_share_ip", 
            "configSharePassword": "config_share_password", 
            "configSharePath": "config_share_path", 
            "configShareType": "config_share_type", 
            "configShareUsername": "config_share_username", 
            "dn": "dn", 
            "isoShare": "iso_share", 
            "isoShareIp": "iso_share_ip", 
            "isoShareType": "iso_share_type", 
            "mountOption": "mount_option", 
            "password": "password", 
            "remoteShareFile": "remote_share_file", 
            "remoteShareIp": "remote_share_ip", 
            "remoteSharePassword": "remote_share_password", 
            "remoteSharePath": "remote_share_path", 
            "remoteShareType": "remote_share_type", 
            "remoteShareUsername": "remote_share_username", 
            "rn": "rn", 
            "status": "status", 
            "timeOut": "time_out", 
            "username": "username", 
            "childAction": "child_action", 
            "isoShareFile": "iso_share_file", 
            "isoSharePath": "iso_share_path", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.answer_file_password = None
        self.answer_file_share_file = None
        self.answer_file_share_ip = None
        self.answer_file_share_path = None
        self.answer_file_share_type = None
        self.answer_file_username = None
        self.boot_medium = None
        self.config_share_file = None
        self.config_share_ip = None
        self.config_share_password = None
        self.config_share_path = None
        self.config_share_type = None
        self.config_share_username = None
        self.iso_share = None
        self.iso_share_ip = None
        self.iso_share_type = None
        self.mount_option = None
        self.password = None
        self.remote_share_file = None
        self.remote_share_ip = None
        self.remote_share_password = None
        self.remote_share_path = None
        self.remote_share_type = None
        self.remote_share_username = None
        self.status = None
        self.time_out = None
        self.username = None
        self.child_action = None
        self.iso_share_file = None
        self.iso_share_path = None

        ManagedObject.__init__(self, "OsiStart", parent_mo_or_dn, **kwargs)

