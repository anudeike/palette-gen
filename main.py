import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # for showing a 3d representation

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
  Gives a pretty cool purple representation of the spectrum
  """
  rNorm = {
      'mean': 150,
      'std': 20
  }

  gNorm = {
      'mean': 20,
      'std': 10
  }

  bNorm = {
      'mean': 150,
      'std': 50
  }

  test_palettes = generateTestPalettes(rNorm, gNorm, bNorm, num_palettes=100)

  # flatten by only one dimension should get shape of (10, 3)
  flat = test_palettes.reshape(-1, test_palettes.shape[-1])
  print(flat.shape)

  # plot the flattened array
  plotColorsInSample(list(zip(*flat)), flat)




if __name__ == "__main__":
  main()