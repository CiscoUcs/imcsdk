"""This module contains the general information for MgmtImporterServer ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MgmtImporterServerConsts:
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    FSM_RMT_INV_ERR_CODE_ = ""
    FSM_RMT_INV_ERR_CODE_ABORTED = "Aborted"
    FSM_RMT_INV_ERR_CODE_ERROR_COLLECTING_CONFIGURATION_DATA = "Error collecting configuration data"
    FSM_RMT_INV_ERR_CODE_ERROR_IMPORTING_CONFIGURATION = "Error importing configuration"
    FSM_RMT_INV_ERR_CODE_PARTIALLY_IMPORTED = "Partially Imported"
    FSM_RMT_INV_ERR_CODE_TFTP_ERROR = "TFTP Error"
    FSM_RMT_INV_ERR_CODE_UNKNOWN_ERROR = "Unknown error"
    FSM_RMT_INV_ERR_CODE_NONE = "none"
    PROTO_FTP = "ftp"
    PROTO_HTTP = "http"
    PROTO_NONE = "none"
    PROTO_SCP = "scp"
    PROTO_SFTP = "sftp"
    PROTO_TFTP = "tftp"


class MgmtImporterServer(ManagedObject):
    """This is MgmtImporterServer class."""

    consts = MgmtImporterServerConsts()
    naming_props = set([])

    mo_meta = {
        "modular": MoMeta("MgmtImporterServer", "mgmtImporterServer", "importer-config", VersionMeta.Version2013e, "InputOutput", 0x7ff, [], ["admin", "read-only", "user"], ['computeServerNode'], [], ["Get", "Set"])
    }


    prop_meta = {

        "modular": {
            "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "entity": MoPropertyMeta("entity", "entity", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 256, None, [], []),
            "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, ["", "Aborted", "Error collecting configuration data", "Error importing configuration", "Partially Imported", "TFTP Error", "Unknown error", "none"], ["0-4294967295"]),
            "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []),
            "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|(https?://)?([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], []),
            "proto": MoPropertyMeta("proto", "proto", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], []),
            "pwd": MoPropertyMeta("pwd", "pwd", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "remote_file": MoPropertyMeta("remote_file", "remoteFile", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, 0, 255, r"""[^\[\]\{\}#&\?\\]{1,255}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user": MoPropertyMeta("user", "user", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, 0, 255, None, [], []),
        },

    }

    prop_map = {

        "modular": {
            "adminState": "admin_state", 
            "childAction": "child_action", 
            "dn": "dn", 
            "entity": "entity", 
            "fsmDescr": "fsm_descr", 
            "fsmRmtInvErrCode": "fsm_rmt_inv_err_code", 
            "fsmRmtInvErrDescr": "fsm_rmt_inv_err_descr", 
            "fsmStageDescr": "fsm_stage_descr", 
            "hostname": "hostname", 
            "proto": "proto", 
            "pwd": "pwd", 
            "remoteFile": "remote_file", 
            "rn": "rn", 
            "status": "status", 
            "user": "user", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.entity = None
        self.fsm_descr = None
        self.fsm_rmt_inv_err_code = None
        self.fsm_rmt_inv_err_descr = None
        self.fsm_stage_descr = None
        self.hostname = None
        self.proto = None
        self.pwd = None
        self.remote_file = None
        self.status = None
        self.user = None

        ManagedObject.__init__(self, "MgmtImporterServer", parent_mo_or_dn, **kwargs)

