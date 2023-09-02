### Create Workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

### Build Workspace

```bash
colcon build
```

### Create Package

```bash
ros2 pkg create --build-type ament_cmake <package_name>
```

### Install Dependencies

```bash
# cd if you're still in the ``src`` directory with the ``ros_tutorials`` clone
cd ..
rosdep install -i --from-path src --rosdistro galactic -y
```

### Build Packages

```bash
colcon build --packages-select <package_name>
```

### Source ROS

```bash
source /opt/ros/galactic/setup.bash
```

**Tip: You can also add this to your bash script**

```bash
sr_software(){
    cd ~/software_session/
    source /opt/ros/galactic/setup.bash
    . install/local_setup.bash
}
```


## Nodes

```bash
ros2 node list
ros2 node info /node_name
```

## Topics

```bash

ros2 topic list
ros2 topic echo /topic_name
```

## Messages

```bash

ros2 interface show /message_name
