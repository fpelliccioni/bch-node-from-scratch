from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class nodeRecipe(ConanFile):
    name = "node"
    version = "1.0"
    package_type = "application"

    # Optional metadata
    license = "MIT License"
    author = "Fernando Pelliccioni fpelliccioni@gmail.com"
    url = "https://github.com/fpelliccioni/bitcoin-node-from-scratch"
    description = "Bitcoin (Cash) node from scratch"
    topics = ("bitcoin", "cash", "bch", "node")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
