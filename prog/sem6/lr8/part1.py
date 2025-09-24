import cv2

def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]

    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
    net.setInput(blob)
    detections = net.forward()

    faceBoxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            faceBoxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)
    return frameOpencvDnn, faceBoxes


def process_image(image_path, faceNet):
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"Ошибка: не удалось загрузить изображение {image_path}")
        return

    resultImg, faceBoxes = highlightFace(faceNet, frame)

    if not faceBoxes:
        print("Лица не распознаны")
    else:
        print(f"Распознано лиц: {len(faceBoxes)}")

    cv2.imshow("Face detection", resultImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def process_camera(faceNet):
    video = cv2.VideoCapture(0)
    while cv2.waitKey(1) < 0:
        hasFrame, frame = video.read()
        if not hasFrame:
            cv2.waitKey()
            break

        resultImg, faceBoxes = highlightFace(faceNet, frame)

        if not faceBoxes:
            print("Лица не распознаны")

        cv2.imshow("Face detection", resultImg)

    video.release()
    cv2.destroyAllWindows()


def main():
    faceProto = "models/opencv_face_detector.pbtxt"
    faceModel = "models/opencv_face_detector_uint8.pb"
    faceNet = cv2.dnn.readNet(faceModel, faceProto)

    mode = input("Выберите режим работы (1 - камера, 2 - изображение): ")

    if mode == "1":
        process_camera(faceNet)
    elif mode == "2":
        image_path = input("Введите имя файла изображения: ")
        process_image(image_path, faceNet)
    else:
        print("Неверный выбор режима")


if __name__ == "__main__":
    main()