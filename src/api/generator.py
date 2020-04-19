import face_recognition
import os
import cv2


def gen(known_faces=None, known_names=None):
    if known_faces == None:
        knwon_faces = []
    if known_names == None:
        known_names = []

    KNOWN_FACES_DIR = 'api/static/known_faces'
    TOLERANCE = 0.6
    FRAME_THICKNESS = 3
    FONT_THICKNESS = 1
    MODEL = 'cnn'

    '''Training of the model on the images'''
    for name in os.listdir(KNOWN_FACES_DIR):
        try:
            for filename in os.listdir(os.path.join(KNOWN_FACES_DIR, name)):
                image = face_recognition.load_image_file(
                    os.path.join(KNOWN_FACES_DIR, name, filename))
                encoding = face_recognition.face_encodings(image)[0]
                known_faces.append(encoding)
                known_names.append(name)
        except NotADirectoryError:
            pass

    # when you use a web camera
    # video = cv2.VideoCapture(0)

    # when you want to use video file
    video = cv2.VideoCapture('api/static/IMG_0909.MOV')

    # Read until video is completed
    while(video.isOpened()):
        # Find OpenCV version
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
        if int(major_ver) < 3:
            fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        else:
            fps = video.get(cv2.CAP_PROP_FPS)
        num_frames = 60

        for i in range(0, num_frames):
            ret, image = video.read()

        # when we are trying to detect a face on the images instead video
        # ret, image = video.read()
        locations = face_recognition.face_locations(
            image, number_of_times_to_upsample=0, model=MODEL)
        encodings = face_recognition.face_encodings(image,  locations)
        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            match = None
            if True in results:
                match = known_names[results.index(True)]
                top_left = (face_location[3], face_location[0] - 20)
                bottom_right = (face_location[1], face_location[2] + 15)
                color = [48, 10, 36]
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                top_left = (face_location[3], face_location[2] + 10)
                bottom_right = (face_location[1], face_location[2] + 50)
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                cv2.putText(image, match, (face_location[3] + 30, face_location[2] + 35),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), FONT_THICKNESS)

        frame = cv2.imencode('.jpg', image)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        # when we are trying to detect a face on the images instead video
        # cv2.imshow(filename, image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    gen()
