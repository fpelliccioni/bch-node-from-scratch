cmake_minimum_required(VERSION 3.15)
project(node CXX)

add_executable(node src/node.cpp src/main.cpp)

install(TARGETS node DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
