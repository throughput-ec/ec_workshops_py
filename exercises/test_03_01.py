import numpy as np

def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    np.testing.assert_allclose(value, np.sin(2*np.pi*1/20*time),err_msg='incorrect value vector')
    np.testing.assert_allclose(time, np.arange(1,2001,1),err_msg='incorrect time vector')

    __msg__.good("Well done!")
