# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/janko/code/trashcan/cmake/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/janko/code/trashcan/cmake/src/build

# Include any dependencies generated for this target.
include CMakeFiles/jlib.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/jlib.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/jlib.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/jlib.dir/flags.make

CMakeFiles/jlib.dir/h1.cpp.o: CMakeFiles/jlib.dir/flags.make
CMakeFiles/jlib.dir/h1.cpp.o: /home/janko/code/trashcan/cmake/src/h1.cpp
CMakeFiles/jlib.dir/h1.cpp.o: CMakeFiles/jlib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/janko/code/trashcan/cmake/src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/jlib.dir/h1.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/jlib.dir/h1.cpp.o -MF CMakeFiles/jlib.dir/h1.cpp.o.d -o CMakeFiles/jlib.dir/h1.cpp.o -c /home/janko/code/trashcan/cmake/src/h1.cpp

CMakeFiles/jlib.dir/h1.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/jlib.dir/h1.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janko/code/trashcan/cmake/src/h1.cpp > CMakeFiles/jlib.dir/h1.cpp.i

CMakeFiles/jlib.dir/h1.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/jlib.dir/h1.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janko/code/trashcan/cmake/src/h1.cpp -o CMakeFiles/jlib.dir/h1.cpp.s

CMakeFiles/jlib.dir/h2.cpp.o: CMakeFiles/jlib.dir/flags.make
CMakeFiles/jlib.dir/h2.cpp.o: /home/janko/code/trashcan/cmake/src/h2.cpp
CMakeFiles/jlib.dir/h2.cpp.o: CMakeFiles/jlib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/janko/code/trashcan/cmake/src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/jlib.dir/h2.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/jlib.dir/h2.cpp.o -MF CMakeFiles/jlib.dir/h2.cpp.o.d -o CMakeFiles/jlib.dir/h2.cpp.o -c /home/janko/code/trashcan/cmake/src/h2.cpp

CMakeFiles/jlib.dir/h2.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/jlib.dir/h2.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janko/code/trashcan/cmake/src/h2.cpp > CMakeFiles/jlib.dir/h2.cpp.i

CMakeFiles/jlib.dir/h2.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/jlib.dir/h2.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janko/code/trashcan/cmake/src/h2.cpp -o CMakeFiles/jlib.dir/h2.cpp.s

# Object files for target jlib
jlib_OBJECTS = \
"CMakeFiles/jlib.dir/h1.cpp.o" \
"CMakeFiles/jlib.dir/h2.cpp.o"

# External object files for target jlib
jlib_EXTERNAL_OBJECTS =

libjlib.a: CMakeFiles/jlib.dir/h1.cpp.o
libjlib.a: CMakeFiles/jlib.dir/h2.cpp.o
libjlib.a: CMakeFiles/jlib.dir/build.make
libjlib.a: CMakeFiles/jlib.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/janko/code/trashcan/cmake/src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX static library libjlib.a"
	$(CMAKE_COMMAND) -P CMakeFiles/jlib.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/jlib.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/jlib.dir/build: libjlib.a
.PHONY : CMakeFiles/jlib.dir/build

CMakeFiles/jlib.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/jlib.dir/cmake_clean.cmake
.PHONY : CMakeFiles/jlib.dir/clean

CMakeFiles/jlib.dir/depend:
	cd /home/janko/code/trashcan/cmake/src/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/janko/code/trashcan/cmake/src /home/janko/code/trashcan/cmake/src /home/janko/code/trashcan/cmake/src/build /home/janko/code/trashcan/cmake/src/build /home/janko/code/trashcan/cmake/src/build/CMakeFiles/jlib.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/jlib.dir/depend

