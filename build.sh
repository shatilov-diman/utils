#/bin/bash

BUILD_TYPE=${1:-Release}

mkdir .build
cd .build
conan install ../conan/conanfile.txt -s compiler.version=7 -s arch=x86_64 -s build_type=${BUILD_TYPE} --build=missing
cmake -DCMAKE_BUILD_TYPE=${BUILD_TYPE} ..
cd ..
cmake --build .build --config ${BUILD_TYPE}

