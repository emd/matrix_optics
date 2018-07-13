import sympy
from sympy.core.numbers import pi, I, oo, Zero
from sympy.core.singleton import Singleton


class GaussianBeam(object):
    def __init__(self, q, w=None, R=None,
                 wavelength=sympy.symbols('lambda0', positive=True)):
        '''Create an instance of symbolic `GaussianBeam` class.

        Input parameters:
        -----------------
        q - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance, or None
            Complex beam parameter. If `None`, use `w` and `R` to
            determine the corresponding value of `q`.
            [q] = [wavelength]

        w - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
            1/e E radius of Gaussian beam. Only used if `q` is `None`.
            Note that `w` must be explicitly *positive*.
            [w] = [wavelength]

        R - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
            Radius of curvature of Gaussian beam. Only used if `q` is `None`.
            Note that `R` must be explicitly *real* and that a value of
            infinity corresponds to a beam waist.
            [R] = [wavelength]

        wavelength - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
            Wavelength of Gaussian beam. Note that `wavelength` must be
            explicitly *positive*.
            [wavelength] = arbitrary units

        '''
        # Enforce that wavelength is always positive.
        _check_symbol(wavelength, 'lambda0')
        self.wavelength = wavelength

        if q is None:
            if (w is not None) and (R is not None):
                _check_symbol(w, 'w')
                _check_symbol(R, 'R')

                qinv = (1 / R) - (I * self.wavelength / (pi * (w ** 2)))
                self.q = sympy.simplify(1 / qinv)
            else:
                raise ValueError(
                    'Both `w` & `R` must be specified if `q` is None')
        else:
            self.q = q

    @property
    def R(self):
        'Get radius of curvature.'
        Rinv = sympy.re(1 / self.q)

        if Rinv == Zero:
            return oo
        else:
            return sympy.simplify(1 / Rinv)

    @property
    def w(self):
        'Get 1/e E radius.'
        qinv = 1 / self.q
        return sympy.simplify(
            sympy.sqrt(-self.wavelength / (pi * sympy.im(qinv))))


def w(z, w0, zR):
    '''Gaussian beam 1/e E radius.

    Parameters:
    -----------
    z - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
        The axial distance from the beam waist.
        [z] = arbitrary units

    w0 - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
        1/e E radius of beam waist.
        [w0] = [z]

    zR - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
        Rayleigh range of beam.
        [zR] = [z]

    Returns:
    --------
    w - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
        The beam 1/e E radius as a function of the axial distance `z`
        from the beam waist.
        [w] = [z]

    '''
    _check_symbol(z, 'z')
    _check_symbol(w0, 'w0')
    _check_symbol(zR, 'zR')

    return sympy.simplify(w0 * sympy.sqrt(1 + ((z / zR) ** 2)))


def R(z, zR):
    '''Gaussian beam radius of curvature.

    Parameters:
    -----------
    z - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
        The axial distance from the beam waist.
        [z] = arbitrary units

    zR - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
        Rayleigh range of beam.
        [zR] = [z]

    Returns:
    --------
    R - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
        The beam radius of curvature as a function of the axial distance `z`
        from the beam waist.
        [R] = [z]

    '''
    _check_symbol(z, 'z')
    _check_symbol(zR, 'zR')

    # Waist needs special treatment, as sympy does not correctly evaluate
    # the general expression.
    if z == Zero:
        return oo
    else:
        return sympy.simplify(z * (1 + ((zR / z) ** 2)))


def _check_symbol(sym, var):
    '''Check that symbol `sym` has required properties for variable `var`.

    Input parameters:
    -----------------
    sym - a sympy expression, variable, or singleton
        The symbol to be used for representation of variable `var`.

    var - string
        The variable to be represented by symbol `sym`.
        Accepted variables are

                ['z', 'R', 'w', 'w0', 'zR', 'lambda0']

        otherwise a ValueError is raised.

    Returns:
    --------
    None if symbol `sym` has required properties for variable `var`;
        otherwise an exception is raised.

    '''
    # Ensure `sym` is an instance of sympy `Symbol` class
    if not (isinstance(sym, sympy.Expr) or isinstance(sym, Singleton)):
        raise TypeError(
            '`sym` must be an instance of sympy Symbol or Singleton class.')

    if var == 'z':
        # Axial distance `z` must be explicitly real
        assert sym.is_real, '`%s` must be explicitly *real*.' % sym
    elif var == 'R':
        # Radius of curvature `R` must be explicitly real
        assert sym.is_real, '`%s` must be explicitly *real*.' % sym
    elif var == 'w':
        # 1/e E radius `w` must be explicitly positive
        assert sym.is_positive, '`%s` must be explicitly *positive*.' % sym
    elif var == 'w0':
        # 1/e E beam-waist radius `w0` must be explicitly positive
        assert sym.is_positive, '`%s` must be explicitly *positive*.' % sym
    elif var == 'zR':
        # Rayleigh range `zR` must be explicitly positive
        assert sym.is_positive, '`%s` must be explicitly *positive*.' % sym
    elif var == 'lambda0':
        # Vacuum wavelength `lambda0` must be explicitly positive
        assert sym.is_positive, '`%s` must be explicitly *positive*.' % sym
    else:
        raise ValueError("'%s' *not* a recognized variable." % var)

    return
