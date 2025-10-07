cmake_minimum_required(VERSION 2.8.3)
project(zed_urdf)

find_package(catkin REQUIRED)

catkin_package(
  CATKIN_DEPENDS
)

install(DIRECTORY  urdf
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

