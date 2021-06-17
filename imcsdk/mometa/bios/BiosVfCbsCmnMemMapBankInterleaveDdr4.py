"""This module contains the general information for BiosVfCbsCmnMemMapBankInterleaveDdr4 ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnMemMapBankInterleaveDdr4Consts:
    VP_CBS_CMN_MEM_MAP_BANK_INTERLEAVE_DDR4_AUTO = "Auto"
    VP_CBS_CMN_MEM_MAP_BANK_INTERLEAVE_DDR4_DISABLED = "Disabled"
    _VP_CBS_CMN_MEM_MAP_BANK_INTERLEAVE_DDR4_DISABLED = "disabled"
    VP_CBS_CMN_MEM_MAP_BANK_INTERLEAVE_DDR4_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnMemMapBankInterleaveDdr4(ManagedObject):
    """This is BiosVfCbsCmnMemMapBankInterleaveDdr4 class."""

    consts = BiosVfCbsCmnMemMapBankInterleaveDdr4Consts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnMemMapBankInterleaveDdr4", "biosVfCbsCmnMemMapBankInterleaveDdr4", "chipset-interleave", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_mem_map_bank_interleave_ddr4": MoPropertyMeta("vp_cbs_cmn_mem_map_bank_interleave_ddr4", "vpCbsCmnMemMapBankInterleaveDdr4", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "disabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnMemMapBankInterleaveDdr4": "vp_cbs_cmn_mem_map_bank_interleave_ddr4", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_mem_map_bank_interleave_ddr4 = None

        ManagedObject.__init__(self, "BiosVfCbsCmnMemMapBankInterleaveDdr4", parent_mo_or_dn, **kwargs)

