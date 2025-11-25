from torch import numel
from predict_and_detect import predict_and_detect
from take_photo import get_photo
from ultralytics import YOLO

MODEL = YOLO("yolo11n.pt")

def count_people_in_image(image):
    """
    Description: Given an image counts the number of people in it

    Args:
        image: cv2 image
    """
    _, number_of_people = predict_and_detect(MODEL, image, classes=[0])
    return number_of_people


def count_people():
    """
    Description: Captures an image from the camera and counts the number of people in it
    """
    image = get_photo()
    return count_people_in_image(image)


if __name__ == "__main__":
    num_people = count_people()
    print(f"Number of people detected: {num_people}")
