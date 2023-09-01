import matplotlib.pyplot as plt

LABEL_SIZE = 18
TITLE_SIZE = 32

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# ax.plot(x_values, y_values, linewidth=3)


# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=TITLE_SIZE)
ax.set_xlabel("Value", fontsize=LABEL_SIZE)
ax.set_ylabel("Square of Value", fontsize=LABEL_SIZE)

# Set size of tick labels.
ax.tick_params(labelsize=LABEL_SIZE)

ax.axis([0, 1100, 0, 1_000_000])
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
