import os
import numpy as np
from PIL import Image


def load_images_as_np_array(path, arquivo):
  return np.array(Image.open(os.path.join(path, arquivo)))