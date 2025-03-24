
"""Class representation of a CPS configuration"""

class CPS:
    """CPS representation"""
    def __init__(self):
        """"""


class Package:
    """CPS package object"""
    def __init__(self):
        """"""

    @compat_version.setter
    def compat_version(self, val):
        self._compat_version = val

    @property
    def compat_version(self):
        return self._compat_version

    @components.setter
    def components(self, val):
        self._components = val

    @property
    def components(self):
        return self._components

    @configuration.setter
    def configuration(self, val):
        self._configuration = val

    @property
    def configuration(self):
        return self._configuration

    @configurations.setter
    def configurations(self, val):
        self._configurations = val

    @property
    def configurations(self):
        return self._configurations

    @cps_path.setter
    def cps_path(self, val):
        self._cps_path = val

    @property
    def cps_path(self):
        return self._cps_path


class Platform:
    """CPS Platform object"""
    def __init__(self):
        """"""
    @c_runtime_vendor.setter
    def c_runtime_vendor(self, val):
        self._c_runtime_vendor = val

    @property
    def c_runtime_vendor(self):
        return self._c_runtime_vendor

    @c_runtime_version.setter
    def c_runtime_version(self, val):
        self._c_runtime_version = val

    @property
    def c_runtime_version(self):
        return self._c_runtime_version

    @cpp_runtime_version.setter
    def cpp_runtime_version(self, val):
        self._cpp_runtime_version = val

    @property
    def cpp_runtime_version(self):
        return self._cpp_runtime_version

    @cpp_runtime_vendor.setter
    def cpp_runtime_vendor(self, val):
        self._cpp_runtime_vendor = val

    @property
    def cpp_runtime_vendor(self):
        return self._cpp_runtime_vendor


    @clr_vendor.setter
    def clr_vendor(self, val):
        self._clr_vendor = val

    @property
    def clr_vendor(self):
        return self._clr_vendor

    @clr_version.setter
    def clr_version(self, val):
        self._clr_version = val

    @property
    def clr_version(self):
        return self._clr_version


class Requirement:
    """CPS Requirement object"""
    def __init__(self):
        """"""

    @components.setter
    def components(self, val):
        self._components = val

    @property
    def components(self):
        return self._components


class Component:
    """CPS Component object"""
    def __init__(self):
        """"""
    @compile_features.setter
    def compile_features(self, val):
        self._compile_features = val

    @property
    def compile_features(self):
        return self._compile_features

    @compile_flags.setter
    def compile_flags(self, val):
        self._compile_flags = val

    @property
    def compile_flags(self):
        return self._compile_flags


    
class Configuration:
    """CPS Configuration object"""
    def __init__(self):
        """"""

    @compile_features.setter
    def compile_features(self, val):
        self._compile_features = val

    @property
    def compile_features(self):
        return self._compile_features

    @compile_flags.setter
    def compile_flags(self, val):
        self._compile_flags = val

    @property
    def compile_flags(self):
        return self._compile_flags



