import cv2;
import os.path

class Headshot:
    def __init__(self,name: str) -> None:
        self.__name = name
        self.__cam = cv2.VideoCapture('/dev/video0')
        self.__image_counter = 0
        self.__dir_name = os.path.dirname(os.path.realpath(__file__))
        try:
            os.mkdir(self.__dir_name+"/dataset/Felipe")
        except OSError as e:
            print(e.args)
        pass
    def takePicture(self):
        while True:
            ret, frame = self.__cam
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
                img_name: str = "./src/dataset/"+ self.__name +"/image_{}.jpg".format(self.__image_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                self.__image_counter += 1
        self.__cam.release()
        cv2.destroyAllWindows()