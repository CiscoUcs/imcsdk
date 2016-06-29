"""This module contains the general information for StorageLocalDiskProps ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageLocalDiskPropsConsts:
    pass


class StorageLocalDiskProps(ManagedObject):
    """This is StorageLocalDiskProps class."""

    consts = StorageLocalDiskPropsConsts()
    naming_props = set([])

    mo_meta = MoMeta("StorageLocalDiskProps", "storageLocalDiskProps", "general-props", VersionMeta.Version151f, "OutputOnly", 0xf, [], ["admin", "read-only", "user"], [u'storageController', u'storageLocalDisk'], [], ["Get"])

    prop_meta = {
        "block_count": MoPropertyMeta("block_count", "blockCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "block_size": MoPropertyMeta("block_size", "blockSize", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "boot_drive": MoPropertyMeta("boot_drive", "bootDrive", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "coerced_size": MoPropertyMeta("coerced_size", "coercedSize", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "device_id": MoPropertyMeta("device_id", "deviceId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x2, 0, 255, None, [], []), 
        "enclosure_device_id": MoPropertyMeta("enclosure_device_id", "enclosureDeviceId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "interface_type": MoPropertyMeta("interface_type", "interfaceType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "link_speed": MoPropertyMeta("link_speed", "linkSpeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "media_error_count": MoPropertyMeta("media_error_count", "mediaErrorCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "media_type": MoPropertyMeta("media_type", "mediaType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "non_coerced_size": MoPropertyMeta("non_coerced_size", "nonCoercedSize", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "other_error_count": MoPropertyMeta("other_error_count", "otherErrorCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pd_status": MoPropertyMeta("pd_status", "pdStatus", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "physical_drive": MoPropertyMeta("physical_drive", "physicalDrive", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "power_state": MoPropertyMeta("power_state", "powerState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "predictive_failure_count": MoPropertyMeta("predictive_failure_count", "predictiveFailureCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "raw_size": MoPropertyMeta("raw_size", "rawSize", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x4, 0, 255, None, [], []), 
        "sas_address0": MoPropertyMeta("sas_address0", "sasAddress0", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "sas_address1": MoPropertyMeta("sas_address1", "sasAddress1", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "sequence_number": MoPropertyMeta("sequence_number", "sequenceNumber", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
    }

    prop_map = {
        "blockCount": "block_count", 
        "blockSize": "block_size", 
        "bootDrive": "boot_drive", 
        "childAction": "child_action", 
        "coercedSize": "coerced_size", 
        "deviceId": "device_id", 
        "dn": "dn", 
        "enclosureDeviceId": "enclosure_device_id", 
        "health": "health", 
        "interfaceType": "interface_type", 
        "linkSpeed": "link_speed", 
        "mediaErrorCount": "media_error_count", 
        "mediaType": "media_type", 
        "nonCoercedSize": "non_coerced_size", 
        "otherErrorCount": "other_error_count", 
        "pdStatus": "pd_status", 
        "physicalDrive": "physical_drive", 
        "powerState": "power_state", 
        "predictiveFailureCount": "predictive_failure_count", 
        "rawSize": "raw_size", 
        "rn": "rn", 
        "sasAddress0": "sas_address0", 
        "sasAddress1": "sas_address1", 
        "sequenceNumber": "sequence_number", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.block_count = None
        self.block_size = None
        self.boot_drive = None
        self.child_action = None
        self.coerced_size = None
        self.device_id = None
        self.enclosure_device_id = None
        self.health = None
        self.interface_type = None
        self.link_speed = None
        self.media_error_count = None
        self.media_type = None
        self.non_coerced_size = None
        self.other_error_count = None
        self.pd_status = None
        self.physical_drive = None
        self.power_state = None
        self.predictive_failure_count = None
        self.raw_size = None
        self.sas_address0 = None
        self.sas_address1 = None
        self.sequence_number = None
        self.status = None

        ManagedObject.__init__(self, "StorageLocalDiskProps", parent_mo_or_dn, **kwargs)

