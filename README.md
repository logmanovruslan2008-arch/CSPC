# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
```bash
conda env create -f PW<n>/Lab <X>/environment.yml
conda activate cspc
---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- Structure for PW1/Lab A with simulation, tests, and conda environment files.

**Speed comparison (loop vs NumPy):**
- loop : 2.7049 s
- numpy : 0.0003 s
- speed-up: 9324.48 x faster

**Tests:** all passing? yes

**Conclusion:**
- Vectorized operations with NumPy drastically outperform standard pure Python loops for simulating decay across large atom populations. Setting up an isolated Conda environment and automated pytest unit tests ensures strict code reproducibility.

## PW1 --- Lab B: Data, Plotting, and Automation

**Data Summary:**
- Read radioactive decay observations from `decay_observed.csv`.
- Generated a side-by-side plot comparing observed data with the analytical exponential decay law $N(t) = N_0 e^{-\lambda t}$.
- The observed data points closely match the theoretical decay curve.

**Snakemake Automation:**
- Created a `Snakefile` pipeline that automatically checks whether `decay_observed.csv` or `plot.py` have changed and regenerates `figure.png` accordingly without manual command execution.
