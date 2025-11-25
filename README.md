# Count People Using Webcam

This project uses the Ultralytics YOLO model to count people in an image captured from your webcam.

## Prerequisites

Ensure you have the following installed:
- Python 3.12
- A functional webcam
- Docker (optional, for containerized usage. 6GB of storage is needed)

## Installation

### Using Python
1. Install the required dependencies:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python3 src/count_people.py
   ```

### Using Docker
1. Build the Docker image:
   ```bash
   docker build -t count .
   ```

2. Run the Docker container:
   ```bash
   docker run -it --device=/dev/video0 --privileged count:latest
   ```

The container will look for the camera located at /dev/video0 on *Linux*. If you have another solution is needed.

## License

This project is licensed under the MIT License.
