"""Easy3D - A simple 3D utility package."""

__version__ = "0.1.1"
__author__ = "Chen Wang"
__email__ = "chwangthu@gmail.com"

# Import pose visualization functions
from .vis_pose import CameraViewer

# Define what gets imported with "from easy3d import *"
__all__ = [
    "CameraViewer",
]