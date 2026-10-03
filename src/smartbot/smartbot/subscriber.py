import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SmartBotSubscriber(Node):

    def __init__(self):
        super().__init__('smartbot_subscriber')

        self.subscription = self.create_subscription(
            String,
            'smartbot_command',
            self.receive_message,
            10
        )

    def receive_message(self, msg):
        self.get_logger().info(f'Received: {msg.data}')


def main(args=None):
    rclpy.init(args=args)

    node = SmartBotSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
