import tkinter as tk

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from .callbacks import run_simulation


class MainWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.model_p_dict = []

        # Left Panel
        self._draw_left_panel()

        # For now I skip drawing the right panel, I use the default
        # visualization in Simulate
        # Right Panel (for the plot)
        # self._draw_right_panel()
        


    def _draw_left_panel(self):
        input_entries = []
        frm_l = tk.Frame(master=self,
                         width=30,
                         height=50)
        
        # First three inputs
        for i, (label_text, default_value) \
                in enumerate(zip(['Simulation time [min] \u207D\u00B9\u207E',
                                  'Inter-spine distance [um] \u207D\u00B2\u207E',
                                  'Spine number \u207D\u00B3\u207E'],
                                 [40,5,200])):
            frame = tk.Frame(master=frm_l)
            tk.Label(master=frame, text=label_text, width=25, anchor='w').pack(side=tk.LEFT)
            entry = tk.Entry(master=frame, width=10)
            entry.insert(0,str(default_value))
            entry.pack(side=tk.LEFT)
            input_entries.append(entry)
            frame.grid(row=i, column=0)

        # Stimulus scheme description
        tk.Label(master=frm_l, 
                 text=' Logic: start, number, stride',
                 font='Helvetica 8 italic',
                 anchor='w').grid(sticky='we',
                                  row=3,
                                  column=0,
                                  pady=(20,0))

        # Stimulus scheme
        frame = tk.Frame(master=frm_l)
        tk.Label(master=frame, 
                 text='Stimulus scheme \u207D\u2074\u207B\u2075\u207B\u2076\u207E',
                 width=25, 
                 anchor='w').pack(side=tk.LEFT)

        # We append all the entries to self
        for _, default_value in enumerate([20,10,2]):
            entry = tk.Entry(master=frame, width=3)
            entry.insert(0, str(default_value))
            entry.pack(side=tk.LEFT)
            input_entries.append(entry)

        frame.grid(row=4, column=0)

        # Finally, the button
        tk.Button(master=frm_l,
                  text='RUN',
                  command=lambda: run_simulation(input_entries)).grid(row=5,column=0, sticky='we')

        # Window to copypaste the pardict
        frame = tk.Frame(master=frm_l)
        
        tk.Label(master=frame, 
                text='Pardict',
                width=10, 
                anchor='w').pack(side=tk.LEFT)

        txt_model_p_dict = tk.Text(master=frame,
                                   width=35,
                                   height=10)

        input_entries.append(txt_model_p_dict)
        txt_model_p_dict.pack(side=tk.LEFT)
        
        frame.grid(row=6, column=0)



    
        frm_l.pack(side=tk.LEFT)


    def _draw_right_panel(self):
        frm_r = tk.Frame(master=self,
                         width=10,
                         height=10)

        # Istantiate the containers
        fig = Figure(figsize=(10,10), dpi=100)
        canvas = FigureCanvasTkAgg(fig, master=frm_r)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH)
        
        frm_r.pack(side=tk.LEFT, padx=(10,0))



if __name__ == '__main__':
    root = tk.Tk()
    main_window = MainWindow(root).pack(side='top', fill='both', expand=True)
    root.mainloop()

