import tensorflow as tf
from tensorflow import keras




def train_mnist():

    class myCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs={}):
            if(logs.get('accuracy') > 0.99):
                print("\nReached 99% accuracy so cancelling training")
                self.model.stop_training = True
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    callback = myCallback()

    model = tf.keras.models.Sequential([keras.layers.Flatten(input_shape=(28, 28)),
                                        keras.layers.Dense(
                                            256, activation=tf.nn.relu),
                                        keras.layers.Dense(10, activation=tf.nn.softmax)])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    history = model.fit(x_train, y_train, epochs=10, callbacks=[callback])
    # model fitting
    return history.epoch, history.history['accuracy'][-1]


train_mnist()
