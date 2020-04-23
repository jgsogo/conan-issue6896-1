from conans import ConanFile, CMake
from conans import tools


class SayConan(ConanFile):
    name = "say"
    version = "version"
    generators = "cmake"

    scm = {"type": "git",
           "url": "https://github.com/jgsogo/conan-issue6896-2.git",
           "revision": "master"}

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["say"]
