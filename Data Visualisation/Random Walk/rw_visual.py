import matplotlib.pyplot as plt

from random_walk import RandomWalk
count = int(input("How many figures do you want to create?\n"))

while count != 0:

    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('grayscale')
    fig, ax = plt.subplots(figsize=(19.20, 10.80), dpi=300)
    ax.set_title(f"Random Walk №{count}", fontsize=16)
    ax.scatter(rw.x_values, rw.y_values, c=range(rw.num_points),
               cmap=plt.cm.Blues, edgecolors='none', s=1)
    # ax.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)
    ax.set_aspect('equal')

    # Emphasize the first and last points
    ax.scatter(0, 0, c='red', edgecolors='none', s=5, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors='none',
               s=5, zorder=3)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.savefig(f'rw_{count}.png', bbox_inches='tight')
    count -= 1
