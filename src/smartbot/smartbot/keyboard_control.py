import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class KeyboardControl(Node):

    def __init__(self):
        super().__init__('keyboard_control')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def run(self):
        print("i = forward")
        print(", = backward")
        print("j = left")
        print("l = right")
        print("k = stop")
        print("q = quit")

        while rclpy.ok():
            key = input("Command: ").strip()

            msg = Twist()

            if key == 'i':
                msg.linear.x = -0.5
            elif key == ',':
                msg.linear.x = 0.5
            elif key == 'j':
                msg.angular.z = 0.8
            elif key == 'l':
                msg.angular.z = -0.8
            elif key == 'k':
                msg.linear.x = 0.0
                msg.angular.z = 0.0
            elif key == 'q':
                break
            else:
                continue

            self.pub.publish(msg)


def main():
    rclpy.init()
    node = KeyboardControl()

    try:
        node.run()
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
