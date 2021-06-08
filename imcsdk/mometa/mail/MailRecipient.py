"""This module contains the general information for MailRecipient ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MailRecipientConsts:
    ADMIN_ACTION_CLEAR = "clear"
    ADMIN_ACTION_SEND_TEST_MAIL = "send-test-mail"
    SEVERITY_CRITICAL = "critical"
    SEVERITY_INFORMATIONAL = "informational"
    SEVERITY_MAJOR = "major"
    SEVERITY_MINOR = "minor"
    SEVERITY_WARNING = "warning"


class MailRecipient(ManagedObject):
    """This is MailRecipient class."""

    consts = MailRecipientConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("MailRecipient", "mailRecipient", "mail-recipient-[id]", VersionMeta.Version303a, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['commMailAlert'], [], ["Get", "Remove", "Set"]),
        "modular": MoMeta("MailRecipient", "mailRecipient", "mail-recipient-[id]", VersionMeta.Version303a, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['commMailAlert'], [], ["Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear", "send-test-mail"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "email": MoPropertyMeta("email", "email", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, 0, 320, r"""(([^<>\(\)\[\]\\\.,;:\s@""]+(\.[^<>\(\)\[\]\\\.,;:\s@""]+)*)|(""\.+""))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}){1,320}""", [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version303a, MoPropertyMeta.NAMING, 0x10, 1, 4, None, [], ["1-4"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "severity": MoPropertyMeta("severity", "severity", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["critical", "informational", "major", "minor", "warning"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "test_mail_status": MoPropertyMeta("test_mail_status", "testMailStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear", "send-test-mail"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "email": MoPropertyMeta("email", "email", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, 0, 64, r"""(([^<>\(\)\[\]\\\.,;:\s@""]+(\.[^<>\(\)\[\]\\\.,;:\s@""]+)*)|(""\.+""))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})""", [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version303a, MoPropertyMeta.NAMING, 0x10, 1, 4, None, [], ["1-4"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []),
            "severity": MoPropertyMeta("severity", "severity", "string", VersionMeta.Version413a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["critical", "informational", "major", "minor", "warning"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "test_mail_status": MoPropertyMeta("test_mail_status", "testMailStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "email": "email", 
            "id": "id", 
            "rn": "rn", 
            "severity": "severity", 
            "status": "status", 
            "childAction": "child_action", 
            "testMailStatus": "test_mail_status", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "email": "email", 
            "id": "id", 
            "rn": "rn", 
            "severity": "severity", 
            "status": "status", 
            "childAction": "child_action", 
            "testMailStatus": "test_mail_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_action = None
        self.email = None
        self.severity = None
        self.status = None
        self.child_action = None
        self.test_mail_status = None

        ManagedObject.__init__(self, "MailRecipient", parent_mo_or_dn, **kwargs)

