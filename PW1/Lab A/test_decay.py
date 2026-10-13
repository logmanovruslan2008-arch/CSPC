import numpy as np
import pytest
from decay import simulate, simulate_loop

def test_starts_at_N0():
    assert simulate(1000, 0.4)[0] == 1000

def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)

def test_matches_law():
    N0 = 1000
    lam = 0.4
    dt = 0.05
    steps = 10
    
    runs = [simulate(N0, lam, dt=dt, steps=steps, seed=s)[-1] for s in range(50)]
    avg_result = np.mean(runs)
    
    t = steps * dt
    expected = N0 * np.exp(-lam * t)
    
    assert np.isclose(avg_result, expected, rtol=0.1)
