"""This module contains the general information for ExportClientCertificate ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ExportClientCertificateConsts:
    PROTOCOL_FTP = "ftp"
    PROTOCOL_HTTP = "http"
    PROTOCOL_NONE = "none"
    PROTOCOL_SCP = "scp"
    PROTOCOL_SFTP = "sftp"
    PROTOCOL_TFTP = "tftp"


class ExportClientCertificate(ManagedObject):
    """This is ExportClientCertificate class."""

    consts = ExportClientCertificateConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("ExportClientCertificate", "exportClientCertificate", "kmip-client-cert-export", VersionMeta.Version302b, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], [u'kmipManagement'], [], [None]),
        "modular": MoMeta("ExportClientCertificate", "exportClientCertificate", "kmip-client-cert-export", VersionMeta.Version303a, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], [u'kmipManagement'], [], [None])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "export_progress": MoPropertyMeta("export_progress", "exportProgress", "string", VersionMeta.Version302b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "export_status": MoPropertyMeta("export_status", "exportStatus", "string", VersionMeta.Version302b, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []), 
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{0,255}""", [], []), 
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version302b, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "export_progress": MoPropertyMeta("export_progress", "exportProgress", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "export_status": MoPropertyMeta("export_status", "exportStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []), 
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{0,255}""", [], []), 
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, r"""([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "exportProgress": "export_progress", 
            "exportStatus": "export_status", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "remoteServer": "remote_server", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "exportProgress": "export_progress", 
            "exportStatus": "export_status", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "remoteServer": "remote_server", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.export_progress = None
        self.export_status = None
        self.protocol = None
        self.pwd = None
        self.remote_file = None
        self.remote_server = None
        self.status = None
        self.user = None

        ManagedObject.__init__(self, "ExportClientCertificate", parent_mo_or_dn, **kwargs)

