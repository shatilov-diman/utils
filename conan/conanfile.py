
import os
from conans import ConanFile, CMake

class LoggerConan(ConanFile):
    name="utils"
    version="1.0"
    description = "charivari's logger framework"
    url = "https://github.com/shatilov-diman/utils"
    license = "MIT License"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "gtest/master@conan/dev"

    def configure(self):
        self.settings.compiler["gcc"].version = "7"
        self.settings.compiler["Visual Studio"].version = "15"

    def source(self):
        self.run("git clone --recurse-submodules https://github.com/shatilov-diman/utils.git .")

    def test(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

        self.run(os.path.join(self.build_folder, "bin", "tests"))

    def package(self):
        self.copy("*.h")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

