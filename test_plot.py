# test plot

import matplotlib.pyplot as plt


fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
ax1.plot(range(1,5), range(11,15))
plt.show()