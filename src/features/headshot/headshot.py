import cv2;
import os

class Headshot:
    def __init__(self,dir_name: str) -> None:
        self.__cam = cv2.VideoCapture('/dev/video0')
        self.__image_counter = 0
        self.__dir_name = dir_name
        pass
    def __makeDir(self, name: str):
        try:
            os.mkdir(self.__dir_name+"/dataset/"+name)
        except OSError as e:
            print("[WORNING]:Folder "+name+" already exist")
    def destroy(self):
        self.__cam.release()
        cv2.destroyAllWindows()
    def takePicture(self, name: str):
        self.__image_counter = 0
        self.__makeDir(name)
        while True:
            ret, frame = self.__cam.read()
            if not ret:
                print("Failed to grab frame, try again!")
                break
            cv2.imshow("Press SPACE to take a photo", frame)
            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name: str = "./src/dataset/"+ name +"/image_{}.jpg".format(self.__image_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                self.__image_counter += 1