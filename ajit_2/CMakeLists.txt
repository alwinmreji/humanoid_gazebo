cmake_minimum_required(VERSION 2.8.3)

project(ajit_2)

find_package(catkin REQUIRED COMPONENTS
roscpp
rospy
std_msgs
)

catkin_package()
# add_executable(${PROJECT_NAME}_node src/driver.cpp)
# target_link_libraries(${PROJECT_NAME}_node ${catkin_LIBRARIES})
# add_dependencies(${PROJECT_NAME}_node roscpp std_msgs)
find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
