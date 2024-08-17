import csv
import click
import numpy as np


# write the data with 2 decimal places only
def write_data(positions, velocities, masses, output_file):
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["px", "py", "pz", "vx", "vy", "vz", "mass"])
        for i in range(len(positions)):
            writer.writerow(
                [
                    f"{positions[i, 0]:.2f}",
                    f"{positions[i, 1]:.2f}",
                    f"{positions[i, 2]:.2f}",
                    f"{velocities[i, 0]:.2f}",
                    f"{velocities[i, 1]:.2f}",
                    f"{velocities[i, 2]:.2f}",
                    f"{masses[i]:.2f}",
                ]
            )


@click.command()
@click.option("--num-planets", type=int, required=True, help="Number of planets.")
@click.option(
    "--output-file", type=str, required=True, help="Data is written to this file."
)
def main(num_planets, output_file):
    """Program that generates random planet positions, velocities, and masses."""

    positions = np.random.uniform(-100.0, 100.0, (num_planets, 3))
    velocities = np.random.uniform(-1.0, 1.0, (num_planets, 3))
    masses = np.random.uniform(0.01, 10.0, num_planets)
    write_data(positions, velocities, masses, output_file)


if __name__ == "__main__":
    main()
