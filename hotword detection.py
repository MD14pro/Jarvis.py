import speech_recognition as sr
import subprocess
import sys

def exitprg():
    sys.exit(0)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        return "None"
    return query

while True:
    wake_up = takeCommand()

    if 'wake up Jarvis' in wake_up:
        subprocess.run(["python","jarvis.py"])
        exitprg()
    else:
        print("nothing....")



import cv2
import face_recognition
video = cv2.VideoCapture(0)

face = face_recognition.load_image_file("md.jpg")
faceencoding = face_recognition.face_encodings(face)[0]

face_encodings_list = [faceencoding]

face_encodings = []
s = True
face_coordinates = []

while True:
    _, frame = video.read()
    resized_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    resized_frame_rgb = resized_frame[:, :, ::-1]

    if s:
        face_coordinates = face_recognition.face_locations(resized_frame_rgb)
        face_encodings = face_recognition.face_encodings(resized_frame_rgb, face_coordinates)
    for faces in face_encodings:
        matches = face_recognition.compare_faces(face_encodings_list, faces)
        if matches[0] == True:
            print("Authenticated successfully...")
            video.release()
            cv2.destroyAllWindows()

