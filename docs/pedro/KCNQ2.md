# Possible outline

**Research question**: specific alterations (R201C/R201H) of the gene KCNQ2,
lead to a gain of function (GoF) of the Kv7.2 potassium channel, phisiologically
responsible for raising the threshold of neuronal spiking.

Intuitively, loss of function leads to increased neuronal firing, with the
consequent emergence of early age epileptic phenotypes (newborns have seizures). 

The gain of function (**I don't really understand what this gain is**) is
supposed to have an opposite effect, and this can be seen experimentally with
neuronal populations showing a decrease in spiking activity (**what were these
experiments? We need _in vivo_ observations since we are applying to
medicine**). Still, babies get seizures. So why is that? We are supposed to
find answers to this questions by basically understanding how a network of **3
cellular types - excit, inhib and astro** can undergo synchronization despite a
lower firing tendency, and we should pin point the exact molecular mechanism
leading to this behaviour.

**Open issues**: how do we link the final parameter modifications to the
alterations in the protein sequence? We don't know how to do that

## Section 1: single cell approach

**Focus**
1. single neuron electrophysiology, optimally one for each of the cellular
families in consideration (excitatory, inhibitory, astrocyte)
2. ideally we would want the experimental data to come from synthetic, controlled
stimulations in order to study _precisely_ the response function of each
cell belonging to the three different cellular species

**Parametrization to infer**
Kinetic parameters of Kv7.2

**Procedure**
1. For each neuronal type, implement Implement **single** neuron, as accurately
as possible
2. Simulate joint across Kv7.2 kinetic parameters (**does KCNQ2 mutate together
with other factors? this is a huge confounding factor that can compromise the
joint distribution**)
3. From single cell electrophysiology data, infer the Kv7.2 alterations.

**Notes**: morphology could have an effect on the overall cellular behaviour. If
we correctly simulate what is being conducted experimentally, and our model is
good, we should get good posteriors. The correct posteriors, however, could have
a different effect once different morphologies are considered (this is to be
expected!)


**Progress**
1. Good posteriors: if we are getting good posteriors for the channel kinetics,
we don't need do do much more in this step (potentially a **deliverable paper**)
2. Bad posteriors: bad posteriors (highly multimodal, highly unspecific) could
emerge from two different causes
    1. Bad single neuron model > _correct the HH model, correct the morphology,
    be careful what point in the dendrite is being stimulated_
    2. Correlation between alteration of KCNQ2 and other alterations, leading to
    the proper misspecification (we would be investigating the wrong region of
    a higher joint distribution) > _understand and implement accordingly the
    correlation between R201C/R201H gain of function and other genetic
    mutations_

Solving issues _i_ and _ii_ puts us back at point 1., with a potential
deliverable paper.


## Section 2: network approach

**Focus**
- Single neuron
- Network data (neuropixel?) -> population activity and metrics

**Parametrization to infer**:
- Cellular population statistics
- Morphology
- Probably other things that I didn't think of
- If we didn't get them in the previous section, Kv7.2 kinetic parameters

**Procedure**
1. Design a simulation with the correct connectional (?) and morphological
   properties
2. Simulate with (i) the wild type (ii) the mutated Kv7.2.

**Progress**
1. If we get seizures in MUT and good activity in WT without having inferred
   anything (just plugged in all the parameters from the previous section and
   the experimental observations) we have a strong, scientifically sound result.
2. If things don't work, we have to infer (this stops being a prediction but
   becomes a hypothesis, that then would need an additional experiment to be
   tested on):
   1. network properties (connections, morphologies, population ratios)
   2. Kv7.2 parameters (I don't like this, as what we see for single cell should
      be true also when a neuron is put in a network - **plasticity could play a
      role in the network activity**)

In case we had point 2, we should propose an additional experimental prediction
to hit, in order to have the pipeline _observation > hypothesis > corroboration_
straight. 


# Mathematical and computational methods
The methods I can think of that could be useful for this project 
1. **SBI and Jaxley** of course
2. **Dynamical systems' theory + renormalization**: spiking networks are known to
   have weird properties (e.g., paradoxical inhibition when input current is
   increased) that depend on the statistical properties of the network. If we
   know how to get from single neurons to the "mean field theory" describing the
   population dynamics as a lower dimensional dynamical system I think we should
   have higher chances of understanding what is happening (also it's more
   elegant)
3. **Dim red techniques**: the mean field theory could still be high dimensional.
   Obtaining a reduced order model, while keeping track of
   the underlying biophysical meaning of its parameters, surely would help.

**Main issues**: I don't think it's easy to obtain a mean field description that
keeps explicitly track of the parameters of Kv7.2 - but maybe it doable? I am
convinced that this would be the cleanest way to do it.

**Possible workaround**: inference from network activity bypasses this issue, and
can be implemented since we have the computational power. With this approach,
however, we would be exposed to misspecification and high dimensionality.



