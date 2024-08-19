# planets: A little example project we use in teaching

This is part of https://coderefinery.github.io/research-software-engineering/.


## Purpose

(...)


## Requirements

- Python (tested with Python 3.12)


## Installation instructions

(...)


## Example

The code is written to accept **command-line arguments** to specify the number
of planets and the number of time steps.

We first generate starting data:
```console
$ python generate-data.py --num-planets 10 --output-file initial.csv
```

The generated file (initial.csv) could look like this:
```
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

Then we can simulate their motion (in this case for 20 steps):
```console
$ python simulate.py --num-steps 20 \
                     --input-file initial.csv \
                     --output-file final.csv
```

The `--output-file` (final.csv) is again a CSV file (comma-separated values)
and contains the final positions of all planets.

It is possible to run on **multiple cores** and to **animate** the result.
Here is an example with 100 planets:
```console
$ python generate-data.py --num-planets 100 --output-file initial.csv

$ python simulate.py --num-steps 50 \
                     --input-file initial.csv \
                     --output-file final.csv \
                     --trajectories-file trajectories.npz \
                     --num-cores 8

$ python animate.py --initial-file initial.csv \
                    --trajectories-file trajectories.npz \
                    --output-file animation.mp4
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
