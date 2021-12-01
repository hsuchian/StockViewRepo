# test plot

import matplotlib.pyplot as plt

# one figure is one window, one window can contain
# mutiple sub plot (axis)
fig1 = plt.figure()

ax1 = fig1.add_subplot(1,2,1)
ax1.plot(range(1,6), [11, 10, None, 12, 13 ])

ax2 = fig1.add_subplot(1,2,2)
ax2.plot(range(1,6), [11, 10, None, 12, 13 ])


plt.show()

