cmake_minimum_required(VERSION 3.18)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

project(CodeWars VERSION 0.1)

add_executable(StringEnds StringEnds/main.cpp StringEnds/stringEnds.cpp)
add_executable(Persistance Persistance/main.cpp Persistance/persistance.cpp)
