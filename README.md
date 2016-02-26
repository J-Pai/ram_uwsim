# ram_uwsim
NOTE: Make sure you are using Ubuntu 14.04 LTS <br />
First clone this repository. Then change your current directory to the newly created repository's directory.
Commandlist:
```bash
git clone (THIS REPO URL)
cd ram_uwsim
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 0xB01FA116
sudo apt-get update
sudo apt-get install ros-indigo-desktop-full
sudo apt-get install python-rosinstall
sudo apt-get install ros-indigo-uwsim-bullet ros-indigo-uwsim-osgbullet ros-indigo-uwsim-osgocean ros-indigo-uwsim-osgworks 
sudo apt-get install ros-indigo-visualization-osg
echo 'source /opt/ros/indigo/setup.bash' >> ~/.bashrc
echo 'source $(pwd)/devel/setup.bash' >> ~/.bashrc
source ~/.bashrc
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro indigo -y
catkin_make install
catkin_make
```
