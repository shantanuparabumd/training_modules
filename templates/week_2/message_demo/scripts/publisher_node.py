#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# Import your Message                     
# from package_name.msg import Message   

class MinimalPublisher(Node):

    def __init__(self):

        # Give your node a name
        super().__init__('node_name')

        # Create a Publisher to publish your Message
        # self.publisher_ = self.create_publisher(Message, 'topic', 10)  

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    # Define the callback function

    # def timer_callback(self):
        # msg = Message()                                               
        # msg.variable_name1 = "drones"      
        # msg.variable_name1 = 10                                    
        # self.publisher_.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
