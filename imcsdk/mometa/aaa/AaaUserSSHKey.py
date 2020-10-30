"""This module contains the general information for AaaUserSSHKey ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaUserSSHKeyConsts:
    ADMIN_ACTION_CLEAR = "clear"
    ADMIN_ACTION_CONTENT_KEY_UPLOAD = "content-key-upload"
    ADMIN_ACTION_REMOTE_KEY_UPLOAD = "remote-key-upload"
    PROTOCOL_FTP = "ftp"
    PROTOCOL_HTTP = "http"
    PROTOCOL_NONE = "none"
    PROTOCOL_SCP = "scp"
    PROTOCOL_SFTP = "sftp"
    PROTOCOL_TFTP = "tftp"


class AaaUserSSHKey(ManagedObject):
    """This is AaaUserSSHKey class."""

    consts = AaaUserSSHKeyConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("AaaUserSSHKey", "aaaUserSSHKey", "ssh-key-[id]", VersionMeta.Version412a, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['aaaUser'], [], [None]),
        "modular": MoMeta("AaaUserSSHKey", "aaaUserSSHKey", "ssh-key-[id]", VersionMeta.Version412a, "InputOutput", 0xfff, [], ["admin", "read-only", "user"], ['aaaUser'], [], [None])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear", "content-key-upload", "remote-key-upload"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version412a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-2"]),
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[^\[\]\{\}#\?\\]{1,255}""", [], []),
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "ssh_key": MoPropertyMeta("ssh_key", "sshKey", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x200, 1, 1536, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear", "content-key-upload", "remote-key-upload"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version412a, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["1-2"]),
            "protocol": MoPropertyMeta("protocol", "protocol", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[^\[\]\{\}#\?\\]{1,255}""", [], []),
            "remote_server": MoPropertyMeta("remote_server", "remoteServer", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "ssh_key": MoPropertyMeta("ssh_key", "sshKey", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x200, 1, 1536, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version412a, MoPropertyMeta.READ_WRITE, 0x800, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version412a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "id": "id", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "remoteServer": "remote_server", 
            "rn": "rn", 
            "sshKey": "ssh_key", 
            "status": "status", 
            "user": "user", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "id": "id", 
            "protocol": "protocol", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "remoteServer": "remote_server", 
            "rn": "rn", 
            "sshKey": "ssh_key", 
            "status": "status", 
            "user": "user", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_action = None
        self.protocol = None
        self.pwd = None
        self.remote_file = None
        self.remote_server = None
        self.ssh_key = None
        self.status = None
        self.user = None
        self.child_action = None

        ManagedObject.__init__(self, "AaaUserSSHKey", parent_mo_or_dn, **kwargs)

