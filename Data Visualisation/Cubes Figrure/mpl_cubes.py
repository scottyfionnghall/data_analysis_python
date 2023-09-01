# Cubes: A number raised to the third power is a cube. Plot the first five
# cubic numbers, and then plot the first 5,000 cubic numbers.

import matplotlib.pyplot as plt

LABEL_SIZE = 16
TITLE_SIZE = 32

x_values = range(1, 1001)
y_values = [x**3 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

ax.set_title("Cube Numbers", fontsize=TITLE_SIZE)
ax.set_xlabel("Value", fontsize=LABEL_SIZE)
ax.set_ylabel("Cube of Value", fontsize=LABEL_SIZE)

ax.tick_params(labelsize=LABEL_SIZE)
ax.axis([0, 1000,  0, y_values[-1]])
plt.savefig('cube_plot.png', bbox_inches='tight')
