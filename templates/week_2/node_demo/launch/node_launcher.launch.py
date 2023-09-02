#!/usr/bin/env python3


import os
import sys
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction



def generate_launch_description():

    ld = LaunchDescription()
    for i in range(5):
        node_name = "node_"+str(i)
        node = Node(
            package='node_demo',
            executable='node_maker.py',
            arguments=[ node_name
            ],
            output='screen',
            emulate_tty=True,
        )
        ld.add_action(TimerAction(period=1.0,
                                  actions=[node],))



    return ld
