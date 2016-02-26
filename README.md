# ram_uwsim
NOTE: Make sure you are using Ubuntu 14.04 LTS and you have git installed <br />
First clone this repository. Then change your current directory to the newly created repository's directory. <br />
Commandlist:
```bash
git clone https://github.com/J-Pai/ram_uwsim.git
cd ram_uwsim
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 0xB01FA116
sudo apt-get update
sudo apt-get install ros-indigo-desktop-full
sudo apt-get install python-rosinstall
sudo apt-get install ros-indigo-uwsim-bullet ros-indigo-uwsim-osgbullet ros-indigo-uwsim-osgocean ros-indigo-uwsim-osgworks 
sudo apt-get install ros-indigo-visualization-osg
echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
echo "source $(pwd)/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro indigo -y
catkin_make install
catkin_make
```
SOURCE: A good chunk of the code from the underwater_simulation folder is directly taken from the main uwsim repository. The modifications done to uwsim here is primarily meant for use with the Robotics@Maryland team. <br />
More information on uwsim can be found here: <http://www.irs.uji.es/uwsim/> <br />
The main repository can be found here: <https://github.com/uji-ros-pkg/underwater_simulation>
