"""This module contains the general information for BiosVfCbsDfCmnAcpiSratL3Numa ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsDfCmnAcpiSratL3NumaConsts:
    VP_CBS_DF_CMN_ACPI_SRAT_L3_NUMA_AUTO = "Auto"
    VP_CBS_DF_CMN_ACPI_SRAT_L3_NUMA_DISABLED = "Disabled"
    VP_CBS_DF_CMN_ACPI_SRAT_L3_NUMA_ENABLED = "Enabled"
    _VP_CBS_DF_CMN_ACPI_SRAT_L3_NUMA_DISABLED = "disabled"
    _VP_CBS_DF_CMN_ACPI_SRAT_L3_NUMA_ENABLED = "enabled"
    VP_CBS_DF_CMN_ACPI_SRAT_L3_NUMA_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsDfCmnAcpiSratL3Numa(ManagedObject):
    """This is BiosVfCbsDfCmnAcpiSratL3Numa class."""

    consts = BiosVfCbsDfCmnAcpiSratL3NumaConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsDfCmnAcpiSratL3Numa", "biosVfCbsDfCmnAcpiSratL3Numa", "strat-l3-numa", VersionMeta.Version421a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_df_cmn_acpi_srat_l3_numa": MoPropertyMeta("vp_cbs_df_cmn_acpi_srat_l3_numa", "vpCbsDfCmnAcpiSratL3Numa", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsDfCmnAcpiSratL3Numa": "vp_cbs_df_cmn_acpi_srat_l3_numa", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_df_cmn_acpi_srat_l3_numa = None

        ManagedObject.__init__(self, "BiosVfCbsDfCmnAcpiSratL3Numa", parent_mo_or_dn, **kwargs)

