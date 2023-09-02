#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import sys


class MyNode(Node):

    def __init__(self, arg1):
       
        # Initialize Node
        super().__init__(arg1)
        self.get_logger().info(f'ROS 2 Node is running with name {arg1}')


def main(args=None):
    rclpy.init(args=args)

    arg1 = sys.argv[1]
    
    node = MyNode(arg1)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
