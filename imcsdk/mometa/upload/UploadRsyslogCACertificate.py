"""This module contains the general information for UploadRsyslogCACertificate ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class UploadRsyslogCACertificateConsts:
    ADMIN_ACTION_CONTENT_CERT_UPLOAD = "content-cert-upload"
    ADMIN_ACTION_REMOTE_CERT_UPLOAD = "remote-cert-upload"
    PROTOCOL_FTP = "ftp"
    PROTOCOL_HTTP = "http"
    PROTOCOL_NONE = "none"
    PROTOCOL_SCP = "scp"
    PROTOCOL_SFTP = "sftp"
    PROTOCOL_TFTP = "tftp"


class UploadRsyslogCACertificate(ManagedObject):
    """This is UploadRsyslogCACertificate class."""

    consts = UploadRsyslogCACertificateConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("UploadRsyslogCACertificate", "uploadRsyslogCACertificate", "upload-rsyslog-ca-cert", VersionMeta.Version422a, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['commSyslog'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["content-cert-upload", "remote-cert-upload"], []),
            "certificate_content": MoPropertyMeta("certificate_content", "certificateContent", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version422a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,255}""", [], []),
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "select_server": MoPropertyMeta("select_server", "selectServer", "uint", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], ["0-2"]),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "upload_progress": MoPropertyMeta("upload_progress", "uploadProgress", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "upload_status": MoPropertyMeta("upload_status", "uploadStatus", "string", VersionMeta.Version422a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version422a, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "certificateContent": "certificate_content", 
            "childAction": "child_action", 
            "dn": "dn", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "remoteServer": "remote_server", 
            "rn": "rn", 
            "selectServer": "select_server", 
            "status": "status", 
            "uploadProgress": "upload_progress", 
            "uploadStatus": "upload_status", 
            "user": "user", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.certificate_content = None
        self.child_action = None
        self.protocol = None
        self.pwd = None
        self.remote_file = None
        self.remote_server = None
        self.select_server = None
        self.status = None
        self.upload_progress = None
        self.upload_status = None
        self.user = None

        ManagedObject.__init__(self, "UploadRsyslogCACertificate", parent_mo_or_dn, **kwargs)

