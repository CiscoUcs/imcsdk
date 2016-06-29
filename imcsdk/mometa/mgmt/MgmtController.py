"""This module contains the general information for MgmtController ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MgmtControllerConsts:
    SUBJECT_ADAPTOR = "adaptor"
    SUBJECT_BLADE = "blade"
    SUBJECT_BOARD_CONTROLLER = "board-controller"
    SUBJECT_SYSTEM = "system"
    SUBJECT_UNKNOWN = "unknown"


class MgmtController(ManagedObject):
    """This is MgmtController class."""

    consts = MgmtControllerConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtController", "mgmtController", "mgmt", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'adaptorUnit', u'computeRackUnit'], [u'firmwareBootDefinition', u'firmwareRunning', u'firmwareUpdatable', u'mgmtIf', u'sysdebugMEpLog'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subject": MoPropertyMeta("subject", "subject", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "blade", "board-controller", "system", "unknown"], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "model": "model", 
        "rn": "rn", 
        "serial": "serial", 
        "status": "status", 
        "subject": "subject", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.model = None
        self.serial = None
        self.status = None
        self.subject = None
        self.vendor = None

        ManagedObject.__init__(self, "MgmtController", parent_mo_or_dn, **kwargs)

