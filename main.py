import numpy as np

# seed the information
np.random.seed(0)

def generateFromGaussian(mean, std):
  return np.random.normal(mean, std, (2,5,3))


def main():

  print(generateFromGaussian(0,1).shape)

  return


if __name__ == "__main__":
  main()