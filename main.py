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

  test_pals = generateTestPalettesHSV(hsvNorm, 10)

  # (X, Y)
  print(test_pals[1])




if __name__ == "__main__":
  main()