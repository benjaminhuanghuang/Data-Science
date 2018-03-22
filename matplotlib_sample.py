# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x) + 1
z = np.cos(x**2) + 1

plt.figure(figsize=(8, 4))   # set plot size
plt.plot(x, y, label='$\sin x  +1$', color='red', linewidth=2)
plt.plot(x, z, 'b--', label='$\cos x ^2 +1$', )   # color is blue , line style is --

plt.xlabel('Time(s) ')
plt.ylabel('Volt')
plt.title('A simple example')
plt.ylim(0, 2.2)    # range of y
plt.legend()        # display legend
plt.show()