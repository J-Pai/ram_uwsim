# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "underwater_sensor_msgs: 2 messages, 1 services")

set(MSG_I_FLAGS "-Iunderwater_sensor_msgs:/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg;-Iroscpp:/opt/ros/indigo/share/roscpp/cmake/../msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg;-Ivisualization_msgs:/opt/ros/indigo/share/visualization_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(underwater_sensor_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/srv/SpawnMarker.srv" NAME_WE)
add_custom_target(_underwater_sensor_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "underwater_sensor_msgs" "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/srv/SpawnMarker.srv" "geometry_msgs/Point:geometry_msgs/Vector3:std_msgs/Header:geometry_msgs/Quaternion:std_msgs/ColorRGBA:visualization_msgs/Marker:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/DVL.msg" NAME_WE)
add_custom_target(_underwater_sensor_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "underwater_sensor_msgs" "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/DVL.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/Pressure.msg" NAME_WE)
add_custom_target(_underwater_sensor_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "underwater_sensor_msgs" "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/Pressure.msg" "std_msgs/Header"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(underwater_sensor_msgs
  "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/DVL.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/underwater_sensor_msgs
)
_generate_msg_cpp(underwater_sensor_msgs
  "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/Pressure.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/underwater_sensor_msgs
)

### Generating Services
_generate_srv_cpp(underwater_sensor_msgs
  "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/srv/SpawnMarker.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/ColorRGBA.msg;/opt/ros/indigo/share/visualization_msgs/cmake/../msg/Marker.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/underwater_sensor_msgs
)

### Generating Module File
_generate_module_cpp(underwater_sensor_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/underwater_sensor_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(underwater_sensor_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(underwater_sensor_msgs_generate_messages underwater_sensor_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/srv/SpawnMarker.srv" NAME_WE)
add_dependencies(underwater_sensor_msgs_generate_messages_cpp _underwater_sensor_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/DVL.msg" NAME_WE)
add_dependencies(underwater_sensor_msgs_generate_messages_cpp _underwater_sensor_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/Pressure.msg" NAME_WE)
add_dependencies(underwater_sensor_msgs_generate_messages_cpp _underwater_sensor_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(underwater_sensor_msgs_gencpp)
add_dependencies(underwater_sensor_msgs_gencpp underwater_sensor_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS underwater_sensor_msgs_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(underwater_sensor_msgs
  "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/DVL.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/underwater_sensor_msgs
)
_generate_msg_lisp(underwater_sensor_msgs
  "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/Pressure.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/underwater_sensor_msgs
)

### Generating Services
_generate_srv_lisp(underwater_sensor_msgs
  "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/srv/SpawnMarker.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/ColorRGBA.msg;/opt/ros/indigo/share/visualization_msgs/cmake/../msg/Marker.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/underwater_sensor_msgs
)

### Generating Module File
_generate_module_lisp(underwater_sensor_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/underwater_sensor_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(underwater_sensor_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(underwater_sensor_msgs_generate_messages underwater_sensor_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/srv/SpawnMarker.srv" NAME_WE)
add_dependencies(underwater_sensor_msgs_generate_messages_lisp _underwater_sensor_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/DVL.msg" NAME_WE)
add_dependencies(underwater_sensor_msgs_generate_messages_lisp _underwater_sensor_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/Pressure.msg" NAME_WE)
add_dependencies(underwater_sensor_msgs_generate_messages_lisp _underwater_sensor_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(underwater_sensor_msgs_genlisp)
add_dependencies(underwater_sensor_msgs_genlisp underwater_sensor_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS underwater_sensor_msgs_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(underwater_sensor_msgs
  "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/DVL.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/underwater_sensor_msgs
)
_generate_msg_py(underwater_sensor_msgs
  "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/Pressure.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/underwater_sensor_msgs
)

### Generating Services
_generate_srv_py(underwater_sensor_msgs
  "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/srv/SpawnMarker.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/ColorRGBA.msg;/opt/ros/indigo/share/visualization_msgs/cmake/../msg/Marker.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/underwater_sensor_msgs
)

### Generating Module File
_generate_module_py(underwater_sensor_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/underwater_sensor_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(underwater_sensor_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(underwater_sensor_msgs_generate_messages underwater_sensor_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/srv/SpawnMarker.srv" NAME_WE)
add_dependencies(underwater_sensor_msgs_generate_messages_py _underwater_sensor_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/DVL.msg" NAME_WE)
add_dependencies(underwater_sensor_msgs_generate_messages_py _underwater_sensor_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/user/ram_uwsim/src/underwater_simulation/underwater_sensor_msgs/msg/Pressure.msg" NAME_WE)
add_dependencies(underwater_sensor_msgs_generate_messages_py _underwater_sensor_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(underwater_sensor_msgs_genpy)
add_dependencies(underwater_sensor_msgs_genpy underwater_sensor_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS underwater_sensor_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/underwater_sensor_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/underwater_sensor_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(underwater_sensor_msgs_generate_messages_cpp roscpp_generate_messages_cpp)
add_dependencies(underwater_sensor_msgs_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(underwater_sensor_msgs_generate_messages_cpp visualization_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/underwater_sensor_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/underwater_sensor_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(underwater_sensor_msgs_generate_messages_lisp roscpp_generate_messages_lisp)
add_dependencies(underwater_sensor_msgs_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(underwater_sensor_msgs_generate_messages_lisp visualization_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/underwater_sensor_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/underwater_sensor_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/underwater_sensor_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(underwater_sensor_msgs_generate_messages_py roscpp_generate_messages_py)
add_dependencies(underwater_sensor_msgs_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(underwater_sensor_msgs_generate_messages_py visualization_msgs_generate_messages_py)
