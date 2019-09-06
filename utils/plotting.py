import matplotlib.pylab as plt
from numpy import linspace


def plot_wf(wf, sr=None, **kwargs):
    if sr is not None:
        plt.plot(linspace(start=0, stop=len(wf) / float(sr), num=len(wf)), wf, **kwargs)
    else:
        plt.plot(wf, **kwargs)
