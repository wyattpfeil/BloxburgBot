import cv2
import numpy as np

picture1 = cv2.imread("./PizzaImages/Cheese.png")
picture2 = cv2.imread("./PizzaImages/Veggie.png")
picture1_norm = picture1/np.sqrt(np.sum(picture1**2))
picture2_norm = picture2/np.sqrt(np.sum(picture2**2))
print(np.sum(picture1_norm**2))