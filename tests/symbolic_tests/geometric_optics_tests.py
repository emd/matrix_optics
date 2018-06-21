from nose import tools
import sympy

from matrix_optics.symbolic.ABCD_matrices import lens, prop
from matrix_optics.symbolic.geometric_optics import Ray, image_distance


def test_Ray_propagation():
    rho0, theta0, d = sympy.symbols('rho0, theta0, d')
    r0 = Ray(rho0, theta0)

    # Propagation does *not* change angle `theta` but does change
    # `rho` if `theta` is non-zero
    r = r0.applyABCD(prop(d))
    tools.assert_true(sympy.Equality(r.rho, rho0 + (d * theta0)))
    tools.assert_true(sympy.Equality(r.theta, theta0))

    return


def test_Ray_focusing():
    rho0, theta0, f = sympy.symbols('rho0, theta0, f')
    r0 = Ray(rho0, theta0)

    # Immediately after lens, transverse distance `rho` is not altered, but
    # angle `theta` is altered
    r = r0.applyABCD(lens(f))
    tools.assert_true(sympy.Equality(r.rho, rho0))
    tools.assert_true(sympy.Equality(r.theta, theta0 - (rho0 / f)))

    return


def test_Ray_imaging():
    rho0, theta0, M, C = sympy.symbols('rho0, theta0, M, C')
    r0 = Ray(rho0, theta0)

    # Arbitrary magnification `M` imaging system
    ABCD = sympy.Matrix([
        [M,    0. ],
        [C, 1. / M]])

    r = r0.applyABCD(ABCD)
    tools.assert_true(sympy.Equality(r.rho, M * rho0))
    tools.assert_true(sympy.Equality(r.theta, (theta0 / M) + (C * rho0)))

    return


def test_image_distance():
    s0, f = sympy.symbols('s0, f')

    # Expected image distance
    sprime = (s0 * f) / (s0 - f)

    tools.assert_true(sympy.Equality(
        image_distance(lens(f) * prop(s0)),
        sprime))

    return
