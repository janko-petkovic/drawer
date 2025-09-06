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

4. **What is the relationship between degeneracy and model structural
   identifiability?** (maybe this is more a question to Pedro)

Questions about Deistler et al. 2022 PNAS:

1. If we reduced the model to render it fully identifiable, could we have found
   simple functional relationships between the degrees of freedom and energy
   efficiency?

## Meta-Learning

**Additional refinement**

Additional refinement: the filtering rules proposed in Confavreaux et al.
2024 are predominantly structural: well defined rates (stability), realistic
weight change, "smoothness" of dynamics (Fano factor and CV),
non-asynchronicity (**non-epilepsy**).
No rules, however, impose any encoding property on the network. "Goodness of
encoding" metrics can be applied on the resulting ~6000 rules to assess how
well the resulting connectivity is able to perform given some task. Also, it
would be interesting to understand which metrics are equivalent.
An additional rule can be taken from Kuzmina et al. 2024.

**Connection with dim-red techniques**

We know that during learning these networks have to exhibit some transition to low-dimensional dynamics. We have a number of methods now suggesting this theory and allowing to extract these dynamics from neuronal recordings [TCA, SSM, sTCA, MartinoRNN]. **Q:** can we find the parameters in a HH network, or the parameters of a plasticity model that makes these properties emerge during learning?





## SSM (spectral submanifolds)

Summary statistics and dimensionality reduction

1. SSM: it looks great and I think one really needs to study it (George Haller
   lab ETH, in particular Marraffa A. and Prof. Mante V.  for neuroscientific
   applications on RNNs). CAVEAT: they need dynamics with fixed points or some
   attractors at least.

2. SSM can provide simplified target trajectories for SBI

3. SSM can be used to analyze the learning trajectories of DL models during
   training.

# Medical

1. From pyloric circuit of C. borealis to heart energy optimization? Does it
   make sense? We have kind of understood everything about the heart by now so
   maybe the only perspective is finding some alterations in the reduced
   dynamics to use instead of ECG - latent Brugata syndrome? In Melo et al. 2023
   PNAS Nexus, they obtain a 0.93 AUC. Also, they do not seem to use a RNN. Can
   we try the **reparametrization** trick

# PhD on epilepsy

1. 25% of epilepsy patients are drug resistant. We know that AEDs act generally
   on some channels, reducing the overall neuronal excitability. This would mean
   that some network structures cannot exit some bifurcated state (epileptic
   state) with a smooth variation of a global parameter. Can we reproduce this?
   Does this network exit this state only via a change in its topology (surgical
   intervention)? **Also, can we use SBI to investigate the channel space in response to therapy?**

# Possible proposals

## Theme 1: spontaneous emergence of information hierarchies from randomness (denoising is all you need lol)

**The wish**: noisy input, processed from a random network with a random update rule MINIMIZING SOMETHING (?), naturally uncouples the input statistics. Spiking systems, like von Neumann systems, are just instantiations of this principle. 

**Because of what**: (1) metalearning with Tim (we found network stability, *but do all of these rules allow for pattern uncoupling? to be discussed*), (2) CNNs with Rita and Janko (gradient descent + filter structure induce invariance to noise intrinsic in the data, without explicit objectives - *other grad-descent strategies work?*)

**What for**: it works always, zero energy, the 7000 superspecific plasticity rules are finally declared a hoax, link between gradient descent and STDP (or any other). Link between architecture, objective and update (von Neumann / brain are just instances).

**Intuitions (knowing 0.1% of the field):** is this related in any way with stochastic resonance? Or the ensemble version of it? Does *asynchronicity of processing* distinguish von Neumann and spiking infrastructures?

**Criticism:** has Kolmogorov already given this project as excercise to the reader?

**Key concepts:**

- hierarchy of informational complexity (whatever it means)

- sparsity, engrams, low energy consumption (are we always minimizing energy consumption? Is there another scalar? [22]) 

