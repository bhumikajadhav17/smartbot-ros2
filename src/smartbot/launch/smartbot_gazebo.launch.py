import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():

    pkg_path = get_package_share_directory('smartbot')

    gazebo_launch = os.path.join(
        get_package_share_directory('ros_gz_sim'),
        'launch',
        'gz_sim.launch.py'
    )

    world = os.path.join(
        pkg_path,
        'worlds',
        'empty.sdf'
    )

    urdf = os.path.join(
        pkg_path,
        'urdf',
        'smartbot.urdf'
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch),
        launch_arguments={
            'gz_args': world
        }.items()
    )

    spawn_robot = TimerAction(
        period=3.0,
        actions=[
            Node(
                package='ros_gz_sim',
                executable='create',
                arguments=[
                    '-file', urdf,
                    '-name', 'smartbot'
                ],
                output='screen'
            )
        ]
    )

    return LaunchDescription([
        gazebo,
        spawn_robot
    ])
