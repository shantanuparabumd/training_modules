#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import sys

# Import message type
from std_msgs.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__("node_subscriber")
        self.get_logger().info(f'ROS 2 Node is running with name node_subscriber')

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

    node = MyNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
