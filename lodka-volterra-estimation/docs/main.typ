#set text(
  size: 11pt,
  font: "Atkinson Hyperlegible",
)

#set par(
  justify: true,
  leading: 0.7em,
)

#set heading(
  numbering: "1.1 ",
)

#show heading: set block(
  below: 1em, above: 3em,
)

#set bibliography(
  // style: "nature",
)

#set math.equation(
  numbering: "(1)"
)


// Define some commands
#let sh = $space.hair$

// Begin the document
#align(center, text(size: 17pt)[
   *Foxes and rabbits in Germany*
])

#v(1cm)

#outline()

= The problem
Consider the dataset reported in the SBI discord, showing the evolution of the
fox and rabbit population in a German wald throughout the last 20 years. We are
interested in optimizing a competitive Lodka-Volterra system to this dataset and
see how well such a simplified model can reproduce a real-life ecological
scenario.

= Introduction
Rabbits do not eat foxes, while foxes eat rabbits and other animals @foxes-diet.
Notes from the Colorado University @colorado-model, model the problem using the
bounded (logistic) rabbit growth LV equations

$ 
  cases(
    dot(x) = r_x sh x (N_x - x) - alpha x y \
    dot(y) = -y/tau_y + beta x y
  )
$

where we see that without an interaction between the two species, rabbits would
tend to grow up to $N_x$ and foxes would die out.

Let's start from an even simpler case (the "traditiona" Lodka-Volterra system),
where the growth of the rabbit is not limited to a carrying capacity but can
carry on indefinitely

$ 
  cases(
    dot(x) = x/tau_x - alpha x y \
    dot(y) = -y/tau_y + beta x y
  )
$

If we adimensionalise this system by reparametrizing with $s = t\/tau_x$ (we put
ourselves in the temporal scale of the rabbits), we obtain the 3-parametric system

$ 
  cases(
    x' = x - a sh x sh  y \
    y'= -R sh y + c sh x sh y
  )
$

where $a = tau_x sh alpha$, $R = tau_x\/tau_y$, and $b = tau_x sh beta$

#bibliography("biblio.bib")
