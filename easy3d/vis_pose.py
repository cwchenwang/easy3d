import viser
import viser.transforms as viser_tf
import json
import time

class CameraViewer:
    def __init__(self):
        self.server = viser.ViserServer()
    
    def add_cameras(self, c2ws, fov, images=None, **kwargs):
        camera_positions = []
        camera_rotations = []
        for c2w in c2ws:
            T_world_camera = viser_tf.SE3.from_matrix(c2w)
            camera_positions.append(T_world_camera.translation())
            camera_rotations.append(T_world_camera.rotation().wxyz)

        for i, (pos, rot) in enumerate(zip(camera_positions, camera_rotations)):
            self.server.scene.add_camera_frustum(
                f"/cam_{i}",
                fov,
                aspect=1.0 if images is None else images[i].shape[1] / images[i].shape[0],
                image=images[i] if images is not None else None,
                wxyz=rot,
                position=pos,
            )

    def run(self):
        while True:
            time.sleep(10.0)