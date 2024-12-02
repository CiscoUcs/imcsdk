"""This module contains the general information for BiosVfErrorCheckScrub ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfErrorCheckScrubConsts:
    VP_ERROR_CHECK_SCRUB_DISABLED = "Disabled"
    VP_ERROR_CHECK_SCRUB_ENABLED_WITH_RESULT_COLLECTION = "Enabled with Result Collection"
    VP_ERROR_CHECK_SCRUB_ENABLED_WITHOUT_RESULT_COLLECTION = "Enabled without Result Collection"
    VP_ERROR_CHECK_SCRUB_PLATFORM_DEFAULT = "platform-default"


class BiosVfErrorCheckScrub(ManagedObject):
    """This is BiosVfErrorCheckScrub class."""

    consts = BiosVfErrorCheckScrubConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfErrorCheckScrub", "biosVfErrorCheckScrub", "Error-Check-Scrub", VersionMeta.Version431a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version431a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_error_check_scrub": MoPropertyMeta("vp_error_check_scrub", "vpErrorCheckScrub", "string", VersionMeta.Version431a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled with Result Collection", "Enabled without Result Collection", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpErrorCheckScrub": "vp_error_check_scrub", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_error_check_scrub = None

        ManagedObject.__init__(self, "BiosVfErrorCheckScrub", parent_mo_or_dn, **kwargs)

