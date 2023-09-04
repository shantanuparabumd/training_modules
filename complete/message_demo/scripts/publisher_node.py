#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from message_demo.msg import Custom                         


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('customer')
        self.publisher_ = self.create_publisher(Custom, 'topic', 10)  
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Custom()                                               
        msg.product_name = "drones"      
        msg.quantity = 10                                    
        self.publisher_.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
