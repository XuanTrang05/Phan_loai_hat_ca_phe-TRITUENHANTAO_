import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

IMG_SIZE = 224

model = tf.keras.models.load_model("coffee_classifier.h5")

def predict_coffee(img_path):
    img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]

    # ===== SỬA NHÃN TẠI ĐÂY (KHÔNG ĐỘNG PHẦN KHÁC) =====
    if prediction >= 0.5:
        return "Xanh (Unripe)", round(prediction * 100, 2)
    else:
        return "Chín (Ripe)", round((1 - prediction) * 100, 2)
