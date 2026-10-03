from setuptools import find_packages, setup

package_name = 'smartbot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            'share/' + package_name + '/urdf',
            ['urdf/smartbot.urdf']
        ),
        (
            'share/' + package_name + '/worlds',
            ['worlds/empty.sdf']
        ),
        (
            'share/' + package_name + '/launch',
            ['launch/smartbot_gazebo.launch.py']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bhumika',
    maintainer_email='bhumika@todo.todo',
    description='SmartBot ROS2 package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = smartbot.publisher:main',
            'subscriber = smartbot.subscriber:main',
        ],
    },
)

