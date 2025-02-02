import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

# ----------------------------
# Step 1: Image Preprocessing
# ----------------------------

def preprocess_image(image_path):
    """Preprocess the image: Grayscale, CLAHE, Gaussian Blur, Resize."""
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(gray_image)
    
    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(enhanced_image, (5, 5), 0)
    
    # Resize the image for the model input (128x128)
    resized_image = cv2.resize(blurred_image, (128, 128))
    normalized_image = resized_image.astype('float32') / 255.0
    normalized_image = np.expand_dims(normalized_image, axis=-1)  # Add channel dimension
    return normalized_image

# ----------------------------
# Step 2: Define the CNN Model
# ----------------------------

def build_model():
    """Build and compile the CNN model."""
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')  # Binary classification: vein or no vein
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# ----------------------------
# Step 3: Load Dataset and Train the Model
# ----------------------------

def train_model():
    """Train the CNN model on the dataset."""
    # Load and preprocess the dataset
    train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    train_generator = train_datagen.flow_from_directory(
        'dataset/train',
        target_size=(128, 128),
        batch_size=32,
        color_mode='grayscale',
        class_mode='binary',
        subset='training'
    )

    validation_generator = train_datagen.flow_from_directory(
        'dataset/train',
        target_size=(128, 128),
        batch_size=32,
        color_mode='grayscale',
        class_mode='binary',
        subset='validation'
    )

    # Build and train the model
    model = build_model()
    model.fit(
        train_generator,
        epochs=10,
        validation_data=validation_generator
    )

    # Save the model for later use
    model.save('vein_detection_model.h5')
    print("Model trained and saved as 'vein_detection_model.h5'.")

# ----------------------------
# Step 4: Vein Detection on New Images
# ----------------------------

def predict_vein(image_path, model_path='vein_detection_model.h5'):
    """Predict whether a vein is detected in the image."""
    # Load the trained model
    model = load_model(model_path)

    # Preprocess the input image
    processed_image = preprocess_image(image_path)

    # Make a prediction
    prediction = model.predict(np.expand_dims(processed_image, axis=0))[0][0]

    # Display the result
    if prediction > 0.5:
        print(f"Vein Detected! (Confidence: {prediction:.2f})")
    else:
        print(f"No Vein Detected. (Confidence: {1 - prediction:.2f})")

# ----------------------------
# Step 5: Visualize Image Processing Pipeline
# ----------------------------

def visualize_pipeline(image_path):
    """Visualize the preprocessing pipeline."""
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(gray_image)
    
    # Gaussian Blur
    blurred_image = cv2.GaussianBlur(enhanced_image, (5, 5), 0)
    
    # Edge Detection (Canny)
    edges = cv2.Canny(blurred_image, 100, 200)

    # Plot results
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 4, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    
    plt.subplot(1, 4, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Grayscale')
    
    plt.subplot(1, 4, 3)
    plt.imshow(enhanced_image, cmap='gray')
    plt.title('Enhanced (CLAHE)')
    
    plt.subplot(1, 4, 4)
    plt.imshow(edges, cmap='gray')
    plt.title('Edges (Canny)')
    
    plt.tight_layout()
    plt.show()

# ----------------------------
# Example Usage
# ----------------------------

if __name__ == "__main__":
    # Uncomment to train the model
    # train_model()
    
    # Test on a new image
    test_image_path = 'dataset/test/new_image.png'
    predict_vein(test_image_path)

    # Visualize preprocessing steps
    visualize_pipeline(test_image_path)
