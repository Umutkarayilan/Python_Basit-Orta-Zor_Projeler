# Proje Açıklaması: TensorFlow kullanarak basit bir sinir ağı modeli oluşturun ve MNIST veri seti üzerinde el yazısı rakamları sınıflandırın.
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# Veri setini yükler
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Veriyi normalize eder
train_images, test_images = train_images / 255.0, test_images / 255.0

# Modeli oluşturur
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

# Modeli derler
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Modeli eğitir
history = model.fit(train_images, train_labels, epochs=5, 
                    validation_data=(test_images, test_labels))

# Model performansını görselleştirir
plt.plot(history.history['accuracy'], label='Eğitim Doğruluğu')
plt.plot(history.history['val_accuracy'], label='Doğrulama Doğruluğu')
plt.xlabel('Epoch')
plt.ylabel('Doğruluk')
plt.legend()
plt.show()

# Modeli değerlendirir
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest Doğruluğu:', test_acc)


# TensorFlow ve Keras kullanılarak derin öğrenme modelleri oluşturulur.
# MNIST veri seti ile el yazısı rakamların sınıflandırılması yapılır.
# Sequential model ile katmanlar ardışık olarak eklenir.
# Dropout katmanı ile aşırı öğrenme (overfitting) önlenir.
# Modelin eğitimi ve doğrulaması sırasında performans grafiklerle izlenir.