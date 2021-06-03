"""This module contains the general information for MctpCertificateManagement ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MctpCertificateManagementConsts:
    FAULT_ALERT_DISABLED = "Disabled"
    FAULT_ALERT_FULL = "Full"
    FAULT_ALERT_PARTIAL = "Partial"


class MctpCertificateManagement(ManagedObject):
    """This is MctpCertificateManagement class."""

    consts = MctpCertificateManagementConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("MctpCertificateManagement", "mctpCertificateManagement", "mctp-cert-mgmt", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['topSystem'], ['endPoint', 'endPointRootCACertificate', 'uploadEndPointRootCACertificate'], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "fault_alert": MoPropertyMeta("fault_alert", "faultAlert", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["Disabled", "Full", "Partial"], []),
            "overall_spdm_status": MoPropertyMeta("overall_spdm_status", "overallSpdmStatus", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "upload_progress": MoPropertyMeta("upload_progress", "uploadProgress", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "upload_status": MoPropertyMeta("upload_status", "uploadStatus", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "faultAlert": "fault_alert", 
            "overallSpdmStatus": "overall_spdm_status", 
            "rn": "rn", 
            "status": "status", 
            "uploadProgress": "upload_progress", 
            "uploadStatus": "upload_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.fault_alert = None
        self.overall_spdm_status = None
        self.status = None
        self.upload_progress = None
        self.upload_status = None

        ManagedObject.__init__(self, "MctpCertificateManagement", parent_mo_or_dn, **kwargs)

