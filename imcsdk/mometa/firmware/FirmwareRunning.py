"""This module contains the general information for FirmwareRunning ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class FirmwareRunningConsts:
    DEPLOYMENT_BOOT_LOADER = "boot-loader"
    DEPLOYMENT_KERNEL = "kernel"
    DEPLOYMENT_SYSTEM = "system"
    DEPLOYMENT_UNSPECIFIED = "unspecified"
    TYPE_ADAPTOR = "adaptor"
    TYPE_BLADE_BIOS = "blade-bios"
    TYPE_BLADE_CONTROLLER = "blade-controller"
    TYPE_SIOC = "sioc"
    TYPE_STORAGE_CONTROLLER = "storage-controller"
    TYPE_SYSTEM = "system"
    TYPE_UNSPECIFIED = "unspecified"


class FirmwareRunning(ManagedObject):
    """This is FirmwareRunning class."""

    consts = FirmwareRunningConsts()
    naming_props = set([u'deployment'])

    mo_meta = MoMeta("FirmwareRunning", "firmwareRunning", "fw-[deployment]", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'biosUnit', u'mgmtController', u'storageController', u'systemIOController'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "deployment": MoPropertyMeta("deployment", "deployment", "string", VersionMeta.Version151f, MoPropertyMeta.NAMING, None, None, None, None, ["boot-loader", "kernel", "system", "unspecified"], []), 
        "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "blade-bios", "blade-controller", "sioc", "storage-controller", "system", "unspecified"], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "deployment": "deployment", 
        "description": "description", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, deployment, **kwargs):
        self._dirty_mask = 0
        self.deployment = deployment
        self.child_action = None
        self.description = None
        self.status = None
        self.type = None
        self.version = None

        ManagedObject.__init__(self, "FirmwareRunning", parent_mo_or_dn, **kwargs)

