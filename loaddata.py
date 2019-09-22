import numpy as np
from urllib.request import urlopen

# url with dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"

# download the file
raw_data = urlopen(url)

# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")

# separate the data from the target attributes
X = dataset[:, 0:7]
y = dataset[:, 8]

print(y.shape)