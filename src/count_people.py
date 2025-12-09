from predict_and_detect import predict_and_detect
from take_photo import get_photo
from ultralytics import YOLO
from cv2 import imwrite, imread

MODEL = YOLO("yolo11n.pt")


def count_people_in_image(image):
    """
    Description: Given an image counts the number of people in it

    Args:
        image: cv2 image
    """
    result_img, number_of_people = predict_and_detect(MODEL, image, classes=[0])
    return (result_img, number_of_people)

def count_people_in_image_path(path):
    """
    Description: Given an image counts the number of people in it

    Args:
        path: string
    """
    image = imread(path)
    result_img, number_of_people = predict_and_detect(MODEL, image, classes=[0])
    imwrite("img/processed_image.jpg", result_img)
    return (result_img, number_of_people)


def count_people():
    """
    Description: Captures an image from the camera and counts the number of people in it
    """
    image = get_photo()
    return count_people_in_image(image)[1]


def count_people_and_save():
    """
    Description: Captures an image from the camera and counts the number of people in it and saves it
    """
    image = get_photo()
    result_img, number_of_people = count_people_in_image(image)
    _ = imwrite("img/captured_image.jpg", result_img)
    return number_of_people


def live_video():
    """
    Description: Captures live video from the camera and counts the number of people in it
    """
    import cv2

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        result_img, number_of_people = count_people_in_image(frame)
        cv2.putText(
            result_img,
            f"People Count: {number_of_people}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )
        cv2.imshow("Live Video - Press Q to Quit", result_img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # num_people = count_people_and_save()
    # print(f"Number of people detected: {num_people}")
    live_video()
