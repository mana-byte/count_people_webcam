import cv2

def predict(chosen_model, img, classes=[0], conf=0.5):
    if classes != []:
        results = chosen_model.predict(img, classes=classes, conf=conf, device="cpu")
    else:
        results = chosen_model.predict(img, conf=conf, device="cpu")
    return results


def predict_and_detect(
    chosen_model, img, classes=[0], conf=0.5, rectangle_thickness=2, text_thickness=1
):
    results = predict(chosen_model, img, classes, conf=conf)
    number_of_results = 0
    for result in results:
        for box in result.boxes:
            number_of_results += 1
            cv2.rectangle(
                img,
                (int(box.xyxy[0][0]), int(box.xyxy[0][1])),
                (int(box.xyxy[0][2]), int(box.xyxy[0][3])),
                (0, 0, 255),
                rectangle_thickness,
            )
            cv2.putText(
                img,
                f"{result.names[int(box.cls[0])]}",
                (int(box.xyxy[0][0]), int(box.xyxy[0][1]) - 10),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (255, 0, 0),
                text_thickness,
            )
    return img, number_of_results
