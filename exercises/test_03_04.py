import numpy as np

def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    np.testing.assert_allclose(time, np.arange(0,10001,100), err_msg='Time vector is incorrect. Remember that the last value is excluded')
    assert np.shape(time_ens) == (101,1000), 'The shape of the ensemble array should be (length of time vector, 1000)'
    assert np.shape(time_mean) == (101,), 'The shape of the mean should be the same as the shape of time'

    __msg__.good("Well done!")
