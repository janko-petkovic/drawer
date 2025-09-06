#set par(
  justify: true,
)

Given $x,y,z: RR arrow.long [0, infinity[$ non negative functions of time, study
the bifurcations or whatever of the 3d system
$
cases(
  &dot(x) = -x/tau_x - k_y x (A - y) - k_z x (B-z)+ y/tau_y + z/tau_z + I(t) \
  &dot(y) = - y/tau_y + k_y x (A - y) \
  &dot(z) = -z/tau_z + k_z x (B - z)
)
$

with the input current being
$ I(t) = sum_(overline(t) in "spike times") delta(t-overline(t)) $ 

What would, in particular, be interesting to obtain is that
- when the spiking frequency is low, $y(t) >> z(t)$
- when the spiking frequency is high, the opposite is true

Experimental observations would suggest that $tau_y < tau_z$ and $k_y >> k_z$ ($y$
consumes $x$ faster, but also decays more quickly).
Also, it seems that $A << B$ (like $1\/10$).

_Maybe_ it is useful to notice that 

$ dot(x) + dot(y) + dot(z) = -x/tau_x + I(t) $
