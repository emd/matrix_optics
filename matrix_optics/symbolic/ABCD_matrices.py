import sympy


def lens(f):
    '''Return ABCD matrix for thin lens of focal length `f`.

    Parameters:
    -----------
    f - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
        Focal length.
        [f] = AU

    Returns:
    --------
    ABCD - :py:class:`MutableDenseMatrix
        <sympy.matrices.dense.MutableDenseMatrix>` instance

        ABCD ray matrix for thin lens of focal length `f`.

    '''
    return sympy.Matrix([
        [   1,   0],
        [-1 / f, 1]])


def prop(d):
    '''Return ABCD matrix for constant-N propagation by distance `d`.

    Parameters:
    -----------
    d - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
        Propagation distance.
        [d] = AU

    Returns:
    --------
    ABCD - :py:class:`MutableDenseMatrix
        <sympy.matrices.dense.MutableDenseMatrix>` instance

        ABCD ray matrix for constant-N propagation by distance `d`.

    '''
    return sympy.Matrix([
        [1, d],
        [0, 1]])


# Not yet implemented:
# --------------------
# def steer(phi):
#     '''Steer ray (rho, theta) by angle `phi`.
# 
#     Parameters:
#     -----------
#     phi - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
#         Steering angle.
#         [phi] = AU
# 
#     Returns:
#     --------
#     (rho, theta + phi) - :py:class:`MutableDenseMatrix
#         <sympy.matrices.dense.MutableDenseMatrix>` instance
# 
#         Ray steered by angle `phi`.
# 
#     '''
#     return sympy.Matrix([[0], [phi]])
