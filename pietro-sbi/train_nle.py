import torch
torch.manual_seed(123)

from modules.utils import parse_config, sample_joint


from sbi.utils import posterior_nn
from sbi.inference import SNLE, SNPE
from sbi.analysis import pairplot


def generate_nle_posterior(inference_setup: dict,
                           joint: tuple[torch.Tensor, torch.Tensor],
                           prior: torch.distributions.Independent,
                           true_x: torch.Tensor,
                           ):
    # Model instantiation
    inference = SNLE(prior)

    theta, x = joint
    x = x.reshape(x.shape[0], -1)

    # print(theta.shape, x.shape, true_x.shape)

    _ = inference.append_simulations(theta, x)
    de = inference.train(training_batch_size=inference_setup['train_batch_size'])
    
    # posterior = inference.build_posterior(mcmc_method='slice_np_vectorized',
    #                                       mcmc_parameters={'num_chains' : 4,
    #                                                        'thin' : 5})
    # posterior = posterior.set_default_x(true_x)

    posterior = inference.build_posterior(
            sample_with='vi',
            vi_method='rKL').set_default_x(true_x).train()
    
    # posterior = inference.build_posterior(de)

    samples = posterior.sample((inference_setup['posterior_sample_size'],),
                               x=true_x)


    import matplotlib.pyplot as plt
    _ = pairplot(samples, labels=['log mu', 'log sigma', 'log theta'])
    plt.show()
    



if __name__ == '__main__':
    # Recover the setup from the config file
    simulator_setup, inference_setup, _, prior = parse_config('config.toml')

    # For more readability
    device = inference_setup['device']

    # Subsample the joint, transform to torch arrays
    theta, x = sample_joint('data/',
                            subsample_size=inference_setup['subsample_size'])

    x = torch.tensor(x, dtype=torch.float32, device=device)
    theta = torch.tensor(theta, dtype=torch.float32, device=device)
    joint = (theta, x)
    

    # Stability target: we want the time-to-time differences in frequency to 
    # be as close to 0 as possible (stability). We will therefore use 0 as true x.
    true_x = torch.tensor((-0.5,), dtype=torch.float32,
                          device=device)


    # breakpoint()

    generate_nle_posterior(inference_setup, joint, prior, true_x)
