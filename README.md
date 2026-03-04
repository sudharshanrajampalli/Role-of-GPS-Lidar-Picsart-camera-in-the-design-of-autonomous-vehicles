PiBot-DetectNav: Autonomous Robotics Platform
<div align="center"> <img src="https://via.placeholder.com/1200x200/1E3A8A/FFFFFF?text=PiBot+DetectNav+-+Edge+AI+Robotics" width="100%"> <br><br> <img src="image-1.jpg" width="180"> <img src="image-2.jpg" width="180"> <img src="MicrosoftTeams-image-2.jpg" width="180"> </div>
📋 Project Overview
Deploy your autonomous robot platform with confidence using this step-by-step guide.

Raspberry Pi-powered robot with TensorFlow Lite object detection + RPLIDAR navigation. Production-ready with 5-10 FPS detection performance.

Status: 🟢 Production Ready | March 2026

🚀 Deployment Paths
Path 1: Local Testing (Current ✅)	Path 2: Full Deployment (Next Phase)
✅ Unit tests, end-to-end, functional	🔄 Docker + Kubernetes deployment
✅ View Prometheus metrics	📊 Production monitoring
Run with confidence	Scale to production
🛠 Path 1: Local Testing (Current State ✅)
1️⃣ Setup Environment
bash
git clone https://github.com/sudharshanrao/pibot-detectnav.git
cd pibot-detectnav
chmod +x setup.sh && ./setup.sh
2️⃣ Unit Tests & Validation
bash
# Test LiDAR Scanning
python3 display_lidar_pi.py --port /dev/ttyUSB0

# Test Object Detection  
python3 detect.py --model efficientdet_lite0.tflite --threshold 0.5

# Motor Performance Test
python3 motor_scan.py  # 343 RPM achieved ✅
3️⃣ View Metrics
text
Current: 7.65A | RPM: 343 | LiDAR: 4K pts/sec | Detection: 5-10 FPS
<div align="center"> <img src="table.jpg" width="100%"> </div>
🏗 Architecture Overview
text
┌──────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Pi Camera  │───▶│ TensorFlow Lite  │───▶│ Motor Drivers   │
│  (detect.py) │    │   EfficientDet   │    │   (L298N)       │
└──────────────┘    └──────────────────┘    └─────────────────┘
         ▲                       ▲                       ▲
         └─────────┬─────────────┼──────────────┬────────┘
                   │             │              │
           ┌───────▼──────┐ ┌───▼──┐    ┌─────▼──────┐
           │   RPLIDAR    │ │ Pi 4/5│    │ 4WD Chassis│
           │ 360° Scanner │ │  CPU  │    │             │
           └──────────────┘ └───┬───┘    └─────────────┘
                               │
                         ┌─────▼──────┐
                         │  Battery   │
                         │   7.4V     │
                         └─────────────┘
📊 Performance Metrics
Component	Status	Performance
Object Detection	🟢 Live	5-10 FPS (80+ COCO classes)
LiDAR Scanning	🟢 Live	360° @ 5.7Hz, 4K points
Motor Control	🟢 Calibrated	343 RPM, 7.65A stable
Power System	⚡ Stable	LiPo 7.4V
Results logged: table_results.csv
​

📦 Prerequisites Checklist
 Raspberry Pi OS (64-bit Bookworm)

 Python 3.9+

 Pi Camera or USB Camera

 RPLIDAR A1/A2

 L298N Motor Drivers

 16GB+ SD Card

Auto-installed: tflite-runtime, opencv-python, numpy, rplidar

🔧 Troubleshooting Guide
Issue	Solution
Camera not found	sudo raspi-config → Interface → Camera → Enable
LiDAR: No data	sudo chmod 666 /dev/ttyUSB0
Low FPS (~2-3)	Add Coral EdgeTPU: --enableEdgeTPU
Motor stall	Verify 7.65A power supply capacity
🚀 Path 2: Full Deployment (Next Phase)
text
# kubernetes/pibot-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pibot-detectnav
spec:
  replicas: 1
  template:
    spec:
      containers:
      - name: robot-core
        image: sudharshanrao/pibot:latest
        resources:
          limits:
            nvidia.com/gpu: 1  # Jetson deployment
Features Planned:

 ROS2 Integration

 Cartographer SLAM

 Prometheus + Grafana

 Kubernetes Edge Deployment

🤝 Contributing Guidelines
text
1. Fork → Clone → Create Feature Branch
2. Run Path 1 tests locally ✅
3. Include performance benchmarks
4. Submit PR with `table_results.csv`
Issues: GitHub Issues

📄 License & Contact
text
License: MIT
Security: SECURITY.md
Author: Sudharshan Rao Rajampalli
Email: sudharshanrajampalli@gmail.com
LinkedIn: https://www.linkedin.com/in/sudharshan-rao-rajampalli-7b69b223a/
Location: Hyderabad, India
<div align="center"> <img src="https://via.placeholder.com/1000x80/1E40AF/FFFFFF?text=Built+with+❤️+for+Edge+AI+Robotics+in+Hyderabad" width="100%"> </div>
