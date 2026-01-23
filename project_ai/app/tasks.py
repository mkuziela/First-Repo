import cv2
import os


PROTOTXT = "ssd_mobilenet_v2_coco.pbtxt"
MODEL = "frozen_inference_graph.pb"


def detect_people_on_image(image_path, output_path=None):
    if not os.path.exists(MODEL) or not os.path.exists(PROTOTXT):
        print("BŁĄD: Brak plików modelu! Uruchom najpierw setup_models.py")
        return 0

    image = cv2.imread(image_path)
    if image is None:
        return 0

    (h, w) = image.shape[:2]

    net = cv2.dnn.readNetFromTensorflow(MODEL, PROTOTXT)

    blob = cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True, crop=False)
    net.setInput(blob)

    detections = net.forward()

    person_count = 0


    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.4:
            class_id = int(detections[0, 0, i, 1])

            if class_id == 1:
                person_count += 1

                if output_path:

                    box = detections[0, 0, i, 3:7] * [w, h, w, h]
                    (startX, startY, endX, endY) = box.astype("int")

                    label = f"Person: {confidence * 100:.1f}%"
                    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

                    label_size, baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
                    cv2.rectangle(image, (startX, startY - label_size[1] - 10), (startX + label_size[0], startY),
                                  (0, 255, 0), cv2.FILLED)
                    cv2.putText(image, label, (startX, startY - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        cv2.imwrite(output_path, image)

    return person_count