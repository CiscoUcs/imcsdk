"""This module contains the general information for AdaptorFcErrorRecoveryProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AdaptorFcErrorRecoveryProfileConsts:
    pass


class AdaptorFcErrorRecoveryProfile(ManagedObject):
    """This is AdaptorFcErrorRecoveryProfile class."""

    consts = AdaptorFcErrorRecoveryProfileConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AdaptorFcErrorRecoveryProfile", "adaptorFcErrorRecoveryProfile", "fc-err-rec", VersionMeta.Version151f, "InputOutput", 0x7ff, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Get", "Set"]),
        "modular": MoMeta("AdaptorFcErrorRecoveryProfile", "adaptorFcErrorRecoveryProfile", "fc-err-rec", VersionMeta.Version2013e, "InputOutput", 0x7ff, [], ["admin", "read-only", "user"], ['adaptorHostFcIf'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "error_detect_timeout": MoPropertyMeta("error_detect_timeout", "errorDetectTimeout", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1000-100000"]),
            "fcp_error_recovery": MoPropertyMeta("fcp_error_recovery", "fcpErrorRecovery", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "io_timeout_retry": MoPropertyMeta("io_timeout_retry", "ioTimeoutRetry", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-59"]),
            "link_down_timeout": MoPropertyMeta("link_down_timeout", "linkDownTimeout", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-240000"]),
            "port_down_io_retry_count": MoPropertyMeta("port_down_io_retry_count", "portDownIoRetryCount", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-255"]),
            "port_down_timeout": MoPropertyMeta("port_down_timeout", "portDownTimeout", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["0-240000"]),
            "resource_allocation_timeout": MoPropertyMeta("resource_allocation_timeout", "resourceAllocationTimeout", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["5000-100000"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "error_detect_timeout": MoPropertyMeta("error_detect_timeout", "errorDetectTimeout", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], ["1000-100000"]),
            "fcp_error_recovery": MoPropertyMeta("fcp_error_recovery", "fcpErrorRecovery", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "io_timeout_retry": MoPropertyMeta("io_timeout_retry", "ioTimeoutRetry", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], ["1-59"]),
            "link_down_timeout": MoPropertyMeta("link_down_timeout", "linkDownTimeout", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-240000"]),
            "port_down_io_retry_count": MoPropertyMeta("port_down_io_retry_count", "portDownIoRetryCount", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-255"]),
            "port_down_timeout": MoPropertyMeta("port_down_timeout", "portDownTimeout", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], ["0-240000"]),
            "resource_allocation_timeout": MoPropertyMeta("resource_allocation_timeout", "resourceAllocationTimeout", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, [], ["5000-100000"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "errorDetectTimeout": "error_detect_timeout", 
            "fcpErrorRecovery": "fcp_error_recovery", 
            "ioTimeoutRetry": "io_timeout_retry", 
            "linkDownTimeout": "link_down_timeout", 
            "portDownIoRetryCount": "port_down_io_retry_count", 
            "portDownTimeout": "port_down_timeout", 
            "resourceAllocationTimeout": "resource_allocation_timeout", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "errorDetectTimeout": "error_detect_timeout", 
            "fcpErrorRecovery": "fcp_error_recovery", 
            "ioTimeoutRetry": "io_timeout_retry", 
            "linkDownTimeout": "link_down_timeout", 
            "portDownIoRetryCount": "port_down_io_retry_count", 
            "portDownTimeout": "port_down_timeout", 
            "resourceAllocationTimeout": "resource_allocation_timeout", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.error_detect_timeout = None
        self.fcp_error_recovery = None
        self.io_timeout_retry = None
        self.link_down_timeout = None
        self.port_down_io_retry_count = None
        self.port_down_timeout = None
        self.resource_allocation_timeout = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "AdaptorFcErrorRecoveryProfile", parent_mo_or_dn, **kwargs)

