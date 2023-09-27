import matplotlib.pyplot as pyplot
import numpy
import os
from scipy.stats import gaussian_kde

width = 13
height = 3

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

def read_data(name):
    with open(os.path.join('data', name + '.txt'), 'r') as file:
        text = file.read()
        split = text.strip().split(',')
        return [float(x) for x in split if x]
    
def gen_graph(name):
    print('![' + name + '](graphs/' + name + '.png)')
    data = read_data(name)
    numsamples = len(data)
    xs = numpy.linspace(0, max(32, max(data)), 2000)
    density = gaussian_kde(data)
    density.covariance_factor = lambda : 0.125
    density._compute_covariance()
    pyplot.figure(figsize = (width, height))
    pyplot.plot(xs, density(xs))
    pyplot.title(name.replace('_', ' | ') + ' | ' + str(numsamples) + ' samples')
    pyplot.gca().axes.get_yaxis().set_visible(False)
    pyplot.xticks(numpy.arange(0, max(32, max(data)), 1.0))
    pyplot.savefig(os.path.join('graphs', name + '.png'), bbox_inches = 'tight', pad_inches = 0)
    pyplot.close()

for item in os.listdir('data'):
    if os.path.isfile(os.path.join('data', item)):
        filename, ext = os.path.splitext(item)
        gen_graph(filename)
