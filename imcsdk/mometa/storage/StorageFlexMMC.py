"""This module contains the general information for StorageFlexMMC ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageFlexMMCConsts:
    ADMIN_ACTION_RESET_TO_DEFAULT = "reset-to-default"


class StorageFlexMMC(ManagedObject):
    """This is StorageFlexMMC class."""

    consts = StorageFlexMMCConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("StorageFlexMMC", "storageFlexMMC", "storage-flexmmc", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeBoard'], ['storageFlexMMCDownloadFile', 'storageFlexMMCFile'], [None]),
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["reset-to-default"], []),
            "available_storage_for_imc_images": MoPropertyMeta("available_storage_for_imc_images", "availableStorageForIMCImages", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 256, None, [], []),
            "available_storage_for_user_files": MoPropertyMeta("available_storage_for_user_files", "availableStorageForUserFiles", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 256, None, [], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "total_storage_for_imc_images": MoPropertyMeta("total_storage_for_imc_images", "totalStorageForIMCImages", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 256, None, [], []),
            "total_storage_for_user_files": MoPropertyMeta("total_storage_for_user_files", "totalStorageForUserFiles", "string", VersionMeta.Version421a, MoPropertyMeta.READ_ONLY, None, 1, 256, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "availableStorageForIMCImages": "available_storage_for_imc_images", 
            "availableStorageForUserFiles": "available_storage_for_user_files", 
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "totalStorageForIMCImages": "total_storage_for_imc_images", 
            "totalStorageForUserFiles": "total_storage_for_user_files", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.available_storage_for_imc_images = None
        self.available_storage_for_user_files = None
        self.child_action = None
        self.status = None
        self.total_storage_for_imc_images = None
        self.total_storage_for_user_files = None

        ManagedObject.__init__(self, "StorageFlexMMC", parent_mo_or_dn, **kwargs)

