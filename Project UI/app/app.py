import base64
import io
import numpy as np
#import tensorflow as tf
from PIL import Image
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


def preprocess_image(image, target_size):
    image = image.resize(target_size)
#    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image


print(" * Loading Keras model...")
#model = tf.keras.models.load_model('diabetic.h5')
print(" * Model loaded!")


@app.route("/", methods=["GET"])
def index():
    return render_template('predict.html')


@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224, 224))

#    prediction = model.predict(processed_image).tolist()
    response = {
        "pred": {
            "l5": prediction[0][0],
            "l1": prediction[0][1],
            "l2": prediction[0][2],
            "l3": prediction[0][3],
            "l4": prediction[0][4],
        }
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
