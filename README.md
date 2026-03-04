Autonomous Robotics Platform: PiBot-DetectNav
Repository: github.com/sudharshanrao/pibot-detectnav
Author: Sudharshan Rao Rajampalli | Linux/Cloud Engineer | MBA (Business Analytics)
Version: 1.0 | March 2023 
​

Raspberry Pi-based autonomous robot integrating TensorFlow Lite object detection, RPLIDAR scanning, and motor control for real-time navigation and obstacle avoidance.

Designed for edge AI applications, achieving ~5-10 FPS detection on Pi hardware.

Technical Overview
Core Components:

Compute: Raspberry Pi 4/5 with TensorFlow Lite (EfficientDet-Lite0).

Vision: Pi Camera / USB cam for sliding-window pyramid detection (utils.py).

Sensors: RPLIDAR A1/A2 (360° mapping), IMU/GPS, motor encoders.

Actuation: DC motors via L298N drivers, 4WD chassis.

Power: LiPo battery pack (7.4V, monitored at 7.65A draw).

Pipeline: Image pyramid → CNN classification → NMS → Bounding boxes → LiDAR fusion for path planning.

Key Capabilities
Feature	Description	Performance
Object Detection	80+ COCO classes, threshold 0.5	5-10 FPS 
​
LiDAR Scanning	360° @ 5.7Hz, 4K points	343 RPM motors 
Navigation	Reactive avoidance via sensor fusion	Real-time 
​
Visualization	Live stream, point clouds, metrics	Pi display/SSH 
​
Results: table_results.csv logs detections (e.g., class probs >0.7).
​

Prerequisites
Raspberry Pi OS (64-bit, Bookworm/Debian 12).

Hardware: Pi Camera, RPLIDAR USB, motor drivers.

Python 3.9+, ~2GB SD card.
​

Installation
bash
git clone https://github.com/sudharshanrao/pibot-detectnav.git
cd pibot-detectnav
chmod +x setup.sh
./setup.sh  # Installs tflite_runtime, opencv, rplidar [file:12]
Libraries: numpy, opencv-python, pillow, tflite-runtime.
​

Usage
1. LiDAR Test:

bash
python3 display_lidar_pi.py --port /dev/ttyUSB0
Visualizes scans; calibrate angles.
​

2. Detection Demo:

bash
python3 detect.py --model efficientdet_lite0.tflite --threshold 0.5
Camera feed with boxes/FPS overlay. Add --enableEdgeTPU for accelerator.

3. Full Robot Mode (extend detect.py):
Integrate motor control via utils.py for autonomous runs.
​

Motor scan example: 343 RPM, stable at Deg 69°.
​

Architecture Diagram
Sensors → Pi CPU → Detection/Nav → Motors.
​

Performance Benchmarks
text
Current: 7.65A | Deg: 69.08 | RPM: 343 | Freq: 5.7Hz [file:13]
EdgeTPU boosts inference 3-5x.
​

Contributing & Roadmap
Issues: Report via GitHub.

Next: ROS2 integration, SLAM (Cartographer), Kubernetes edge deployment.

License: MIT. See SECURITY.md for guidelines.
​

Acknowledgments
Built on TensorFlow Lite examples; RPLIDAR SDK. Portfolio project showcasing edge AI, Linux automation.
​

Contact: sudharshanrajampalli@gmail.com | LinkedIn:https://www.linkedin.com/in/sudharshan-rao-rajampalli-7b69b223a/ | Hyderabad, India. 
