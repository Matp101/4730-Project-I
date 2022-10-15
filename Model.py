# %%
# load the dataset

from tensorflow.keras.datasets import mnist
from progressbar import ProgressBar as progressbar
import numpy as np
import multiprocessing as mp
from itertools import product

from layers.Conv2D import Conv2D
from layers.Pooling import Pooling
from layers.Dense import Dense
from layers.Flatten import Flatten

# %%
# import the data
(train_X, train_y), (test_X, test_y) = mnist.load_data()

# scale the data
train_X, test_X = train_X / 255.0, test_X / 255.0


# reduce the size of the dataset
train_X, test_X = train_X[:10000], test_X[:1000]
train_y, test_y = train_y[:10000], test_y[:1000]

# need the fourth dimension to represent the number of channels
train_X = train_X.reshape(-1, 28, 28, 1)
test_X = test_X.reshape(-1, 28, 28, 1)

print('Train: X=%s, y=%s' % (train_X.shape, train_y.shape))
print('Test: X=%s, y=%s' % (test_X.shape, test_y.shape))

# %%
# define the model
model = []

model.append(Conv2D(32, 2, 1, 1, activation='relu'))
model.append(Pooling(2, 2, 'max'))
model.append(Flatten())

# determine the number of input features by running one forward pass on one image
dims = train_X[0]
dims = dims.reshape(1, *dims.shape)
for layer in model:
    dims = layer.forward(dims)

model.append(Dense(np.prod(dims.shape[1:]), 128, activation='relu'))
model.append(Dense(128, 10, activation='softmax'))

for layer in model[3:]:
    dims = layer.forward(dims)

# %%


def predict(X, model):
    # forward pass on a single image
    for layer in model:
        X = layer.forward(X)
    return X


def train(X, y, model, lr=0.01, epochs=10):

    # need to make epochs work
    # need to do forward passes chunks of mp.cpu_count() images at a time
    # when each forward pass is done, do a backward pass on the same chunk of images
    loss = 0
    chunksize = 10
    # create a one-hot vector of y
    y = np.eye(10)[y]

    for epoch in range(epochs):
        p = progressbar(
            max_value=X.shape[0], prefix='epoch %d ' % epoch, redirect_stdout=True)
        # break into chunks of at most mp.cpu_count() images
        for i in range(0, len(X), chunksize):
            # forward pass
            y_pred = predict(X[i:min(X.shape[0], i+chunksize)], model)

            # gradient
            grad_y_pred = np.abs(y_pred - y[i:min(X.shape[0], i+chunksize)])

            loss = np.square(grad_y_pred).sum()
            print(loss)

            # backward pass
            for layer in reversed(model):
                grad_y_pred = layer.backward(grad_y_pred, lr)

            p.update(i)
        p.finish()


# %%
# train the model
train(train_X, train_y, model)