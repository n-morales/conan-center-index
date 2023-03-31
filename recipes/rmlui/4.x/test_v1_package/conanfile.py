from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools.build import cross_building
import os

# legacy validation with Conan 1.x
class ConanRmluiTestV1Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeToolchain", "CMakeDeps"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not cross_building(self):
            cmake = CMake(self)
            cmake.configure()
            cmake.test()
