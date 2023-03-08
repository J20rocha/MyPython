import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.ylim(ymin=5)

plt.gca().invert_yaxis()
plt.bar(x,y)
plt.show()