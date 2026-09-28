"""
Tests for the decay simulation.
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop

def test_starts_at_N0():
    assert simulate(1000, 0.4)[0] == 1000
