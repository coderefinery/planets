import numpy as np
import click
import csv


def read_data(input_file):
    with open(input_file) as f:
        reader = csv.reader(f)
        next(reader)
        positions = []
        velocities = []
        masses = []
        for row in reader:
            px, py, pz, vx, vy, vz, m = map(float, row)
            positions.append([px, py, pz])
            velocities.append([vx, vy, vz])
            masses.append(m)
    return np.array(positions), np.array(velocities), np.array(masses)


# write the data with 2 decimal places only
def write_data(positions, output_file):
    with open(output_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["px", "py", "pz"])
        for px, py, pz in positions:
            writer.writerow([f"{px:.2f}", f"{py:.2f}", f"{pz:.2f}"])


def force_between_planets(position1, mass1, position2, mass2):
    G = 1.0  # gravitational constant

    r = position2 - position1
    distance = (r[0] ** 2 + r[1] ** 2 + r[2] ** 2) ** 0.5
    force_magnitude = G * mass1 * mass2 / distance**2
    force = (r / distance) * force_magnitude

    return force


def calculate_forces_range(args):
    start, end, positions, masses = args
    num_planets = len(positions)
    forces = np.zeros((num_planets, 3))
    for i in range(start, end):
        for j in range(i + 1, num_planets):
            force = force_between_planets(
                positions[i], masses[i], positions[j], masses[j]
            )
            forces[i] += force
            forces[j] -= force
    return forces


def calculate_forces(positions, masses):
    num_planets = len(positions)
    args = (0, num_planets, positions, masses)
    return calculate_forces_range(args)


@click.command()
@click.option("--num-steps", type=int, required=True, help="Number of steps.")
@click.option(
    "--input-file", type=str, required=True, help="We read the data from this file."
)
@click.option(
    "--output-file", type=str, required=True, help="Data is written to this file."
)
@click.option(
    "--trajectories-file", type=str, help="File to store trajectories into (optional)."
)
def main(num_steps, input_file, output_file, trajectories_file):
    """Program that simulates the motion of planets."""

    positions, velocities, masses = read_data(input_file)

    dt = 0.1  # time step

    if trajectories_file:
        trajectories = np.zeros((num_steps, len(positions), 3))

    for step in range(num_steps):
        if trajectories_file:
            trajectories[step] = positions

        forces = calculate_forces(positions, masses)

        # update velocities and positions
        accelerations = forces / masses[:, np.newaxis]
        velocities += accelerations * dt
        positions += velocities * dt

    write_data(positions, output_file)

    if trajectories_file:
        np.savez_compressed(trajectories_file, trajectories)

    print(f"Simulated {num_steps} steps. Results written to {output_file}.")


if __name__ == "__main__":
    main()
