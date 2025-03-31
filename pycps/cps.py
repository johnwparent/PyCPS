
import typing
import pathlib

"""Class representation of a CPS configuration"""

class CPS:
    """CPS representation"""
    def __init__(self):
        """"""


class Package:
    """CPS Package object

    The Package is the root of the CPS Specification
    denoting the package the file is describing
    """
    def __init__(
            self,
            *,
            compat_version=None,
            components=None,
            configuration=None,
            cps_path=None
        ):
        """"""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, val):
        self._platform = val

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, val):
        self._prefix = val

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, val):
        self._version = val

    @property
    def version_scheme(self):
        return self._version_scheme

    @version_scheme.setter
    def version_scheme(self, val):
        self._version_scheme = val

    @property
    def compat_version(self):
        return self._compat_version

    @compat_version.setter
    def compat_version(self, val):
        self._compat_version = val

    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, val):
        self._components = val

    @property
    def configuration(self):
        return self._configuration

    @configuration.setter
    def configuration(self, val):
        self._configuration = val

    @property
    def configurations(self):
        return self._configurations

    @configurations.setter
    def configurations(self, val):
        self._configurations = val

    @property
    def cps_path(self):
        return self._cps_path

    @cps_path.setter
    def cps_path(self, val):
        self._cps_path = val

    @property
    def cps_version(self):
        return self._cps_version

    @cps_version.setter
    def cps_version(self, val):
        self._cps_version = val

    @property
    def default_components(self):
        return self._default_components

    @default_components.setter
    def default_components(self, val):
        self._default_components = val

    @property
    def requires(self):
        return self._requires

    @requires.setter
    def requires(self, val):
        self._requires = val


class Platform:
    """CPS Platform object"""
    def __init__(
            self,
            *,
            c_runtime_vendor=None,
            c_runtime_version=None,
            cpp_runtime_version=None,
            cpp_runtime_vendor=None,
            clr_vendor=None,
            clr_version=None,
        ):
        """"""

    @property
    def c_runtime_vendor(self):
        return self._c_runtime_vendor

    @c_runtime_vendor.setter
    def c_runtime_vendor(self, val):
        self._c_runtime_vendor = val

    @property
    def c_runtime_version(self):
        return self._c_runtime_version

    @c_runtime_version.setter
    def c_runtime_version(self, val):
        self._c_runtime_version = val

    @property
    def cpp_runtime_version(self):
        return self._cpp_runtime_version

    @cpp_runtime_version.setter
    def cpp_runtime_version(self, val):
        self._cpp_runtime_version = val

    @property
    def cpp_runtime_vendor(self):
        return self._cpp_runtime_vendor

    @cpp_runtime_vendor.setter
    def cpp_runtime_vendor(self, val):
        self._cpp_runtime_vendor = val

    @property
    def clr_vendor(self):
        return self._clr_vendor

    @clr_vendor.setter
    def clr_vendor(self, val):
        self._clr_vendor = val

    @property
    def clr_version(self):
        return self._clr_version

    @clr_version.setter
    def clr_version(self, val):
        self._clr_version = val

    @property
    def isa(self):
        return self._isa

    @isa.setter
    def isa(self, val):
        self._isa = val

    @property
    def jvm_vendor(self):
        return self._jvm_vendor

    @jvm_vendor.setter
    def jvm_vendor(self, val):
        self._jvm_vendor = val

    @property
    def jvm_version(self):
        return self._jvm_version

    @jvm_version.setter
    def jvm_version(self, val):
        self._jvm_version = val

    @property
    def kernel(self):
        return self._kernel

    @kernel.setter
    def kernel(self, val):
        self._kernel = val

    @property
    def kernel_version(self):
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, val):
        self._kernel_version = val



class Requirement:
    """CPS Requirement object"""
    def __init__(self, *comps, components=None):
        """"""

    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, val):
        self._components = val

    @property
    def hints(self):
        return self._hints

    @hints.setter
    def hints(self, val):
        self._hints = val

    @property
    def requires(self):
        return self._requires

    @requires.setter
    def requires(self, val):
        self._requires = val

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, val):
        self._version = val



class Component:
    """CPS Component object"""
    def __init__(self):
        """"""

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, val):
        self._type = val

    @property
    def compile_features(self):
        return self._compile_features

    @compile_features.setter
    def compile_features(self, val):
        self._compile_features = val

    @property
    def compile_flags(self):
        return self._compile_flags

    @compile_flags.setter
    def compile_flags(self, val):
        self._compile_flags = val

    @property
    def definitions(self):
        return self._definitions

    @definitions.setter
    def definitions(self, val):
        self._definitions = val

    @property
    def includes(self):
        return self._includes

    @includes.setter
    def includes(self, val):
        self._includes = val

    @property
    def link_features(self):
        return self._link_features

    @link_features.setter
    def link_features(self, val):
        self._link_features = val

    @property
    def link_flags(self):
        return self._link_flags

    @link_flags.setter
    def link_flags(self, val):
        self._link_flags = val

    @property
    def link_languages(self):
        return self._link_languages

    @link_languages.setter
    def link_languages(self, val):
        self._link_languages = val

    @property
    def link_libraries(self):
        return self._link_libraries

    @link_libraries.setter
    def link_libraries(self, val):
        self._link_libraries = val

    @property
    def link_location(self):
        return self._link_location

    @link_location.setter
    def link_location(self, val):
        self._link_location = val

    @property
    def link_requires(self):
        return self._link_requires

    @link_requires.setter
    def link_requires(self, val):
        self._link_requires = val

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, val):
        self._location = val

    @property
    def requires(self):
        return self._requires

    @requires.setter
    def requires(self, val):
        self._requires = val


class Configuration:
    """CPS Configuration object"""
    def __init__(self):
        """"""

    @property
    def compile_features(self):
        return self._compile_features

    @compile_features.setter
    def compile_features(self, val):
        self._compile_features = val

    @property
    def compile_flags(self):
        return self._compile_flags

    @compile_flags.setter
    def compile_flags(self, val):
        self._compile_flags = val

    @property
    def definitions(self):
        return self._definitions

    @definitions.setter
    def definitions(self, val):
        self._definitions = val

    @property
    def includes(self):
        return self._includes

    @includes.setter
    def includes(self, val):
        self._includes = val

    @property
    def link_features(self):
        return self._link_features

    @link_features.setter
    def link_features(self, val):
        self._link_features = val

    @property
    def link_flags(self):
        return self._link_flags

    @link_flags.setter
    def link_flags(self, val):
        self._link_flags = val

    @property
    def link_languages(self):
        return self._link_languages

    @link_languages.setter
    def link_languages(self, val):
        self._link_languages = val

    @property
    def link_libraries(self):
        return self._link_libraries

    @link_libraries.setter
    def link_libraries(self, val):
        self._link_libraries = val

    @property
    def link_location(self):
        return self._link_location

    @link_location.setter
    def link_location(self, val):
        self._link_location = val

    @property
    def link_requires(self):
        return self._link_requires

    @link_requires.setter
    def link_requires(self, val):
        self._link_requires = val

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, val):
        self._location = val

    @property
    def requires(self):
        return self._requires

    @requires.setter
    def requires(self, val):
        self._requires = val
