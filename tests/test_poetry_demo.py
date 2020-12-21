import numpy as np
import pandas as pd

from poetry_demo import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_something():
    some_array = np.arange(0,100)
    df = pd.DataFrame(
        {'a': some_array, 'b': some_array}
    )

    assert df.shape == (100, 2)
