"""This module contains the general information for SecureLdap ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class SecureLdapConsts:
    ADMIN_ACTION_CONTENT_CERT_UPLOAD = "content-cert-upload"
    ADMIN_ACTION_REMOTE_CERT_UPLOAD = "remote-cert-upload"
    PROTOCOL_FTP = "ftp"
    PROTOCOL_HTTP = "http"
    PROTOCOL_NONE = "none"
    PROTOCOL_SCP = "scp"
    PROTOCOL_SFTP = "sftp"
    PROTOCOL_TFTP = "tftp"


class SecureLdap(ManagedObject):
    """This is SecureLdap class."""

    consts = SecureLdapConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("SecureLdap", "secureLdap", "secure-ldap", VersionMeta.Version412a, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['aaaLdap'], [], [None]),
        "modular": MoMeta("SecureLdap", "secureLdap", "secure-ldap", VersionMeta.Version412a, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['aaaLdap'], [], [None])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["content-cert-upload", "remote-cert-upload"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "certificate_content": MoPropertyMeta("certificate_content", "certificateContent", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[^\[\]\{\}#\?\\]{1,255}""", [], []),
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "download_progress": MoPropertyMeta("download_progress", "downloadProgress", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "download_status": MoPropertyMeta("download_status", "downloadStatus", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["content-cert-upload", "remote-cert-upload"], []),
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "certificate_content": MoPropertyMeta("certificate_content", "certificateContent", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[^\[\]\{\}#\?\\]{1,255}""", [], []),
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "download_progress": MoPropertyMeta("download_progress", "downloadProgress", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "download_status": MoPropertyMeta("download_status", "downloadStatus", "string", VersionMeta.Version412a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "certificateContent": "certificate_content", 
            "dn": "dn", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "remoteServer": "remote_server", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
            "childAction": "child_action", 
            "downloadProgress": "download_progress", 
            "downloadStatus": "download_status", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "adminState": "admin_state", 
            "certificateContent": "certificate_content", 
            "dn": "dn", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "remoteServer": "remote_server", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
            "childAction": "child_action", 
            "downloadProgress": "download_progress", 
            "downloadStatus": "download_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.admin_state = None
        self.certificate_content = None
        self.protocol = None
        self.pwd = None
        self.remote_file = None
        self.remote_server = None
        self.status = None
        self.user = None
        self.child_action = None
        self.download_progress = None
        self.download_status = None

        ManagedObject.__init__(self, "SecureLdap", parent_mo_or_dn, **kwargs)

