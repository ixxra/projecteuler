# coding: utf-8
get_ipython().magic(u'ls ')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'clear ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd problem058')
get_ipython().magic(u'ls ')
get_ipython().magic(u'clear ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'run problem58.py ')
model = np.zeros((len(ns), 2))
model
model = np.ones((len(ns), 2))
model
import matplotlib.pyplot as plt
model[:, 0] = ns
model
get_ipython().magic(u'pinfo np.linalg.solve')
np.linalg.lstsq(model, np.log(ratios))
get_ipython().magic(u'pinfo np.linalg.lstsq')
plt.semilogx(ns, ratios, 'r.')
plt.show()
plt.semilogy(ns, ratios, 'r.')
plt.show()
plt.loglog (ns, ratios, 'r.')
plt.show()
plt.semilogx(ns, ratios, 'r.')
plt.show()
plt.loglog (ns, ratios, 'r.')
plt.show()
model = np.ones((len(ns), 2))
model[:,0] = np.log(ns)
np.linalg.lstsq(model, np.log(ratios))
model
np.linalg.lstsq(model, np.log(ratios))
model[:10, :]
logy =  -0.25248504 * np.log(ns) -0.16987566
np.plot(ns, ratios, '.r', ns, np.exp(logy), 'g-')
plt.plot(ns, ratios, '.r', ns, np.exp(logy), 'g-')
plt.show()
get_ipython().magic(u'clear ')
plt.plot(ns, ratios, '.r', ns, np.exp(logy), 'g-')
plt.grid()
plt.title('Prime numbers ratio in the lattice')
plt.show()
plt.plot(ns, ratios, '.r', ns, np.exp(logy), 'g-')
plt.grid()
plt.title('Prime numbers ratio in the lattice')
plt.xlabel ('Lattice size')
plt.ylabel ('Prime numbers ratio')
plt.savefig ('prime-numbers-lattice.png')
get_ipython().system(u'display prime-numbers-lattice.png ')
plt.plot(ns, ratios, '.r', ns, np.exp(logy), 'g-')
plt.title('Prime numbers ratio in the lattice')
plt.xlabel ('Lattice size')
plt.ylabel ('Prime numbers ratio')
model
get_ipython().magic(u'clear ')
logy =  -0.25248504 * np.log(ns) -0.16987566
get_ipython().magic(u'pinfo plt.text')
get_ipython().magic(u'pinfo plt.legend')
get_ipython().magic(u'clear ')