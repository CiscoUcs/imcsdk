import logging
from connection.info import imc_login, imc_logout
from imcsdk.mometa.bios.BiosPassword import BiosPassword

logging.basicConfig()
log = logging.getLogger('imc')
log.setLevel(logging.DEBUG)

handle = None


def set_bios_password():
    bios_pass = BiosPassword(parent_mo_or_dn="", password="Nbv12345")
    handle.set_mo(bios_pass)


def main():
    global handle
    handle = imc_login()
    handle.set_dump_xml()

    set_bios_password()

    imc_logout(handle)

main()
