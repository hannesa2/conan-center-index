import os

from conans import ConanFile, CMake, tools

class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package_multi"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self):
            bin_c_path = os.path.join("bin", "test_package_c")
            self.run(bin_c_path, run_environment=True)
            bin_cpp_path = os.path.join("bin", "test_package_cpp")
            self.run(bin_cpp_path, run_environment=True)
