#!/usr/bin/env python3



from launch import LaunchDescription
from launch.actions import ExecuteProcess



def generate_launch_description():

    ld = LaunchDescription()

    robot_1 = ExecuteProcess(
        cmd=[[
            'ros2 run topics_demo node_maker.py robot_1'
        ]],
        shell=True
    )


    robot_2 = ExecuteProcess(
        cmd=[[
            'ros2 run topics_demo node_maker.py robot_2'
        ]],
        shell=True
    )

    robot_3 = ExecuteProcess(
        cmd=[[
            'ros2 run topics_demo node_maker.py robot_3'
        ]],
        shell=True
    )


    ld.add_action(robot_1)
    ld.add_action(robot_2)
    ld.add_action(robot_3)



    return ld
