#set page(
  paper: "a4",
  margin: (x: 2cm, y: 2.5cm),
  numbering: "1",
)

#set text(
  size: 11pt,
  font: "Archivo",
  weight: "light"
)

#set par(
  justify: true,
  leading: 0.7em,
  spacing: 1.7em,
)

#set heading(
  numbering: "1.1.",
)

#show heading: it => {
  set block(below: 0.7em, above: 2em)
  set text(weight: "semibold", font: "Roboto")
  it
}

#set math.equation(
  numbering: "(1.1)"
)


#show figure.caption: cap => {
  set text(size: 10pt)
  set align(left)
  cap
}


#let rhobar = $overline(rho)$



#align(center, text(17pt, weight: "bold", font: "Roboto")[
  A reasonably robust way of synchronizing two oscillators while mostly preserving
  their phase difference
])


#outline()


= Introduction
The ellipsoid body of the D. melanogaster shows a bump of activity
corresponding to the allocentric orientation of the fly. A possible model of
the neuronal implementation giving raise to this navigation instrument, has
been presented in @workshop. 

Here, the position (angle) of the activity bump on the ellipsoid body was
proposed to correspond to the coincidence detection of two inputs coming 
from two different neurons, spiking with some phase difference. The axons
of these two neurons would wind around the ellipsoid ring in opposing
directions, so that the spikes traveling through them would meet at a 
location spefic to the phase difference between the two neurons' activity
(@fig:intro).


#figure(image("figures/figure-1-concept.png"), caption: [
  Cartoon representation of the coincidence detection mechanism giving raise 
  to the bump attractor dynamics in the ellipsoid body.
])<fig:intro>

This mechanism is put forward to decode on a linear domain $D = [0, L]$ the
information decoded in the phase shift $phi in [-pi,pi]$ between the activity 
of the two neurons. In order for the mapping $f : phi mapsto x in D$ to be a
function, it is necessary that $f$ does not depend on time. A necessary condition
for this to happen is that the two neurons spike with the same frequency, as 
any difference in the two rates would lead to precession on the domain $D$ 
(cfr. @fig:intro c and d). 

In other words, it is necessary to find a mechanism (or more realistically a
reasonable equation) coupling the activity of the two neurons that also
+ does not substantially alter their phase difference, and
+ shows some degree of robustness with respect to neuronal parameter and input
  perturbations.

= Problem setup
Consider two neurons spiking at a certain _constant_ frequency $omega_i$, $i=1,2$.
Let $theta_i$ be the phase of the respective (evenly spaced) generated action
potentials, and let $phi_(i j) = theta_i - theta_j$. Let now two mechanisms 
unfold simultaneously in this setup:

+ _Input driven phase shift:_ some controller needs to be able to shift the spike
  phase in each of the two neurons, effectively encoding two different, continuous, cyclic
  pieces of information in their activity;
+ _Frequency synchronization_: another mechanism needs to couple the two neurons
  ensuring spiking at a same, possibly constant, frequency. This target frequency could
  either depend on an external clock or pace generator, or could be determined autonomusly
  only from some summary statistic describing the two neuron system. The second case 
  appears to be more interesting and flexible.

These two mechanisms need to have robust structure, meaning that they should not
undergo some kind of bifurcation when a small perturbation in the system's parameters
is performed. To this end, one can model the oscillating activity of each neuron as a 
dynamical system endowed with an attractive limit cycle. Many such neuronal models 
exist in the literature (e.g. Fitzhugh-Nagumo, or Morris-Lecar models), but since
we are intersted only in the structurally robust existance of a limit cycle we could
recur to the very trivial model (in polar coordinates)

$
cases(
  dot(rho_i) = -(rho_i - overline(rho)_i)\, quad rhobar_i > 0 \
  dot(theta)_i = omega_i
)
$

This model shows both (i) permanence of the limit cycle with respect to perturbations of 
$rhobar_i$ and, enticingly, (ii) uncoupling between the radial and angular dynamics. 
*The second property is NOT usually found in more complex systems (like FN oscillators), 
and the treatment presented in the next sections does not apply to them.*


= Introducing the mechanisms
== Shifting the phase
In this setup, a neuronal phase shift happening throughout the interval $[t_1, t_2]$ can be obtained via the addition of a temporary "current" $I: t mapsto RR$ in the equation for the angular velocity

$
  dot(theta)_i = omega_i + I, quad I = plus.minus [Theta(t-t_1) - Theta(t-t_2)]
$

By directly integrating and considering $t > t_2$, we get $theta(t) = theta_0 + omega t plus.minus (t_2 - t_1)$, i.e. the forcing has induced a positive (or negative) shift of linear magnitude $t_2 - t_1$.
Clearly, this shift could be greater than $2 pi$, and the consequences of the final module 
operation $t_2 - t_1 mapsto delta in [0,2 pi]$ on the neuronal information encoding need to be
understood carefully.

== Synchronizing the neurons

=== Quick firefly recap
We start briefly analyzing a model from Ermentraut and Rinzel (1984) and reported in @strogatz:1994,
describing the synchronization of the firefly glowing.
Let $theta(t)$ represent the phase of one firefly's flashing rhythm, *where $theta=0$ corresponds to 
the instant when a flash is emitted*. Assume also $omega$ be the firefly's own flashing frequency,
so that $dot(theta) = omega$. Now suppose we introduce a periodic forcing $dot(Theta) = Omega$,
#footnote[possibly representing the average swarm frequency? [AN]] *where $Theta=0$ corresponds to 
the forcing's flash.* We model the effect of this forcing on the firefly's activity as

$
  dot(theta) = omega + A sin (Theta - theta)\, quad A>0 
$<eq:firefly>

Calling the $phi = Theta - theta$ the phase difference between the firefly flash and the forcing
flash, one finds the final equation for the phase shift to be 

$
  dot(phi) = Omega - omega - A sin phi
$

This equation allows to recover two main testable phenomena (via a fold bifurcation):
+ *phase locking*: if $Omega$ and $omega$ are close enough, the firefly will lock 
  with the forcing, flashing with the same frequency at a constant phase difference 
  $phi(t) = phi(Omega, omega,A)$;
+ *phase drift*: in the opposite case (when $omega$ has values outside the _range of entrainment_),
  the phase $phi(t)$ increases indefinitely, drifting away.

This model model is not suitable for our application as, when synchronization occurs, it is
accompanied by phase locking, a behaviour deriving from the phase terms $theta$ and $Theta$ 
being present in the equation for the angular velocity change (@eq:firefly). We would want 
our model to allow for "frequency locking" without this condition being dependent on the value
of the phase difference $phi$. One possible way to achieve this effect is introducing an equation
for $dot(omega)$ not depending on the phase variables $theta_i$.

=== A simpler model


#bibliography("biblio.bib")
