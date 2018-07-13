from nose import tools
import sympy
from sympy.core.numbers import pi, I, oo, Zero

from matrix_optics.symbolic.gaussian_beam import (
    w, R, _check_symbol)


def test__check_symbol():
    # Only sympy.Symbol instances are accepted
    tools.assert_raises(
        TypeError,
        _check_symbol,
        1, 'z')

    # Axial distances must be explicitly real
    z = sympy.symbols('z')
    tools.assert_raises(
        AssertionError,
        _check_symbol,
        z, 'z')

    z = sympy.symbols('z', real=True)
    _check_symbol(z, 'z')

    # Radii of curvature must be explicitly real
    R = sympy.symbols('R')
    tools.assert_raises(
        AssertionError,
        _check_symbol,
        R, 'R')

    R = sympy.symbols('R', real=True)
    _check_symbol(R, 'R')

    # 1/e E radii must be explicitly positive
    w = sympy.symbols('w')
    tools.assert_raises(
        AssertionError,
        _check_symbol,
        w, 'w')

    w = sympy.symbols('w', positive=True)
    _check_symbol(w, 'w')

    # 1/e E beam-waist radii must be explicitly positive
    w0 = sympy.symbols('w0')
    tools.assert_raises(
        AssertionError,
        _check_symbol,
        w0, 'w0')

    w0 = sympy.symbols('w0', positive=True)
    _check_symbol(w0, 'w0')

    # Rayleigh ranges must be explicitly positive
    zR = sympy.symbols('zR')
    tools.assert_raises(
        AssertionError,
        _check_symbol,
        zR, 'zR')

    zR = sympy.symbols('zR', positive=True)
    _check_symbol(zR, 'zR')

    # Non-recognized variable `a` raises ValueError
    tools.assert_raises(
        ValueError,
        _check_symbol,
        zR, 'a')

    return


def test_w_and_R():
    z = sympy.symbols('z', real=True)
    w0, zR = sympy.symbols('w0, zR', positive=True)

    # Straightforward algebra with R(z) and w(z) shows that
    # the below equality is true. (Further, a few additional
    # lines of algebra show that q = z + (i * zR)).
    tools.assert_true(sympy.Equality(
        sympy.simplify(R(z, zR) / (w(z, w0, zR) ** 2)),  # simplify required!
        (zR ** 2) / (z * (w0 ** 2))))

    tools.assert_true(sympy.Equality(
        R(Zero, zR),
        oo))

    return


# def test_GaussianBeam__init__():
#     z = sympy.symbols('z', real=True)
#     w0, zR = sympy.symbols('w0, zR', positive=True)
#     lambda0 = pi * (w0 ** 2) / zR
# 
#     # Test for arbitrary `z`
#     g = GaussianBeam(
#         None,
#         w=w(z, w0, zR),
#         R=R(z, zR),
#         wavelength=lambda0)
# 
#     tools.assert_true(sympy.Equality(
#         sympy.factor(g.q, gaussian=True),
#         z + (I * zR)))
# 
#     tools.assert_true(sympy.Equality(
#         g.R,
#         R(z, zR)))
# 
#     tools.assert_true(sympy.Equality(
#         g.w,
#         w(z, w0, zR)))
# 
#     # Test for arbitrary `z` = 0
# 
#     return
