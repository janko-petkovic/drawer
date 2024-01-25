import matplotlib.pyplot as plt
# plt.style.use('rdn.plotstyles.rdnstyle')
import numpy as np

data = np.genfromtxt('output/data.csv', delimiter=',').T
ispulse = (data[1] > 0)

ptot = data[0]
ppulse = data[0][np.where(ispulse)]
pchase = data[0][np.where(ispulse==False)]

pdf_pulse, bins = np.histogram(ppulse, bins=50)
pdf_chase, bins = np.histogram(pchase, bins=50)
pdf_ratio = pdf_pulse/(pdf_chase + pdf_pulse)


# Plotting
fig, axs = plt.subplots(2,1,height_ratios=(2,1), sharex=True)

ax = axs[0]
ax.plot(bins[:-1], pdf_pulse, label='pulse')
ax.plot(bins[:-1], pdf_chase, label='chase')

ax.legend()
ax.set_ylabel('Protein count')

ax = axs[1]
ax.plot(bins[:-1], pdf_ratio)
ax.set_yscale('log')

ax.set_xlabel(r'Dendrite position [$\mu m$]')
ax.set_ylabel(r'$n_{pulse} \, / \, n_{tot}$')

plt.subplots_adjust(left=0.15, bottom=0.12, right=0.98, top=0.9)
plt.show()



