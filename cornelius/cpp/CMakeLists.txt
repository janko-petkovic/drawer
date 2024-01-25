cmake_minimum_required(VERSION 3.28)

project(CRN95)
set(CMAKE_CXX_STANDARD 20)
set(PYBIND11_PYTHON_VERSION 3.6)
set(CMAKE_CXX_FLAGS "-Wall -Wextra -fPIC -lpython3.11")

find_package(pybind11 REQUIRED)

pybind11_add_module(${PROJECT_NAME} simulation.cpp pywrap.cpp)


target_compile_definitions(${PROJECT_NAME} PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
target_include_directories(${PROJECT_NAME} PRIVATE ${PYBIND11_INCLUDE_DIRS})
