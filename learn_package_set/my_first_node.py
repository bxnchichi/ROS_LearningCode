#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

#create node by using class
class MyNode(Node):

    def __init__(self):
        super().__init__("first_node")
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)

    
    def timer_callback(self):
        self.get_logger().info("Hello!!" + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    #start of the node
    rclpy.init(args = args) 
    #ros2 communication is here
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown() #end node


#call main if the name of the node is called
if __name__ == '__main__':
    main()