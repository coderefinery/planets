import matplotlib

matplotlib.use("Agg")  # use the 'Agg' backend which is suitable for file outputs
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

import numpy as np
import csv
import math
import click


def load_sizes(file_name):
    masses = []
    with open(file_name, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            masses.append(float(row["mass"]))
    density = 0.001
    radii = [((3 * mass) / (4 * math.pi * density)) ** (1 / 3) for mass in masses]
    return [2.0 * r for r in radii]


def load_trajectories(file_name):
    data = np.load(file_name)
    return data["arr_0"]


@click.command()
@click.option(
    "--initial-file", type=str, required=True, help="We read the masses from this file."
)
@click.option(
    "--trajectories-file",
    type=str,
    required=True,
    help="We read the trajectories from this file.",
)
@click.option(
    "--output-file", type=str, required=True, help="Video will be written to this file."
)
def main(initial_file, trajectories_file, output_file):
    """Program that animates trajectories."""

    sizes = load_sizes(initial_file)
    trajectories = load_trajectories(trajectories_file)

    fig = plt.figure(dpi=150)
    ax = fig.add_subplot(111, projection="3d")

    def update(frame):
        ax.cla()
        ax.scatter(
            trajectories[frame, :, 0],
            trajectories[frame, :, 1],
            trajectories[frame, :, 2],
            s=sizes,
            c=sizes,
            cmap="BuPu",
        )
        ax.set_xlim([-100.0, 100.0])
        ax.set_ylim([-100.0, 100.0])
        ax.set_zlim([-100.0, 100.0])

    animation = FuncAnimation(fig, update, frames=len(trajectories), repeat=False)
    animation.save(output_file, writer=FFMpegWriter(fps=30))


if __name__ == "__main__":
    main()
