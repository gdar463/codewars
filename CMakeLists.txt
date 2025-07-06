cmake_minimum_required(VERSION 3.18)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

project(CodeWars VERSION 0.1)

add_executable(StringEnds StringEnds/main.cpp StringEnds/stringEnds.cpp)
add_executable(Persistance Persistance/main.cpp Persistance/persistance.cpp)
add_executable(Alphabet Alphabet/main.cpp Alphabet/alphabet.cpp)
add_executable(Atoi Atoi/main.cpp Atoi/atoi.cpp)
add_executable(Baker Baker/main.cpp Baker/baker.cpp)
add_executable(BitCount BitCount/main.cpp BitCount/bitCount.cpp)
add_executable(CamelCase CamelCase/main.cpp CamelCase/camelCase.cpp)
