import numpy as np
from numpy.random import default_rng

def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    rng = default_rng(10)
    white_noise_ans = rng.normal(0, np.sqrt(np.var(value)/2), size=np.size(value))

    np.testing.assert_allclose(value2, value+white_noise_ans,err_msg='incorrect value vector')
    
    __msg__.good("Well done!")
