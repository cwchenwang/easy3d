# Easy3D

A simple and intuitive Python package for 3D.

## Features

- 3D camera pose visualization using Viser

## Installation

```bash
pip install easy3d
```

## Quick Start

```python
from easy3d import CameraViewer

# Create camera poses (4x4 transformation matrices)
poses = []
for i in range(10):
    pose = np.eye(4)
    pose[:3, 3] = [i * 0.1, 0, 0]  # Move along x-axis
    poses.append(pose)

# Visualize the camera poses
camera_viewer = CameraViewer()
camera_viewer.add_cameras(poses, fov=30)
camera_viewer.run()
```

## Requirements

- Python >= 3.8
- numpy >= 1.21.0
- matplotlib >= 3.5.0
- viser >= 0.1.0

## License

MIT License - see LICENSE file for details.

## Author

Chen Wang (chwangthu@gmail.com) 