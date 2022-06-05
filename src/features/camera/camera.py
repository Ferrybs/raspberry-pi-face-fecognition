import cv2
import face_recognition
import json
import numpy as np
class Camera:
    def __init__(self,home_dir: str) -> None:
        self.__home_dir = home_dir
        self.__cam = cv2.VideoCapture('/dev/video0')
        self.__data = {}
        self.__loadData()
        pass
    def __loadData(self):
        with open(self.__home_dir+"/data/encodings.json") as data:
            self.__data = json.load(data)
        pass
    def start(self):
        while True:
            ret, frame = self.__cam.read()
            rgb_frame = frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(self.__data["encodings"], face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(self.__data["encodings"], face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.__data["names"][best_match_index]

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            cv2.imshow('Video', frame)
            k = cv2.waitKey(1)
            if k%256 == 27:
                self.__cam.release()
                cv2.destroyAllWindows()