# Possible projects to investigate

The eligible projects could tackle any of the following themes:

1. Network modeling
2. Biophysics
3. Neuromodulation
4. Robustness
5. ML / SBI modeling
6. Meta-learning with Tim (and all the others ofc)

## Degeneracy

1. Redundancy in reaction networks: the machinery underlying synaptic
   plasticity (everything really) is composed of hundreds of different
   molecules. The emerging target dynamics, however, exhibit a surprisingly
   simple and intuitive behaviour (hebbian learning, monotonic frequency
   dependence). Is, therefore, the total reaction network the result of an
   amazingly intricate optimization process or is its complexity aimed at
   providing a sufficient degree of robustness to perturbations?

2. Genetic algorythms and redundancy (more theoretical): can we investigate how
   parameter degeneracy survives genetic optimization?

3. Any small model: what are the parameter degeneracies in a 2 layer perceptron?
   How is this invariance impacted by different non linearities?
   How do they translate in better accuracy or faster training times? Are they
   correlated to a network robustness in respect to input perturbations?

## Meta-Learning

1. Additional refinement: the filtering rules proposed in Confavreaux et al.
   2024 are predominantly structural: well defined rates (stability), realistic
   weight change, "smoothness" of dynamics (Fano factor and CV),
   non-asynchronicity (**non-epilepsy**).
   No rules, however, impose any encoding property on the network. "Goodness of
   encoding" metrics can be applied on the resulting ~6000 rules to assess how
   well the resulting connectivity is able to perform given some task. Also, it
   would be interesting to understand which metrics are equivalent.
   An additional rule can be taken from Kuzmina et al. 2024.

## SSM: summary statistics and dimensionality reduction

1. SSM: it looks great and I think one really needs to study it (George Haller
   lab ETH, in particular Marraffa A. and Prof. Mante V.  for neuroscientific
   applications on RNNs).

2. SSM can provide simplified target trajectories for SBI

3. SSM can be used to analyze the learning trajectories of DL models during
   training.
