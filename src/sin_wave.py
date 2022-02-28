# source https://github.com/avantcontra/coding-druid/blob/master/01-Math-Trig-Function/sine-python/01-math-sine-python.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# class holds base definition of sine function
class AnimBase(object):
    def __init__(self):
        # define plot
        self.fig, self.ax = plt.subplots(1,1)
        # define sine function
        self.x = np.linspace(0, 2*np.pi, 100)
        self.y = np.sin(self.x)


class SinPlot(AnimBase):
    def __init__(self):
        super(SinPlot, self).__init__()
        # window settings
        self.ax.set_xlim([0, 2*np.pi])
        self.ax.set_ylim([-2.5, 2.5])

    def plot_graph(self):    
        self.sineLine, = self.ax.plot([], [], linewidth=4)
        self.sineDot, = self.ax.plot([], [], 'o', color='#ff0000')

    def __animation_func(self, i):
        self.sineLine.set_data(self.x[:i], self.y[:i])
        self.sineDot.set_data(self.x[i], self.y[i])
        
    def start_animation(self):    
        anim = animation.FuncAnimation(self.fig, self.__animation_func, frames=len(self.x), interval=50)
        return anim


class UnitCirclePlot(AnimBase):
    def __init__(self):
        super(UnitCirclePlot, self).__init__()
        # window settings
        self.ax.set_xlim([-2.5, 2.5])
        self.ax.set_ylim([-2.5, 2.5])

    def plot_graph(self):    
        self.circleLine, = self.ax.plot([], [],linewidth=4)
        self.circleDot, = self.ax.plot([], [], 'o', color='black')

    def __animation_func(self, i):
        self.circleLine.set_data(np.cos(self.x[:i]), np.sin(self.x[:i]))
        self.circleDot.set_data(np.cos(self.x[i]), np.sin(self.x[i]))
        
    def start_animation(self):    
        anim = animation.FuncAnimation(self.fig, self.__animation_func, frames=len(self.x), interval=50)
        return anim        


if __name__ == "__main__":
    # sine wave
    plotsin = SinPlot()
    # prepare plot
    plotsin.plot_graph()
    ani = plotsin.start_animation()

    # unitcircle
    plotcirc = UnitCirclePlot()
    # prepare plot
    plotcirc.plot_graph()
    anim = plotcirc.start_animation()

    plt.show()