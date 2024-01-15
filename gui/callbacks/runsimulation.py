import ast
import tkinter as tk
import torch

from rdn.fitting.models import LocalGaussModelTilde
from rdn.validation import Simulation


def run_simulation(input_entries: list):

    # Parse the input_entries[].get()
    simulation_time = int(input_entries[0].get())
    inter_spine_distance = int(input_entries[1].get())
    spine_number = int(input_entries[2].get())

    stim_idxes = torch.arange(int(input_entries[3].get()),
                              int(input_entries[3].get())+int(input_entries[4].get()),
                              int(input_entries[5].get()))

    print(input_entries[6].get('1.0',tk.END))
    model_p_dict_str = input_entries[6].get('1.0',tk.END).replace('\n', ' ')
    model_p_dict_str = '{' + model_p_dict_str + '}'
    model_p_dict = ast.literal_eval(model_p_dict_str)

    simulation = Simulation(model = LocalGaussModelTilde(),
                            model_p_dict = model_p_dict,
                            simulation_time = simulation_time,
                            spine_number = spine_number,
                            inter_spine_distance = inter_spine_distance,
                            stim_indexes = stim_idxes)

    simulation.visualize_run(100,2)


