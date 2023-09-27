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

class DataSource:
    name: str
    filename: str
def datasource(name, filename):
    ds = DataSource()
    ds.name = name
    ds.filename = filename
    return ds

def gen_graph(output, name, datanames):
    print('![' + name + '](graphs/' + output + '.png)')
    xs = numpy.linspace(0, 32, 2000)
    pyplot.figure(figsize = (width, height))
    for it in datanames:
        data = read_data(it.filename)
        density = gaussian_kde(data)
        density.covariance_factor = lambda : 0.125
        density._compute_covariance()
        pyplot.plot(xs, density(xs), label = it.name)
    pyplot.legend()
    pyplot.title(name)
    pyplot.gca().axes.get_yaxis().set_visible(False)
    pyplot.xticks(numpy.arange(0, 32, 1.0))
    pyplot.savefig(os.path.join('graphs', output + '.png'), bbox_inches = 'tight', pad_inches = 0.1)
    pyplot.close()

gen_graph('emptymap_160fps', '160 fps, empty map', [
    datasource('CS:GO', 'csgo_emptymap_160fps'), 
    datasource('CS2 (low latency disabled)', 'cs2_emptymap_lowlatency-disabled_160fps'), 
    datasource('CS2 (low latency enabled)', 'cs2_emptymap_lowlatency-enabled_160fps'), 
    datasource('CS2 (low latency boost)', 'cs2_emptymap_lowlatency-boost_160fps'),
])

gen_graph('emptymap_240fps', '240 fps, empty map', [
    datasource('CS:GO', 'csgo_emptymap_240fps'), 
    datasource('CS2 (low latency disabled)', 'cs2_emptymap_lowlatency-disabled_240fps'), 
    datasource('CS2 (low latency enabled)', 'cs2_emptymap_lowlatency-enabled_240fps'), 
    datasource('CS2 (low latency boost)', 'cs2_emptymap_lowlatency-boost_240fps'),
])

gen_graph('emptymap_300fps', '300 fps, empty map', [
    datasource('CS:GO', 'csgo_emptymap_300fps'), 
    datasource('CS2 (low latency disabled)', 'cs2_emptymap_lowlatency-disabled_300fps'), 
    datasource('CS2 (low latency enabled)', 'cs2_emptymap_lowlatency-enabled_300fps'), 
    datasource('CS2 (low latency boost)', 'cs2_emptymap_lowlatency-boost_300fps'),
])

gen_graph('emptymap_480fps', '480 fps, empty map', [
    datasource('CS:GO', 'csgo_emptymap_480fps'), 
    datasource('CS2 (low latency disabled)', 'cs2_emptymap_lowlatency-disabled_480fps'), 
    datasource('CS2 (low latency enabled)', 'cs2_emptymap_lowlatency-enabled_480fps'), 
    datasource('CS2 (low latency boost)', 'cs2_emptymap_lowlatency-boost_480fps'),
])

gen_graph('emptymap_720fps', '720 fps, empty map', [
    datasource('CS:GO', 'csgo_emptymap_720fps'), 
    datasource('CS2 (low latency disabled)', 'cs2_emptymap_lowlatency-disabled_720fps'), 
    datasource('CS2 (low latency enabled)', 'cs2_emptymap_lowlatency-enabled_720fps'), 
    datasource('CS2 (low latency boost)', 'cs2_emptymap_lowlatency-boost_720fps'),
])

gen_graph('emptymap_236fps_gsync', 'GSYNC (236 fps), empty map', [
    datasource('CS:GO', 'csgo_emptymap_236fps_gsync'), 
    datasource('CS2 (low latency disabled)', 'cs2_emptymap_lowlatency-disabled_236fps_gsync'), 
    datasource('CS2 (low latency enabled)', 'cs2_emptymap_lowlatency-enabled_236fps_gsync'), 
    datasource('CS2 (low latency boost)', 'cs2_emptymap_lowlatency-boost_236fps_gsync'),
])

gen_graph('inferno_160fps', '160 fps, inferno', [
    datasource('CS:GO', 'csgo_inferno_160fps'), 
    datasource('CS2 (low latency disabled)', 'cs2_inferno_lowlatency-disabled_160fps'), 
    datasource('CS2 (low latency enabled)', 'cs2_inferno_lowlatency-enabled_160fps'), 
    datasource('CS2 (low latency boost)', 'cs2_inferno_lowlatency-boost_160fps'),
])

gen_graph('inferno_240fps', '240 fps, inferno', [
    datasource('CS:GO', 'csgo_inferno_240fps'), 
    datasource('CS2 (low latency disabled)', 'cs2_inferno_lowlatency-disabled_240fps'), 
    datasource('CS2 (low latency enabled)', 'cs2_inferno_lowlatency-enabled_240fps'), 
    datasource('CS2 (low latency boost)', 'cs2_inferno_lowlatency-boost_240fps'),
])

gen_graph('inferno_300fps', '300 fps, inferno', [
    datasource('CS:GO', 'csgo_inferno_300fps'), 
    datasource('CS2 (low latency disabled)', 'cs2_inferno_lowlatency-disabled_300fps'), 
    datasource('CS2 (low latency enabled)', 'cs2_inferno_lowlatency-enabled_300fps'), 
    datasource('CS2 (low latency boost)', 'cs2_inferno_lowlatency-boost_300fps'),
])

gen_graph('inferno_unlocked-fps', 'unlocked fps, inferno', [
    datasource('CS:GO (~560fps)', 'csgo_inferno_unlocked-fps'), 
    datasource('CS:GO (400fps)', 'csgo_inferno_400fps'), 
    datasource('CS2 (low latency disabled, ~400fps)', 'cs2_inferno_lowlatency-disabled_unlocked-fps'), 
    datasource('CS2 (low latency enabled, ~400fps)', 'cs2_inferno_lowlatency-enabled_unlocked-fps'), 
    datasource('CS2 (low latency boost, ~400fps)', 'cs2_inferno_lowlatency-boost_unlocked-fps'),
])

gen_graph('inferno_236fps_gsync', 'GSYNC (236 fps), inferno', [
    datasource('CS:GO', 'csgo_inferno_236fps_gsync'), 
    datasource('CS2 (low latency disabled)', 'cs2_inferno_lowlatency-disabled_236fps_gsync'), 
    datasource('CS2 (low latency enabled)', 'cs2_inferno_lowlatency-enabled_236fps_gsync'), 
    datasource('CS2 (low latency boost)', 'cs2_inferno_lowlatency-boost_236fps_gsync'),
])

gen_graph('inferno_vsync', 'VSYNC, inferno', [
    datasource('CS:GO (double buffer)', 'csgo_inferno_vsync-doublebuffer'), 
    datasource('CS:GO (triple buffer)', 'csgo_inferno_vsync-triplebuffer'), 
    datasource('CS2 (low latency enabled)', 'cs2_inferno_lowlatency-enabled_vsync'), 
])

gen_graph('inferno_fullscreen-windowed', '300 fps, inferno, fullscreen windowed', [
    datasource('CS:GO (tear free)', 'csgo_inferno_300fps_fullscreen-windowed'), 
    datasource('CS2 (NOT tear free)', 'cs2_inferno_lowlatency-enabled_300fps_fullscreen-windowed'), 
])
