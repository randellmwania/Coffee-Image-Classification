# Import necessary modules
from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf

# Create a Flask application instance
app = Flask(__name__)

# Load the saved model
model = tf.keras.models.load_model('Models\model_11.h5')

# Define class names
class_names = ["Cercospora", "Healthy", "Leaf Rust", "Phoma"]

# Define recommendations for each disease
disease_recommendations = {
    "Cercospora": {
        "cause": "Cercospora can be caused by fungal pathogens such as Cercospora coffeicola. It commonly occurs in warm and humid conditions.",
        "cure": "To treat Cercospora, use fungicides containing copper. Additionally, maintain proper cultural practices such as pruning and disposing of infected plant parts.",
        "Learn More": "https://apps.lucidcentral.org/pppw_v12/text/web_full/entities/coffee_browneye_spot_142.htm"
    },
    "Leaf Rust": {
        "cause": "Leaf Rust is caused by the fungal pathogen Hemileia vastatrix. It spreads rapidly in warm and moist conditions.",
        "cure": "To treat Leaf Rust, prune the affected leaves and apply fungicides. Implement cultural practices such as proper spacing of plants and maintaining good airflow to reduce humidity.",
        "Learn More": "https://bioprotectionportal.com/resources/coffee-rust-symptoms-causes-and-solutions/"
    },
    "Phoma": {
        "cause": "Phoma is caused by the fungal pathogen Phoma spp. It thrives in cool and wet conditions, especially during periods of high humidity.",
        "cure": "To treat Phoma, remove and destroy affected plant parts. Apply fungicides containing active ingredients such as azoxystrobin or copper hydroxide. Implement proper irrigation practices to reduce moisture levels around the plants.",
        "Learn More": "https://www.plantwise.org/en/pest/coffee/fungal-diseases/phoma-blight"
    },
    "Healthy": {
        "cause": "No disease detected. Continue preventive measures and good cultural practices to maintain plant health.",
        "cure": "No cause for concern.",
    }
}

# Function to preprocess input image


def preprocess_image(image):
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Prediction endpoint


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file found'})

        file = request.files['file']
        image = Image.open(file)
        processed_image = preprocess_image(image)

        # Make prediction
        prediction = model.predict(processed_image)

        # Get predicted class index and name
        predicted_class_index = np.argmax(prediction)
        predicted_class_name = class_names[predicted_class_index]

        # Get recommendation for the predicted disease
        recommendation = disease_recommendations.get(
            predicted_class_name, "No specific recommendation available.")

        # Prepare response
        response = {
            'prediction': predicted_class_name,
            'recommendation': recommendation
        }

        return jsonify(response)

    return render_template('index.html')


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
