# load and plot monthly airline passengers dataset
from pandas import read_csv
import warnings
warnings.simplefilter("ignore")
%matplotlib inline
from matplotlib import pyplot
# load
series = read_csv('monthly-airline-passengers.csv', header=0, index_col=0)
# summarize shape
print(series.shape)
# plot
pyplot.plot(series)
pyplot.xticks([])
pyplot.show()