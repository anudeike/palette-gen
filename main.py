import numpy as np

# seed the information
np.random.seed(0)

def generateTestPalettes(rN, gN, bN, num_palettes, num_colors = 5):
    """
    :param rN: The mean and standard distribution for the red channel
    :param gN: The mean and standard deviation for the green channel
    :param bN: The mean and standard deviation for the blue channel
    :param num_palettes: the number of palettes to be generated
    :param num_colors: the number of colors in each palette - default is 5
    :return: returns a sample of palettes
    """

    palettes = []
    for n in range(num_palettes):
        palette = []
        for c in range(num_colors):
            palette.append([int(np.random.normal(rN['mean'], rN['std'])), int(np.random.normal(gN['mean'], gN['std'])), int(np.random.normal(bN['mean'], bN['std']))])

        palettes.append(palette)

    # return it as an numpy array
    return np.asarray(palettes)

def main():
  # generate a bunch of test palettes with specified means and std_dev

  # details of te distributions
  rNorm = {
      'mean': 15,
      'std': 3
  }

  gNorm = {
      'mean': 230,
      'std': 3
  }

  bNorm = {
      'mean': 150,
      'std': 7
  }

  test_palettes = generateTestPalettes(rNorm, gNorm, bNorm, num_palettes=2)

  print(test_palettes)


if __name__ == "__main__":
  main()