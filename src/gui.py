import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler 
from sin_wave import SinPlot, UnitCirclePlot


class SideMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        # slider
        lbl_amp = tk.Label(self, text="Amplitude:")
        sld_omega = tk.Scale(self, from_=0.1, to=1.0, resolution=0.1, orient="horizontal")
        # button
        btn_quit = tk.Button(self, text="Quit", command=self.quit) 
        lbl_amp.grid(row=0, column=0)
        sld_omega.grid(row=0, column=1)
        btn_quit.grid(row=1, columnspan=2)

class MatPlot(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="orange")
        self.parent = parent
        # init unit circle plot
        circ_canvas = self.disp_animation(UnitCirclePlot, 0)
        # init sine wave plot
        sine_canvas = self.disp_animation(SinPlot, 1)
        self.update_toolbar(circ_canvas)
        self.update_toolbar(sine_canvas) 
    

    def disp_animation(self, plot_class, side):
        plotsin = plot_class()
        # prepare plot
        plotsin.plot_graph()
        ani = plotsin.start_animation()
        canvas = FigureCanvasTkAgg(plotsin.fig, self)
        canvas.draw()
        canvas._tkcanvas.grid(row=0, column=side)
        return canvas

    def update_toolbar(self, plot_canvas):
        toolbar = NavigationToolbar2Tk(plot_canvas, self, pack_toolbar=False) 
        toolbar.update()         
  

        
class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # init other windows
        self.side_menu = SideMenu(self)
        self.matplot = MatPlot(self)

        # arrange frames
        self.matplot.grid(row=0)
        self.side_menu.grid(row=1)

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()