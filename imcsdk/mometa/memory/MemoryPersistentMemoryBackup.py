"""This module contains the general information for MemoryPersistentMemoryBackup ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MemoryPersistentMemoryBackupConsts:
    PROTO_FTP = "ftp"
    PROTO_HTTP = "http"
    PROTO_NONE = "none"
    PROTO_SCP = "scp"
    PROTO_SFTP = "sftp"
    PROTO_TFTP = "tftp"


class MemoryPersistentMemoryBackup(ManagedObject):
    """This is MemoryPersistentMemoryBackup class."""

    consts = MemoryPersistentMemoryBackupConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("MemoryPersistentMemoryBackup", "memoryPersistentMemoryBackup", "export-config", VersionMeta.Version404b, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryConfiguration'], [], [None]),
        "modular": MoMeta("MemoryPersistentMemoryBackup", "memoryPersistentMemoryBackup", "export-config", VersionMeta.Version404b, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['memoryPersistentMemoryConfiguration'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], []),
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,255}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,255}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "hostname": "hostname", 
            "proto": "proto", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
            "childAction": "child_action", 
            "fsmDescr": "fsm_descr", 
            "fsmStatus": "fsm_status", 
        },

        "modular": {
            "dn": "dn", 
            "hostname": "hostname", 
            "proto": "proto", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
            "childAction": "child_action", 
            "fsmDescr": "fsm_descr", 
            "fsmStatus": "fsm_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.hostname = None
        self.proto = None
        self.pwd = None
        self.remote_file = None
        self.status = None
        self.user = None
        self.child_action = None
        self.fsm_descr = None
        self.fsm_status = None

        ManagedObject.__init__(self, "MemoryPersistentMemoryBackup", parent_mo_or_dn, **kwargs)

