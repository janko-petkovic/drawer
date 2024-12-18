from typing import Union
from os.path import join
import numpy as np

def sample_joint(path_to_theta_x_folder: str, 
                 subsample_size: Union[int,None] = None,
                 ) -> tuple:
    '''Generates a tuple with "sample size" x and theta pairs, subsampled from a
    "ground truth" joint distribution'''

    # Load the whole joint
    x = np.load(join(path_to_theta_x_folder, 'x.npy'))
    theta = np.load(join(path_to_theta_x_folder, 'theta.npy'))

    # If the sample size is a number
    if subsample_size is not None:
        idxes = np.arange(len(x))
        sub_idxes = np.random.choice(idxes, size=subsample_size, replace=False)

        sub_x = x[sub_idxes]
        sub_theta = theta[sub_idxes]
    else:
        sub_x, sub_theta = x, theta

    return sub_theta, sub_x
