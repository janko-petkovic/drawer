cmake_minimum_required(VERSION 3.20)

project(Jlib)

add_library(jlib h1.cpp h2.cpp)
add_executable(main main.cpp)
target_link_libraries(main jlib)
