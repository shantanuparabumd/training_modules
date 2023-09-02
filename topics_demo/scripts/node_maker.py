#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import sys

# Import message type
from std_msgs.msg import String


class MyNode(Node):

    def __init__(self, arg1):
       
        # Initialize Node
        super().__init__(arg1)
        self.get_logger().info(f'ROS 2 Node is running with name {arg1}')

        self.subscription = self.create_subscription(
            String,
            'my_topic',
            self.callback,
            10
        )
        self.subscription  # Prevent unused variable warning

    def callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')


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
