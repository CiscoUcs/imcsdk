"""This module contains the general information for BiosVfProcessorC3Report ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfProcessorC3ReportConsts:
    VP_PROCESSOR_C3_REPORT_DISABLED = "Disabled"
    VP_PROCESSOR_C3_REPORT_ENABLED = "Enabled"
    _VP_PROCESSOR_C3_REPORT_DISABLED = "disabled"
    _VP_PROCESSOR_C3_REPORT_ENABLED = "enabled"
    VP_PROCESSOR_C3_REPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfProcessorC3Report(ManagedObject):
    """This is BiosVfProcessorC3Report class."""

    consts = BiosVfProcessorC3ReportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfProcessorC3Report", "biosVfProcessorC3Report", "Processor-C3-Report", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfProcessorC3Report", "biosVfProcessorC3Report", "Processor-C3-Report", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_processor_c3_report": MoPropertyMeta("vp_processor_c3_report", "vpProcessorC3Report", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_processor_c3_report": MoPropertyMeta("vp_processor_c3_report", "vpProcessorC3Report", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpProcessorC3Report": "vp_processor_c3_report", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpProcessorC3Report": "vp_processor_c3_report", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_processor_c3_report = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfProcessorC3Report", parent_mo_or_dn, **kwargs)

