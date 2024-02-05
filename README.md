# NumpAI

A hard-coded NumPy implementation of a Convolutional Neural Network (CNN) for the MNIST dataset.

4730 Machine Learning Fall 2022 Project I Repository -- We misread the assignment and thought we were supposed to implement a CNN from scratch. We were not. But now we have a hard-coded NumPy implementation of a CNN for the MNIST dataset. It is not the most accurate (~70%), but it works.

This is a collaborative project between [Mathew Pellarin](https://github.com/Matp101) and I.

## Running the Project

There are two CNNs implemented here:

1. `main.py` is hard coded in NumPy. It is less accurate, but works enough that we are happy with it, and is completely done from scratch.
2. phase_1.ipynb, which uses a sequential Keras model. It is more accurate(>98%), but is not completely done from scratch. This is an example of how to use Keras to implement a CNN.

### Installing Requirements

To install the requirements, run the following command:

```bash
pip install -r requirements.txt
```

## Notes on the dataset

- These images are 28x28 pixels, grayscale, and centered.
