import logging
from connection.info import imc_login, imc_logout
from imcsdk.mometa.aaa.AaaUser import AaaUser

logging.basicConfig()
log = logging.getLogger('imc')
log.setLevel(logging.DEBUG)

user_id = "4"
handle = None


def add_user():
    log.debug("add_user")
    user_mo = AaaUser(parent_mo_or_dn="sys/user-ext", id=user_id,
                      name="test_user", pwd="TestPassword1")
    handle.add_mo(user_mo, modify_present=True)


def activate_user():
    log.debug("activate_user")
    user_mo = AaaUser(parent_mo_or_dn="sys/user-ext", id=user_id,
                      account_status="active")
    handle.set_mo(user_mo)


def de_activate_user():
    log.debug("de_activate_user")
    user_mo = AaaUser(parent_mo_or_dn="sys/user-ext", id=user_id,
                      account_status="inactive")
    handle.set_mo(user_mo)


def main():
    global handle
    handle = imc_login()
    handle.set_dump_xml()

    add_user()
    activate_user()
    de_activate_user()

    imc_logout(handle)

main()
