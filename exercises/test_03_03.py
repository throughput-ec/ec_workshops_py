import numpy as np


def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    idx_min = np.where(time==200)[0][0]
    idx_max = np.where(time==400)[0][0]

    np.testing.assert_allclose(value2, value[idx_min:idx_max+1], err_msg='Remember that slice notation is exclusive of the final index')

    __msg__.good("Well done!")