- universal approximation properties (if true, you have to prove a mapping between the one layer perceptron and some neuronal system - probably done)

- spiking, with infrastructure of reward+update, is just one possible implementation of a more general denoising concept (Hamilton-Jacobi-Bellmann framework is a possibility)

- event-based: seems to be a keyword in neuromorphic, I don't know much about it

**Methods**

- framework: **information theory, information geometry**

- **SBI**
  
  - pretty good for investigating information invariance and degeneracy, from models to datasets -> Rita has a formal paper on the foliation geometry of MNIST
  
  - investigate neuromorphic chip invariances? Robustness? Do we have a model? 

- **Jaxley**: simulate whatever neuronal superquick -> can we simulate also chips? does it even make sense?

**Chapters**

1. Metalearning: start by training a bunch of LIF neurons with different plasticity rules and see if they can all encode (I guess Tim is already doing this). Honestly im not a fan of LIF, idk whats the validity regime.

2. Metalearning 2: as above but with HH neurons. Does SBI see something about the parameters of a network being able to encode information? what about a network that reaches *good properties?* (sparsity, smt else idk)

3. Robustness in neuromorphic chips with SBI (some analysis like the one they did to use choose 0-1 Voltage decoding instead of multi-voltage decoding)

### Roles for everyone

**Experimental collabs**: we have super cool experimental collaborators, with cutting edge cultures of SN (and globus pallidus from memory but I studied this much time ago). Parkinson's (which is, I would guess their main interest) affects the pars compacta of the SN, which happens to be one of the main dopaminergic centers (together with the VTA) driving **reward**. So this is the **perfect area to have to check how reward shapes neuronal circuits** (a whole bunch of literature there - **reinforcement learning, predictive coding**).

**Rodolphe Sepulchre**: Just make chips? He does controly theory mainly - not my strong suit atm

**Us**: we are the theoreticians in theory. I guess the framework is information theory, and experiments/chips/brain are just instantiations? Do I go to cry to Dayan?

We now have a way to simulate with juxley, so we can test and implement hypotheses on how a biologically plausible system is able to carry out a specific task (in a robust fashion). From our simulations we can bring ideas, predictions, inspiration (also in a very naive way). 

### Kudithipud, ..., Subramoney & Furber [(link)](https://doi.org/10.1038/s41586-024-08253-8)

Neuromorph pros: (1) no transfer between memory and CPU, (2) sparse information encoding - lol, (3) dynamic local learning with less energy expenditure, (4) predictions about input - ? (4) multiscale dynamics for real time learning.  Buzzwordy paper.

**Scale:** capacity of a system to operate at a given size, speed, energy

**Metric:** density of underlying hardware (Moore's law) + FLOPS

**Desirable features**:

1. **Hierarchical and distributed** (and this is where we jump in with our great science). **Levels of information complexity** (what does it mean?). This should reduce redundancy (?)

2. **Sparsity**: apparently present in the human brain (idk man, but Poirazi I think i examining this in NNs or whatever). SPARSE -> DENSE -> SPARSE (**connection to transformers and pseudoorthogonality**). Engrams (as single cells) are good for energy consumption [22]. Could be an issue [27]

3. **Neuronal scalability**: from a practical standpoint, we have to put many neurons on a chip.

4. **Asynchronous communication**: there's a bunch of protocols supporting async comm between units [3,32,36-41]

5. **Dynamic reconfigurability**: equivalent of plasticity. If this noise theory is true, this could come from free  

## Theme 2 (proposed by Pedro): I don't remember

## Theme 3 model misspecification

For the fellowship: it is useful for a neuroscience follow-up project. 

Circuit level

1. we need scalable and accurate SBI methods -> we deal with model misspecification (look for SBI misspecification)

2. asdf

3. fitting models to data

## Theme 4: Jaxley scales super well, you can implement neurons for whatever thing you want, also for neuromorphic
