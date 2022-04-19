import numpy as np

def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    np.testing.assert_allclose(time, np.linspace(0,1000,1001),err_msg='incorrect time vector')
    assert time_index == time[20], 'Wrong index'

    __msg__.good("Well done!")
