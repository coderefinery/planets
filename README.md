# planets: A little example project we use in teaching

This is part of https://coderefinery.github.io/research-software-engineering/.


## Purpose

(...)


## Installation instructions

(...)


## Requirements

(dependencies and their versions or version ranges)


## Example

Generate 10 planets with random initial positions, velocities, and masses,
and save them to a file called `results/initial.csv`:
```bash
python generate-data.py --num-planets 10 --output-file results/initial.csv
```

The generated file will look like this:
```csv
px,py,pz,vx,vy,vz,mass
-46.88,-42.51,88.33,-0.86,-0.18,0.55,6.70
-5.29,17.09,-96.13,0.66,0.45,-0.17,3.51
83.53,-92.83,-68.77,-0.26,-0.48,0.24,6.84
-36.31,25.48,64.16,0.85,0.75,-0.56,1.53
-68.38,-17.21,-97.07,0.60,0.26,0.69,6.63
-48.37,-48.74,3.92,-0.92,-0.33,-0.93,8.60
40.53,-75.50,44.18,-0.62,-0.31,-0.53,8.04
-27.21,10.78,-78.82,-0.09,-0.55,-0.03,5.35
88.42,-74.95,-45.85,0.81,0.68,0.56,5.36
39.09,53.12,-59.54,-0.54,0.56,0.07,8.98
```

In the following example, we generate 500 planets and simulate their motion
for 20 steps using 8 cores in parallel:
```bash
python generate-data.py --num-planets 500 --output-file results/initial.csv

python simulate.py --num-steps 20 \
                   --input-file results/initial.csv \
                   --output-file results/final.csv \
                   --num-cores 8
```

The next example shows how to simulate and animate the motion of 20 planets:
```bash
python generate-data.py --num-planets 20 --output-file results/initial.csv

python simulate.py --num-steps 500 \
                   --input-file results/initial.csv \
                   --output-file results/final.csv \
                   --trajectories-file results/trajectories.npz

python animate.py --initial-file results/initial.csv \
                  --trajectories-file results/trajectories.npz \
                  --output-file results/animation.mp4
```


## Documentation

- Tutorials covering key functionality
- Reference documentation (e.g. API) covering all functionality


## Authors and recommended citation

(...)


## License

(...)


## Contribution guide

(...)
