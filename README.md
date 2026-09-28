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
