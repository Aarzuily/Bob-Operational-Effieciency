import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate sample data (replace with your actual dataset)
X = np.random.rand(100, 5)  # Features
y = np.random.randint(0, 2, size=(100,))  # Target labels (0 or 1)

# Define a simple neural network model
model = Sequential([
    Dense(10, input_shape=(5,), activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model (replace with actual training process)
model.fit(X, y, epochs=10, batch_size=32)

# Save the trained model
model.save('loan_approval_model.h5')
