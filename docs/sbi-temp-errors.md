FAILED tests/inference_on_device_test.py::test_nograd_after_inference_train[SNPE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/inference_on_device_test.py::test_nograd_after_inference_train[SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/inference_on_device_test.py::test_nograd_after_inference_train[SNRE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/inference_on_device_test.py::test_nograd_after_inference_train[SNRE_B] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/inference_on_device_test.py::test_nograd_after_inference_train[SNRE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/inference_on_device_test.py::test_nograd_after_inference_train[SNLE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray

FAILED tests/inference_with_NaN_simulator_test.py::test_restricted_prior_log_prob[uniform] - TypeError: Concatenation operation is not implemented for NumPy arrays, use np.concatenate() instead. Please do not rely on this error; it may not be given on all Python implementations.
FAILED tests/inference_with_NaN_simulator_test.py::test_restricted_prior_log_prob[gaussian] - TypeError: Concatenation operation is not implemented for NumPy arrays, use np.concatenate() instead. Please do not rely on this error; it may not be given on all Python implementations.

FAILED tests/linearGaussian_mdn_test.py::test_mdn_inference_with_different_methods[SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/linearGaussian_mdn_test.py::test_mdn_with_1D_uniform_prior - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray

FAILED tests/linearGaussian_snle_test.py::test_api_snle_multiple_trials_and_rounds_map[uniform-1] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/linearGaussian_snle_test.py::test_api_snle_multiple_trials_and_rounds_map[gaussian-1] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

FAILED tests/linearGaussian_snle_test.py::test_c2st_snl_on_linear_gaussian_different_dims - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

FAILED tests/linearGaussian_snpe_test.py::test_c2st_snpe_on_linearGaussian[2-gaussian-SNPE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/linearGaussian_snpe_test.py::test_c2st_snpe_on_linearGaussian[2-gaussian-SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/linearGaussian_snpe_test.py::test_c2st_snpe_on_linearGaussian[2-uniform-SNPE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/linearGaussian_snpe_test.py::test_c2st_snpe_on_linearGaussian[2-uniform-SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/linearGaussian_snpe_test.py::test_c2st_snpe_on_linearGaussian[1-gaussian-SNPE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/linearGaussian_snpe_test.py::test_c2st_snpe_on_linearGaussian[1-gaussian-SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray

FAILED tests/linearGaussian_snpe_test.py::test_c2st_snpe_on_linearGaussian_different_dims - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

FAILED tests/linearGaussian_snpe_test.py::test_api_force_first_round_loss[True-True] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/linearGaussian_snpe_test.py::test_api_force_first_round_loss[True-False] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/linearGaussian_snpe_test.py::test_api_force_first_round_loss[False-True] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray

FAILED tests/linearGaussian_snpe_test.py::test_mdn_conditional_density - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray

FAILED tests/linearGaussian_snpe_test.py::test_example_posterior[SNPE_A] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/linearGaussian_snpe_test.py::test_example_posterior[SNPE_C] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

FAILED tests/linearGaussian_snre_test.py::test_api_snre_multiple_trials_and_rounds_map[SNRE_B-1] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/linearGaussian_snre_test.py::test_api_snre_multiple_trials_and_rounds_map[SNRE_C-1] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

FAILED tests/linearGaussian_snre_test.py::test_c2st_sre_on_linearGaussian[SNRE_B] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/linearGaussian_snre_test.py::test_c2st_sre_on_linearGaussian[SNRE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray

FAILED tests/mcmc_test.py::test_getting_inference_diagnostics[nuts_pyro] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/mcmc_test.py::test_getting_inference_diagnostics[hmc_pyro] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/mcmc_test.py::test_getting_inference_diagnostics[nuts_pymc] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/mcmc_test.py::test_getting_inference_diagnostics[hmc_pymc] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/mcmc_test.py::test_getting_inference_diagnostics[slice_pymc] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/mcmc_test.py::test_getting_inference_diagnostics[slice_np] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/mcmc_test.py::test_getting_inference_diagnostics[slice_np_vectorized] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

FAILED tests/plot_test.py::test_plot_summary[SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/plot_test.py::test_plot_summary[SNLE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/plot_test.py::test_plot_summary[SNRE_B] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray

FAILED tests/posterior_nn_test.py::test_log_prob_with_different_x[0-SNPE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_log_prob_with_different_x[0-SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_log_prob_with_different_x[1-SNPE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_log_prob_with_different_x[1-SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_log_prob_with_different_x[2-SNPE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_log_prob_with_different_x[2-SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray

FAILED tests/posterior_nn_test.py::test_importance_posterior_sample_log_prob[SNPE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_importance_posterior_sample_log_prob[SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_importance_posterior_sample_log_prob[SNLE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_importance_posterior_sample_log_prob[SNRE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_importance_posterior_sample_log_prob[SNRE_B] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_importance_posterior_sample_log_prob[SNRE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray

FAILED tests/posterior_nn_test.py::test_batched_sample_log_prob_with_different_x[0-SNPE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_sample_log_prob_with_different_x[0-SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_sample_log_prob_with_different_x[1-SNPE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_sample_log_prob_with_different_x[1-SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_sample_log_prob_with_different_x[2-SNPE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_sample_log_prob_with_different_x[2-SNPE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray

FAILED tests/posterior_nn_test.py::test_batched_mcmc_sample_log_prob_with_different_x[0-SNLE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_mcmc_sample_log_prob_with_different_x[0-SNRE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_mcmc_sample_log_prob_with_different_x[0-SNRE_B] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_mcmc_sample_log_prob_with_different_x[0-SNRE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_mcmc_sample_log_prob_with_different_x[1-SNLE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_mcmc_sample_log_prob_with_different_x[1-SNRE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_mcmc_sample_log_prob_with_different_x[1-SNRE_B] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_mcmc_sample_log_prob_with_different_x[1-SNRE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_mcmc_sample_log_prob_with_different_x[2-SNLE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_mcmc_sample_log_prob_with_different_x[2-SNRE_A] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_mcmc_sample_log_prob_with_different_x[2-SNRE_B] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/posterior_nn_test.py::test_batched_mcmc_sample_log_prob_with_different_x[2-SNRE_C] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray

FAILED tests/posterior_sampler_test.py::test_api_posterior_sampler_set[1-slice_np] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/posterior_sampler_test.py::test_api_posterior_sampler_set[1-slice_np_vectorized] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/posterior_sampler_test.py::test_api_posterior_sampler_set[1-nuts_pyro] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/posterior_sampler_test.py::test_api_posterior_sampler_set[1-hmc_pyro] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/posterior_sampler_test.py::test_api_posterior_sampler_set[1-nuts_pymc] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/posterior_sampler_test.py::test_api_posterior_sampler_set[1-hmc_pymc] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
FAILED tests/posterior_sampler_test.py::test_api_posterior_sampler_set[1-slice_pymc] - UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

FAILED tests/sbc_test.py::test_running_sbc[SNPE_C-None-boxuniform-marginals] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/sbc_test.py::test_running_sbc[SNPE_C-None-boxuniform-posterior_log_prob] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/sbc_test.py::test_running_sbc[SNPE_C-None-independent-marginals] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/sbc_test.py::test_running_sbc[SNPE_C-None-independent-posterior_log_prob] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/sbc_test.py::test_running_sbc[SNLE_A-mcmc-boxuniform-marginals] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/sbc_test.py::test_running_sbc[SNLE_A-mcmc-boxuniform-posterior_log_prob] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/sbc_test.py::test_running_sbc[SNLE_A-mcmc-independent-marginals] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/sbc_test.py::test_running_sbc[SNLE_A-mcmc-independent-posterior_log_prob] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/sbc_test.py::test_running_sbc[SNLE_A-vi-boxuniform-marginals] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/sbc_test.py::test_running_sbc[SNLE_A-vi-boxuniform-posterior_log_prob] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/sbc_test.py::test_running_sbc[SNLE_A-vi-independent-marginals] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
FAILED tests/sbc_test.py::test_running_sbc[SNLE_A-vi-independent-posterior_log_prob] - TypeError: randn_like(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
