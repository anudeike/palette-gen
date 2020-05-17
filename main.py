import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # for showing a 3d representation

# keras imports


# set up the figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# seed the information
#np.random.seed(0)

def generateTestPalettes(rN, gN, bN, num_palettes, num_colors = 5):
    """
    :param rN: The mean and standard distribution for the red channel
    :param gN: The mean and standard deviation for the green channel
    :param bN: The mean and standard deviation for the blue channel
    :param num_palettes: the number of palettes to be generated
    :param num_colors: the number of colors in each palette - default is 5
    :return: returns a sample of palettes
    """

    sample = []
    for n in range(num_palettes):
        palette = []
        for c in range(num_colors):
            palette.append([min(abs(int(np.random.normal(rN['mean'], rN['std']))), 255),
                            min(abs(int(np.random.normal(gN['mean'], gN['std']))), 255),
                            min(abs(int(np.random.normal(bN['mean'], bN['std']))), 255)])

        sample.append(palette)


    # return it as an numpy array
    return np.asarray(sample)

# hsv generator
def generateTestPalettesHSV(hsvNorm, num_palettes, num_colors = 5):
    """
    format:
    [ h1, s1, v1, h2, s2, v2, h3, s3, v3, h4, s4, v4, h5, s5, v5, label ]

    :param hsvNorm: A dictionary defining the normal parameters of distrubtion for each channel of the graph
    :param num_palettes: the number of palettes
    :param num_colors: the amount of colors in each palette
    :return: a 3d matrix containing the palettes and all of their colors (with their values)
    """

    # wrap the hue value around 360
    # keep the sat and value values under 100

    # this is interesting

    # data set


    X = []
    Y = []

    for n in range(num_palettes // 2):
        palette = []
        # for each color
        for c in range(num_colors):

            # format: [ h, s, v, 1] 1 denotes that it is within the target distribution
            palette.append([int(np.random.normal(hsvNorm["hue"][0], hsvNorm["hue"][1])) % 360,
                            min(int(np.random.normal(hsvNorm["saturation"][0], hsvNorm["saturation"][1])), 100),
                            min(int(np.random.normal(hsvNorm["value"][0], hsvNorm["value"][1])), 100)])

        # flatten the array
        palette = np.asarray(palette)
        palette = palette.flatten()
        #print("this is: " + str(palette))

        # add the label
        Y = np.concatenate((Y, [1]))


        #palette = np.concatenate((palette, [1]))

        # add it to the X data
        X.append(palette)

    # adding noise to the sample
    for n in range(num_palettes // 2):
        palette = []
        for c in range(num_colors):

            # format: [ h, s, v, 0] 1 denotes that it is within the target distribution
            palette.append([int(np.random.normal(180, 90)) % 360,
                            min(abs(int(np.random.normal(50, 25))), 100),
                            min(abs(int(np.random.normal(50, 25))), 100)])

        # flatten the array
        palette = np.asarray(palette)
        palette = palette.flatten()

        # add the label
        Y = np.concatenate((Y, [0]))

        # print("this is noise: " + str(palette))

        X.append(palette)

    return np.asarray(X), np.asarray(Y)



def plotColorsInSample(sample_unzipped, raw_sample):
    """
    :param sample_unzipped: the sample generated in the generateTestPalettes function (unzipped)
    :param raw_sample: raw sample from the generator function
    :return:
    """

    #color = np.asarray([10, 252, 150, 10, 252, 150, 10, 252, 150, 10, 252, 150, 10, 252, 150, 10, 252, 150, 10, 252])
    ax.scatter(sample_unzipped[0], sample_unzipped[1], sample_unzipped[2], c = raw_sample/255)
    plt.show()


# compute sigmoid nonlinearity
def sigmoid(x, deriv=False):
    # if there is a derivative
    if deriv:
        return x * (1 - x)

    # else
    output = 1 / (1 + np.exp(-x))
    return output


# define the relu function
def relu(x, deriv = False):
    """
    :param x: the input matrix
    :param deriv: whether the derivative. default is False
    :return: returns a transformed numpy matrix
    """

    # this should work?
    if deriv:
        x[x <= 0] = 0
        x[x > 0] = 1
        return x

    # use a numpy universal function like np.maximum -> bunch online
    return np.maximum(0, x)

# define leaky relu
def leaky_relu(x, deriv=True, leakiness = 0.0):

    # main function

    # this works!
    x[x <= 0] = np.multiply(x[x <= 0], leakiness)

    return x

# create a function to generate the weights
def initialize_weights():
    pass


def network():

    # much of this code it taken from I am trask
    # input dataset
    X = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])

    # output dataset
    y = np.array([[0,
                   1,
                   1,
                   0]]).T

    np.random.seed(1)



    # set the alpha
    alpha = 10

    # setting the size of the hiddenLayer
    hidden_size = 3

    # xavier initlization
    synapse_0 = np.random.randn(X.shape[1], hidden_size) * np.sqrt(1 / (X.shape[1] - 1))
    synapse_1 = np.random.randn(hidden_size, y.shape[1]) * np.sqrt(1 / (X.shape[1] - 1))



    for j in range(10000):

        # Feed forward through layers 0, 1, and 2
        layer_0 = X
        layer_1 = sigmoid(np.dot(layer_0, synapse_0))
        layer_2 = sigmoid(np.dot(layer_1, synapse_1))

        # how much did we miss the target value?
        layer_2_error = layer_2 - y

        # print the error after a certain about of iterations
        if (j % 1000) == 0:
            print ("Error after " + str(j) + " iterations:" + str(np.mean(np.abs(layer_2_error))))

        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        layer_2_delta = layer_2_error * sigmoid(layer_2, True)

        # how much did each l1 value contribute to the l2 error (according to the weights)?
        layer_1_error = layer_2_delta.dot(synapse_1.T)

        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        layer_1_delta = layer_1_error * sigmoid(layer_1, True)

        # gradient descent happens here
        synapse_1 -= alpha * (layer_1.T.dot(layer_2_delta))
        synapse_0 -= alpha * (layer_0.T.dot(layer_1_delta))

    print("output after training: ")
    print(layer_2.shape)

