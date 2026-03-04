Autonomous Robot with Object Detection and LiDAR Navigation
This repository contains code and setup for a Raspberry Pi-powered autonomous robot featuring real-time object detection using TensorFlow Lite and LiDAR-based navigation.

The robot integrates a camera for EfficientDet-Lite object detection, RPLIDAR for mapping, motor drivers for mobility, and sensors like GPS for positioning.

Images show the assembled chassis with Raspberry Pi, battery, wheels, and electronics.

Features
Real-time object detection with sliding window pyramid processing and NMS.
​

LiDAR visualization and scanning via RPLIDAR (display_lidar_pi.py).
​

Robot hardware: Motors, camera, sensors, as in diagrams and motor scan results.

Performance metrics like RPM (343), current (7.65A), and detection results in CSV.
​

Hardware Setup
Assemble the robot using Raspberry Pi 4/5, RPLIDAR A1/A2, Pi Camera or USB cam, motor drivers (e.g., L298N), and 4-wheel chassis.

Connect as shown in photos: Raspberry Pi central, LiDAR top-mounted, battery power.

Run motor tests and LiDAR scans first for calibration.
​

Software Requirements
Install dependencies from requirements.txt, including tflite_runtime, opencv, numpy.

Key libraries: TensorFlow Lite, OpenCV for detection; rplidar for scanning.
​

Quick Start
Clone repo and run setup:

text
chmod +x setup.sh
./setup.sh
This installs deps and downloads models.

Test LiDAR:

text
python3 display_lidar_pi.py
Visualize scans on Pi display.
​

Run object detection:

text
python3 detect.py --model efficientdet_lite0.tflite
Streams camera, detects objects with bounding boxes and FPS.

Object Detection Pipeline
Uses pyramid sliding window: Input image → Construct pyramid → Classify windows via CNN → NMS → Extract ROIs.

Supports EdgeTPU acceleration for faster inference.
​

LiDAR and Navigation
RPLIDAR provides 360° scans at ~5-10Hz. display_lidar_pi.py renders point clouds.
​

Integrate with detection for obstacle avoidance.
​

Results
Metric	Value
Motor RPM	343
Current	7.65A
FPS (est.)	~5-10
Detection table image shows class probs and boxes.
​

Future Work
Fuse LiDAR + detection for SLAM/autonomous nav.

Kubernetes deployment for cloud logging (user interest).

Optimize for Pi with threading.
​

License and Security
See SECURITY.md for vuln reporting. MIT License.
​

Built by Sudharshan Rao Rajampalli for robotics and analytics portfolio. [user-information]



