cmake_minimum_required(VERSION 3.20)
project(Jlib)

set(SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)
add_library(jlib
	${SRC_DIR}/h1.cpp
			${CMAKE_CURRENT_SOURCE_DIR}/src/h2.cpp)

add_executable(test ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp)
target_link_libraries(test jlib)
install(TARGETS test DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/bin)