# much of this code it taken from I am trask
def network_relu(leaky_relu = False):

    # input dataset
    X = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])

    # output dataset
    y = np.array([[0,
                   1,
                   1,
                   0]]).T

    np.random.seed(1)



    # set the alpha
    alpha = 0.1

    # setting the size of the hiddenLayer
    hidden_size = 3

    # xavier initlization
    synapse_0 = np.random.randn(X.shape[1], hidden_size) * np.sqrt(1 / (X.shape[1] - 1))
    synapse_1 = np.random.randn(hidden_size, y.shape[1]) * np.sqrt(1 / (X.shape[1] - 1))

    for j in range(10000):

        # Feed forward through layers 0, 1, and 2
        layer_0 = X
        layer_1 = relu(np.dot(layer_0, synapse_0))
        layer_2 = relu(np.dot(layer_1, synapse_1))

        # how much did we miss the target value?
        layer_2_error = layer_2 - y

        # print the error after a certain about of iterations
        if (j % 1000) == 0:
            print ("Error after " + str(j) + " iterations:" + str(np.mean(np.abs(layer_2_error))))

        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        layer_2_delta = layer_2_error * relu(layer_2, True)

        # how much did each l1 value contribute to the l2 error (according to the weights)?
        layer_1_error = layer_2_delta.dot(synapse_1.T)

        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        layer_1_delta = layer_1_error * relu(layer_1, True)

        # gradient descent happens here
        synapse_1 -= alpha * (layer_1.T.dot(layer_2_delta))
        synapse_0 -= alpha * (layer_0.T.dot(layer_1_delta))

    print("output after training: ")
    print(layer_2)



def main():
  # generate a bunch of test palettes with specified means and std_dev
  # details of the distributions

  """
  Gives a pretty cool purple representation of the spectrum:

  instead of using RGB, lets use HSV
  - will need to create a separate generator

  """


  # dictionary for the HSV
  hsvNorm = {
      "hue": (120, 20),
      "saturation": (70, 10), # in percentages
      "value": (50, 15) # in percentages
  }

  #test_pals = generateTestPalettesHSV(hsvNorm, 10)

  # (X, Y)
  #print(test_pals[1])

  # call the network function
  #
  #network_relu()

  ex = np.array([[0.41287266, -0.73082379, 0.78215209],
                 [0.76983443, 0.46052273, 0.4283139],
                 [-0.18905708, 0.57197116, 0.53226954]])

  print(leaky_relu(ex))

if __name__ == "__main__":
  main()