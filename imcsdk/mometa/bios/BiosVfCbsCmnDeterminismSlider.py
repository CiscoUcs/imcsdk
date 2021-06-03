"""This module contains the general information for BiosVfCbsCmnDeterminismSlider ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnDeterminismSliderConsts:
    VP_CBS_CMN_DETERMINISM_SLIDER_AUTO = "Auto"
    VP_CBS_CMN_DETERMINISM_SLIDER_PERFORMANCE = "Performance"
    VP_CBS_CMN_DETERMINISM_SLIDER_POWER = "Power"
    VP_CBS_CMN_DETERMINISM_SLIDER_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnDeterminismSlider(ManagedObject):
    """This is BiosVfCbsCmnDeterminismSlider class."""

    consts = BiosVfCbsCmnDeterminismSliderConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnDeterminismSlider", "biosVfCbsCmnDeterminismSlider", "cpu-detslider", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_determinism_slider": MoPropertyMeta("vp_cbs_cmn_determinism_slider", "vpCbsCmnDeterminismSlider", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Performance", "Power", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnDeterminismSlider": "vp_cbs_cmn_determinism_slider", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_determinism_slider = None

        ManagedObject.__init__(self, "BiosVfCbsCmnDeterminismSlider", parent_mo_or_dn, **kwargs)

