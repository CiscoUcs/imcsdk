"""This module contains the general information for BiosVfEpochUpdate ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfEpochUpdateConsts:
    VP_EPOCH_UPDATE_CHANGE_TO_NEW_RANDOM_OWNER_EPOCHS = "Change to New Random Owner EPOCHs"
    VP_EPOCH_UPDATE_MANUAL_USER_DEFINED_OWNER_EPOCHS = "Manual User Defined Owner EPOCHs"
    VP_EPOCH_UPDATE_SGX_OWNER_EPOCH_ACTIVATED = "SGX Owner EPOCH activated"
    VP_EPOCH_UPDATE_PLATFORM_DEFAULT = "platform-default"


class BiosVfEpochUpdate(ManagedObject):
    """This is BiosVfEpochUpdate class."""

    consts = BiosVfEpochUpdateConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfEpochUpdate", "biosVfEpochUpdate", "Epoch-Update", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_epoch_update": MoPropertyMeta("vp_epoch_update", "vpEpochUpdate", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Change to New Random Owner EPOCHs", "Manual User Defined Owner EPOCHs", "SGX Owner EPOCH activated", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEpochUpdate": "vp_epoch_update", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_epoch_update = None

        ManagedObject.__init__(self, "BiosVfEpochUpdate", parent_mo_or_dn, **kwargs)

