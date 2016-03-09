#include <pluginlib/class_list_macros.h>
#include <uwsim/SimRawData.h>

/* You will need to add your code HERE */

SimulatedDeviceConfig::Ptr SimRawData_Factory::processConfig(const xmlpp::Node* node, ConfigFile * config){}

bool SimRawData_Factory::applyConfig(SimulatedIAUV * auv, Vehicle &vehicleChars, SceneBuilder *sceneBuilder, size_t iteration){}

std::vector<boost::shared_ptr<ROSInterface> > SimRawData_Factory::getInterface(ROSInterfaceInfo & rosInterface, std::vector<boost::shared_ptr<SimulatedIAUV> > & iauvFile){}


#if ROS_VERSION_MINIMUM(1, 9, 0)
// new pluginlib API in Groovy and Hydro
PLUGINLIB_EXPORT_CLASS(SimRawData_Factory, uwsim::SimulatedDeviceFactory)
#else
PLUGINLIB_REGISTER_CLASS(SimRawData_Factory, SimRawData_Factory, uwsim::SimulatedDeviceFactory)
#endif
