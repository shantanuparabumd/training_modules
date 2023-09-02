Create Workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

Build Workspace

```bash
colcon build
```

Create Package

```bash
ros2 pkg create --build-type ament_cmake <package_name>
```

Install Dependencies

```bash
# cd if you're still in the ``src`` directory with the ``ros_tutorials`` clone
cd ..
rosdep install -i --from-path src --rosdistro galactic -y
```

