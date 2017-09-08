"""This module contains the general information for MailRecipient ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class MailRecipientConsts:
    ADMIN_ACTION_CLEAR = "clear"
    ADMIN_ACTION_SEND_TEST_MAIL = "send-test-mail"


class MailRecipient(ManagedObject):
    """This is MailRecipient class."""

    consts = MailRecipientConsts()
    naming_props = set([u'id'])

    mo_meta = {
        "classic": MoMeta("MailRecipient", "mailRecipient", "mail-recipient-[id]", VersionMeta.Version303a, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'commMailAlert'], [], ["Get", "Remove", "Set"]),
        "modular": MoMeta("MailRecipient", "mailRecipient", "mail-recipient-[id]", VersionMeta.Version303a, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'commMailAlert'], [], ["Get", "Remove", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear", "send-test-mail"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "email": MoPropertyMeta("email", "email", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, 0, 64, r"""(([^<>\(\)\[\]\\\.,;:\s@""]+(\.[^<>\(\)\[\]\\\.,;:\s@""]+)*)|(""\.+""))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})""", [], []), 
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version303a, MoPropertyMeta.NAMING, 0x10, 1, 4, None, [], ["1-4"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "test_mail_status": MoPropertyMeta("test_mail_status", "testMailStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear", "send-test-mail"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version303a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "email": MoPropertyMeta("email", "email", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x8, 0, 64, r"""(([^<>\(\)\[\]\\\.,;:\s@""]+(\.[^<>\(\)\[\]\\\.,;:\s@""]+)*)|(""\.+""))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})""", [], []), 
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version303a, MoPropertyMeta.NAMING, 0x10, 1, 4, None, [], ["1-4"]), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version303a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "test_mail_status": MoPropertyMeta("test_mail_status", "testMailStatus", "string", VersionMeta.Version303a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "email": "email", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
            "testMailStatus": "test_mail_status", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "email": "email", 
            "id": "id", 
            "rn": "rn", 
            "status": "status", 
            "testMailStatus": "test_mail_status", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_action = None
        self.child_action = None
        self.email = None
        self.status = None
        self.test_mail_status = None

        ManagedObject.__init__(self, "MailRecipient", parent_mo_or_dn, **kwargs)

