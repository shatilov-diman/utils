cp conan/conanfile.py ./
conan create . charivari_ltd/dev --build=missing
rm conanfile.py
