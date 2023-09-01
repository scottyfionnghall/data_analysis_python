from random import choice


class RandomWalk:
    """
    A class to generate random walks
    """

    def __init__(self, num_points=5000):
        """
        Initialize attributes of a walk.
        """
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self, max_distance):
        """
        Calculate distance to the next step.
        """
        direction = choice([1, -1])
        distance = choice(max_distance)
        step = direction * distance
        return step

    def fill_walk(self, max_distance=5):
        """
        Calculate all the point in the walk.
        """
        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:

            # Decide which direction to go, and how far to go.
            distance = range(0, max_distance)
            x_step = self.get_step(distance)
            y_step = self.get_step(distance)

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
