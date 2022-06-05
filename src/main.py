import os
from features.camera.camera import Camera
if __name__ == "__main__":
    dir_home = os.path.dirname(os.path.realpath(__file__))
    Camera(dir_home).start()

