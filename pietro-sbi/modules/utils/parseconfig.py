import tomllib
import torch
from sbi.utils import BoxUniform

def parse_config(path_to_config : str) -> tuple:
  '''Small parser for the config.toml.

  Parameters
  ----------
  path_to_config : str
    Path to the config.toml. Can be absolute or relative to the main.


  Returns
  -------
  tuple : simulator_setup, prior, true_parameter
  '''

  with open(path_to_config, 'rb') as f:
    config = tomllib.load(f)

  # Simulator setup
  simulator_setup = config['simulator_setup']

  # Inference setup
  inference_setup = config['inference_setup']

  # Build the priors
  params_prior = config['params_prior']
  keys = params_prior.keys()
  # breakpoint()
  lb = [x[0] for x in params_prior.values()]
  ub = [x[1] for x in params_prior.values()]
  prior = BoxUniform(low=torch.tensor(lb),
                     high=torch.tensor(ub),
                     device=inference_setup['device'])


  return simulator_setup, inference_setup, params_prior, prior

