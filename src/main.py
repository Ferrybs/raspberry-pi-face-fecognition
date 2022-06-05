import cv2
import os

from features.headshot.headshot import Headshot

if __name__ == "__main__":
    print(cv2.getBuildInformation())
    Headshot("Felipe")
    

