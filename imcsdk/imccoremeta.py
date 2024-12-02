# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains all the base classes for the Meta.
"""

import re
import logging

log = logging.getLogger('imc')


class WriteXmlOption(object):
    """Class used as enum."""
    ALL = 0
    ALL_CONFIG = 1
    DIRTY = 2


class ImcVersion(object):
    """
    This class handles the operations related to the ImcVersions.
    It provides the functionality to compare Imc version objects.

    Attributes:
        * version (str): version string
    """

    def __init__(self, version):
        if version is None:
            return None

        self.__version = version
        self.__major = None
        self.__minor = None
        self.__mr = None
        self.__patch = None
        self.__spin = None

        match_pattern = re.compile("^(?P<major>[1-9][0-9]{0,2})\."
                                   "(?P<minor>(([0-9])|([1-9][0-9]{0,1})))\("
                                   "(?P<mr>(([0-9])|([1-9][0-9]{0,2})))\."
                                   "(?P<patch>(([0-9])|([1-9][0-9]{0,4})))\)$")
        match_obj = re.match(match_pattern, version)
        if self._set_versions(match_obj):
            return

        match_pattern = re.compile("^(?P<major>[1-9][0-9]{0,2})\."
                                   "(?P<minor>(([0-9])|([1-9][0-9]{0,1})))\("
                                   "(?P<mr>(([0-9])|([1-9][0-9]{0,2})))"
                                   "(?P<patch>[a-z])\)$")
        match_obj = re.match(match_pattern, version)
        if self._set_versions(match_obj):
            return

        match_pattern = re.compile("^(?P<major>[1-9][0-9]{0,2})\."
                                   "(?P<minor>(([0-9])|([1-9][0-9]{0,1})))\("
                                   "(?P<mr>(([0-9])|([1-9][0-9]{0,2})))\)$")
        match_obj = re.match(match_pattern, version)
        if self._set_versions(match_obj):
            return

        # handle spin builds "2.0(13aS1))"
        match_pattern = re.compile("^(?P<major>[1-9][0-9]{0,2})\."
                                   "(?P<minor>(([0-9])|([1-9][0-9]{0,1})))\("
                                   "(?P<mr>(([0-9])|([1-9][0-9]{0,2})))"
                                   "(?P<patch>[a-z])"
                                   "(?P<spin>S[1-9][0-9]{0,2})\)$")
        match_obj = re.match(match_pattern, version)
        if self._set_versions(match_obj):
            return

        # handle spin builds "3.0(1S10))"
        match_pattern = re.compile("^(?P<major>[1-9][0-9]{0,2})\."
                                   "(?P<minor>(([0-9])|([1-9][0-9]{0,1})))\("
                                   "(?P<mr>(([0-9])|([1-9][0-9]{0,2})))"
                                   "(?P<spin>S[1-9][0-9]{0,2})\)$")
        match_obj = re.match(match_pattern, version)
        if self._set_versions(match_obj):
            return

        # handle spin builds "4.2(1.2021052301)"
        match_pattern = re.compile("^(?P<major>[1-9][0-9]{0,2})\."
                                   "(?P<minor>(([0-9])|([1-9][0-9]{0,1})))\("
                                   "(?P<mr>(([0-9])|([1-9][0-9]{0,2})))\."
                                   "(?P<spin>\d{0,4}\d{0,2}\d{0,2}\d{0,2})\)$")
        match_obj = re.match(match_pattern, version)
        if self._set_versions(match_obj):
            return

        # handle patch spin builds "4.2(1a.2021052301)"
        match_pattern = re.compile("^(?P<major>[1-9][0-9]{0,2})\."
                                   "(?P<minor>(([0-9])|([1-9][0-9]{0,1})))\("
                                   "(?P<mr>(([0-9])|([1-9][0-9]{0,2})))"
                                   "(?P<patch>[a-z])\."
                                   "(?P<spin>\d{0,4}\d{0,2}\d{0,2}\d{0,2})\)$")
        match_obj = re.match(match_pattern, version)
        if self._set_versions(match_obj):
            return

    def _set_versions(self, match_obj):
        if not match_obj:
            return False

        match_dict = match_obj.groupdict()
        self.__major = match_dict.get("major")
        self.__minor = match_dict.get("minor")
        self.__mr = match_dict.get("mr")
        self.__patch = match_dict.get("patch")
        self.__spin = match_dict.get("spin")

        # Starting LB release, Spin builds only are released.
        # Spin builds version is not converted to patch build version, hence there is no need of
        # handling of patch none values or spin none values while processing version.
        # Patch and Spin will now be used in comparision function, and none values are handled accordingly.
        # For this reason, below code is being commented out.
        # if self.__patch is None:
        #     self.__patch = 'z'
        # elif self.__patch.isdigit() and self.__mr.isdigit():
        #     log.debug("Interim version encountered: %s. MR version has been bumped up." % self.version)
        #     self.__mr = str(int(self.__mr) + 1)
        #     self.__patch = 'a'
        # elif self.__patch.isalpha() and self.__spin:
        #     log.debug("Interim version encountered: %s. patch version has been bumped up." % self.version)
        #     self.__patch = str(chr(ord(self.__patch)+1))
        return True

    @property
    def major(self):
        """Getter Method of ImcVersion Class"""
        return self.__major

    @property
    def minor(self):
        """Getter Method of ImcVersion Class"""
        return self.__minor

    @property
    def mr(self):
        """Getter Method of ImcVersion Class"""
        return self.__mr

    @property
    def patch(self):
        """Getter Method of ImcVersion Class"""
        return self.__patch

    @property
    def spin(self):
        """Getter Method of ImcVersion Class"""
        return self.__spin

    @property
    def version(self):
        """Getter Method of UcsVersion Class"""
        return self.__version

    def _compare(self, version1, version2):
        if version1 == version2:
            return 0
        if not version1:
            return -1
        if not version2:
            return 1

        func = (ord, int)[version1.isdigit() and version2.isdigit()]
        return func(version1) - func(version2)

    def compare_to(self, version):
        """Method to compare Imc Version."""
        if version is None or not isinstance(version, ImcVersion):
            return 1

        ret = 0

        # From LB release spin builds are processed.
        # Hence spin comparision needs to be included
        versions = [(self.__major, version.major),
                    (self.__minor, version.minor),
                    (self.__mr, version.mr)]
        for item in versions:
            ret = self._compare(item[0], item[1])
            if ret:
                # If major, minor or mr are not equal then return from here only, further check not required.
                return ret
        # Compare Patch if patch available in both.
        if self.__patch and version.patch:
            if self.__patch == version.patch:
                ret = 0
                # If patch is also same, then nightly builds [4.0(234bS3)] have patch and spin both
                # So in that case compare spin as well.
                # This comparison is actually not required
                # (as nightly builds are not released, and are for internal purpose only)
                # but for completeness we are adding this.
                if self.__spin and version.spin:
                    ret = self._compare(self.__spin, version.spin)
                elif self.__spin:
                    ret = 1
                elif version.spin:
                    ret = -1
            elif self.__patch < version.patch:
                ret = -1
            else:
                ret = 1
        elif self.__spin and version.spin:
            # compare spin if spin available in both.
            ret = self._compare(self.__spin, version.spin)
        elif (not self.__patch and self.__spin) and (version.patch and not version.spin):
            # if spin available in self, and patch available in version, then consider self as greater.
            # We consider spin builds as greater than patch builds, as spin builds started from LB release.
            ret = 1
        elif (self.__patch and not self.__spin) and (not version.patch and version.spin):
            # if spin available in version, and patch available in self, then consider version as greater.
            # We consider spin builds as greater than patch builds, as spin builds started from LB release.
            ret = -1
        elif not self.__spin and version.spin:
            # If we reached here, then there is no patch, and only one have spin, consider that as greater.
            ret = 1
        elif self.__spin and not version.spin:
            # If we reached here, then there is no patch, and only one have spin, consider that as greater.
            ret = -1

        return ret

    def __gt__(self, version):
        return self.compare_to(version) > 0

    def __lt__(self, version):
        return self.compare_to(version) < 0

    def __ge__(self, version):
        return self.compare_to(version) >= 0

    def __le__(self, version):
        return self.compare_to(version) <= 0

    def __eq__(self, version):
        return self.compare_to(version) == 0

    def __str__(self):
        return self.__version


class MoPropertyRestriction(object):
    """
    This class handles the restriction information of the properties
    of managed object.
    """

    def __init__(self, min_length=None, max_length=None, pattern=None,
                 value_set=None, range_val=None):
        self.__min_length = min_length
        self.__max_length = max_length
        self.__pattern = pattern
        self.__range_val = range_val
        self.__value_set = value_set
        self.__range_roc = None
        self.__value_set_roc = None

    @property
    def min_length(self):
        """Getter Method of MoPropertyRestriction Class"""
        return self.__min_length

    @property
    def max_length(self):
        """Getter Method of MoPropertyRestriction Class"""
        return self.__max_length

    @property
    def pattern(self):
        """Getter Method of MoPropertyRestriction Class"""
        return self.__pattern

    @property
    def range_val(self):
        """Getter Method of MoPropertyRestriction Class"""
        return self.__range_val

    @property
    def value_set(self):
        """Getter Method of MoPropertyRestriction Class"""
        return self.__value_set

    @property
    def range_roc(self):
        """Getter Method of MoPropertyRestriction Class"""
        return self.__range_roc

    @property
    def value_set_roc(self):
        """Getter Method of MoPropertyRestriction Class"""
        return self.__value_set_roc


class MoPropertyMeta(object):
    """
    This class handles the meta information of the properties of managed
    Object.
    """

    NAMING = 0
    CREATE_ONLY = 1
    READ_ONLY = 2
    READ_WRITE = 3
    INTERNAL = 4

    def __init__(self, name, xml_attribute, field_type, version, access, mask,
                 min_length, max_length, pattern,
                 value_set, range_val):
        self.__name = name
        self.__xml_attribute = xml_attribute
        self.__field_type = field_type
        self.__version = version
        self.__access = access
        self.__mask = mask
        self.__restriction = MoPropertyRestriction(min_length, max_length,
                                                   pattern, value_set,
                                                   range_val)

    @property
    def name(self):
        """Getter Method of MoPropertyMeta Class"""
        return self.__name

    @property
    def xml_attribute(self):
        """Getter Method of MoPropertyMeta Class"""
        return self.__xml_attribute

    @property
    def field_type(self):
        """Getter Method of MoPropertyMeta Class"""
        return self.__field_type

    @property
    def version(self):
        """Getter Method of MoPropertyMeta Class"""
        return self.__version

    @property
    def access(self):
        """Getter Method of MoPropertyMeta Class"""
        return self.__access

    @property
    def mask(self):
        """Getter Method of MoPropertyMeta Class"""
        return self.__mask

    @property
    def restriction(self):
        """Getter Method of MoPropertyMeta Class"""
        return self.__restriction

    def validate_property_value(self, input_value):
        """validate property value of mo."""
        error_msg = None

        if input_value is None:
            log.debug("<%s> Value should not be None" % self.name)
            return False, error_msg

        if self.__restriction.min_length:
            if len(input_value) >= self.__restriction.min_length:
                return True, error_msg
            else:
                error_msg = (str(self.name) +
                             " minimum character should be  " +
                             str(self.__restriction.min_length))

        if self.__restriction.max_length:
            if len(input_value) <= self.__restriction.max_length:
                return True, error_msg
            else:
                error_msg = (str(self.name) + " maximum character should be " +
                             str(self.__restriction.max_length))

        if self.__restriction.range_val and str(input_value).isdigit() \
                and len(self.__restriction.range_val) > 0:
            fits_in_range = False
            value = int(input_value)
            for rest_range in self.__restriction.range_val:
                match = re.match(
                    r"""^(?P<min>[0-9]{1,})\-(?P<max>[0-9]{1,})$""",
                    rest_range, 0)
                if match:
                    min_ = int(match.group("min"))
                    max_ = int(match.group("max"))
                else:
                    continue

                if min_ <= value and max_ >= value:
                    fits_in_range = True
                    break
            if fits_in_range:
                return True, error_msg
            else:
                error_msg = ("Value " + str(value) +
                             " does not fit the range" +
                             str(self.__restriction.range_val))

        if self.__restriction.pattern and self.__restriction.value_set:
            pattern = "^" + str(self.__restriction.pattern) + "%s%s$" % (
                '|' if self.__restriction.value_set else '',
                '|'.join(['('+x+')' for x in self.__restriction.value_set]))
            match = re.match(pattern, input_value, 0)
            if match:
                return True, error_msg
            else:
                error_msg = (str(self.name) + " should adhere to regex " +
                             str(pattern))
        elif self.__restriction.pattern:
            pattern = "^" + self.__restriction.pattern + "$"
            match = re.match(pattern, input_value, 0)
            if match:
                return True, error_msg
            else:
                error_msg = (str(self.name) + " should adhere to regex " +
                             str(pattern))
        elif self.__restriction.value_set \
                and len(self.__restriction.value_set) > 0:
            if input_value in self.__restriction.value_set:
                return True, error_msg
            else:
                error_msg = (str(self.name) + " valid values are " +
                             str(self.__restriction.value_set))

        if self.field_type == "uint" and \
            self.__restriction.range_val and \
            len(self.__restriction.range_val) > 0:
            if not str(input_value).isdigit():
                error_msg = ("Value " + str(input_value) +
                             " does not fit the range " +
                             str(self.__restriction.range_val))
        if error_msg:
            # log.debug(error_msg)
            return False, error_msg
        return True, error_msg

    def __str__(self):
        """
        Method to return string representation.
        """

        access_dict = {0: "NAMING",
                       1: "CREATE_ONLY",
                       2: "READ_ONLY",
                       3: "READ_WRITE",
                       4: "INTERNAL"}

        ts = 8
        out_str = "\n"
        out_str += "Property".ljust(ts * 4) + str(self.name) + "\n"
        out_str += ("-" * len("Property")).ljust(ts * 4) + "-" * len(
            self.name) + "\n"
        out_str += str("xml_attribute").ljust(ts * 4) + ':' + str(
            self.xml_attribute) + "\n"
        out_str += str("field_type").ljust(ts * 4) + ':' + str(
            self.field_type) + "\n"
        out_str += str("min_version").ljust(ts * 4) + ':' + str(
            self.version) + "\n"
        out_str += str("access").ljust(ts * 4) + ':' + str(
            access_dict[self.access]) + "\n"
        out_str += str("min_length").ljust(ts * 4) + ':' + str(
            self.restriction.min_length) + "\n"
        out_str += str("max_length").ljust(ts * 4) + ':' + str(
            self.restriction.max_length) + "\n"
        out_str += str("pattern").ljust(ts * 4) + ':' + str(
            self.restriction.pattern) + "\n"
        out_str += str("value_set").ljust(ts * 4) + ':' + str(
            self.restriction.value_set) + "\n"
        out_str += str("range_val").ljust(ts * 4) + ':' + str(
            self.restriction.range_val)
        return out_str


class MoMeta(object):
    """
    This class handles the meta information of the managed Object.
    """

    ACCESS_TYPE_IO = "InputOutput"
    ACCESS_TYPE_OUTPUTONLY = "OutputOnly"

    def __init__(self, name, xml_attribute, rn, version, inp_out, mask,
                 field_names, access, parents, children, verbs):
        self.__name = name
        self.__xml_attribute = xml_attribute
        self.__rn = rn
        self.__version = version
        self.__inp_out = inp_out
        self.__mask = mask
        self.__field_names = field_names
        self.__access = access
        self.__children = children
        self.__parents = parents
        self.__verbs = verbs

    @property
    def name(self):
        """Getter Method of MoMeta Class"""
        return self.__name

    @property
    def xml_attribute(self):
        """Getter Method of MoMeta Class"""
        return self.__xml_attribute

    @property
    def rn(self):
        """Getter Method of MoMeta Class"""
        return self.__rn

    @property
    def version(self):
        """Getter Method of MoMeta Class"""
        return self.__version

    @property
    def inp_out(self):
        """Getter Method of MoMeta Class"""
        return self.__inp_out

    @property
    def mask(self):
        """Getter Method of MoMeta Class"""
        return self.__mask

    @property
    def field_names(self):
        """Getter Method of MoMeta Class"""
        return self.__field_names

    @property
    def access(self):
        """Getter Method of MoMeta Class"""
        return self.__access

    @property
    def children(self):
        """Getter Method of MoMeta Class"""
        return self.__children

    @property
    def parents(self):
        """Getter Method of MoMeta Class"""
        return self.__parents

    @property
    def verbs(self):
        """Getter Method of MoMeta Class"""
        return self.__verbs


class MethodPropertyMeta(object):
    """
    This class handles the meta information of the properties of
    external method Object.
    """

    def __init__(self, name, xml_attribute, field_type, version, inp_out,
                 is_complex_type):
        self.__name = name
        self.__xml_attribute = xml_attribute
        self.__field_type = field_type
        self.__version = version
        self.__inp_out = inp_out
        self.__is_complex_type = is_complex_type

    @property
    def name(self):
        """Getter Method of MethodPropertyMeta Class"""
        return self.name

    @property
    def xml_attribute(self):
        """Getter Method of MethodPropertyMeta Class"""
        return self.__xml_attribute

    @property
    def field_type(self):
        """Getter Method of MethodPropertyMeta Class"""
        return self.__field_type

    @property
    def version(self):
        """Getter Method of MethodPropertyMeta Class"""
        return self.__version

    @property
    def inp_out(self):
        """Getter Method of MethodPropertyMeta Class"""
        return self.__inp_out

    @property
    def is_complex_type(self):
        """Getter Method of MethodPropertyMeta Class"""
        return self.__is_complex_type


class MethodMeta(object):
    """
    This class handles the meta information of the meta property of
    external method Object.
    """

    def __init__(self, name, xml_attribute, version):
        self.__name = name
        self.__xml_attribute = xml_attribute
        self.__version = version

    @property
    def name(self):
        """Getter Method of MethodMeta Class"""
        return self.__name

    @property
    def xml_attribute(self):
        """Getter Method of MethodMeta Class"""
        return self.__xml_attribute

    @property
    def version(self):
        """Getter Method of MethodMeta Class"""
        return self.__version
