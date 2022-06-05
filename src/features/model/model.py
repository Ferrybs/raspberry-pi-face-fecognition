import face_recognition
import os
import json
class Model:
    def __init__(self,dir_home: str) -> None:
        self.__dir_home = dir_home
        self.__images = {}
        self.__knownEncodings = []
        self.__knownNames = []


    def __loadImages(self):
        for folder in os.listdir(self.__dir_home+"/dataset"):
            if folder !=  ".keep":
                self.__images[folder]  = os.listdir(self.__dir_home+"/dataset/"+folder)
    def __encode(self):
        for name,v in self.__images.items():
            for image_name in v:
                print("["+name+"]:"+image_name)
                image = face_recognition.load_image_file(self.__dir_home+"/dataset/"+name+"/"+image_name)
                boxes = face_recognition.face_locations(image,model="hog")
                encodings = face_recognition.face_encodings(image, boxes)
                for encod in encodings:
                    self.__knownEncodings.append(encod.tolist())
                    self.__knownNames.append(name)
    def __save(self):
        data = {"encodings": self.__knownEncodings, "names": self.__knownNames}
        with open(self.__dir_home+"/data/encodings.json","w+") as outfile:
            json.dump(data,outfile)
  
    def train(self):
        self.__loadImages()
        self.__encode()
        self.__save()

