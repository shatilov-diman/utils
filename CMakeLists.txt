project(utils)
cmake_minimum_required(VERSION 3.10)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(tests
	./__tests/main.cpp
	./__utils_tests/bool_t.cpp
	./__utils_tests/worker.cpp
	./__utils_tests/to_string.cpp
	./__utils_tests/task_queue.cpp
	./__utils_tests/ordered_queue.cpp
)
target_include_directories(tests PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/include")
target_link_libraries(tests ${CONAN_LIBS})

