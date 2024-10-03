# This script deletes a random number of images from the specified folder. This is useful for creating a smaller dataset for testing purposes.

import random
import os

def delete_random_images(folder, N):
    """
    Deletes N random images from the specified folder.

    Parameters:
    folder (str): The path to the folder containing images.
    N (int): The number of images to delete.
    """
    images = os.listdir(folder)
    if len(images) < N:
        raise ValueError("N is greater than the number of images in the folder")

    images_to_delete = random.sample(images, N)
    for image in images_to_delete:
        os.remove(os.path.join(folder, image))



delete_random_images('Images\\Not Duck\\train\\images', 2500)

delete_random_images('Images\\Not Duck\\test\\images', 1300)

delete_random_images('Images\\Not Duck\\val\\images', 1300)
