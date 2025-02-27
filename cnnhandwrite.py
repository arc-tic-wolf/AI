import tensorflow as tf
from tensorflow import keras

def train_mnist_conv():
    # Please write your code only where you are indicated.
    # please do not remove model fitting inline comments.

    # YOUR CODE STARTS HERE
    class myCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self,epoch,logs={}):
            if(logs.get('accuracy')>.998):
                print("Reached 99.8% accuracy so cancelling training")
                self.model.stop_training=True
    callback=myCallback()
    # YOUR CODE ENDS HERE

    mnist = tf.keras.datasets.mnist
    (training_images, training_labels), (test_images, test_labels) = mnist.load_data()
    # YOUR CODE STARTS HERE
    training_images=training_images.reshape(60000, 28, 28, 1)/255.0
    test_images=test_images.reshape(10000, 28, 28, 1)/255.0
    # YOUR CODE ENDS HERE

    model = tf.keras.models.Sequential([
        
            # YOUR CODE STARTS HERE
            tf.keras.layers.Conv2D(64,(3,3),activation='relu',input_shape=(28,28,1)),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128,activation='relu'),
            tf.keras.layers.Dense(10,activation='softmax')

            # YOUR CODE ENDS HERE
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    # model fitting
    history = model.fit(
        # YOUR CODE STARTS HERE
        training_images,training_labels,epochs=20,callbacks=[callback]
        # YOUR CODE ENDS HERE
    )
    # model fitting
    return history.epoch, history.history['accuracy'][-1]

train_mnist_conv()