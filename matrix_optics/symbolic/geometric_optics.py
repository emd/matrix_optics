import sympy


class Ray(object):
    def __init__(self, rho, theta):
        '''Create an instance of symbolic `Ray` class.

        Input parameters:
        -----------------
        rho - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
            Transverse distance of beam from optical axis.
            [rho] = arbitrary units

        theta - :py:class:`Symbol <sympy.core.symbol.Symbol>` instance
            Angle between ray and optical axis.
            [theta] = rad

        '''
        self.rho = rho
        self.theta = theta

    def applyABCD(self, ABCD):
        'Apply symbolic `ABCD` ray-matrix transformation to ray.'
        A = ABCD[0, 0]
        B = ABCD[0, 1]
        C = ABCD[1, 0]
        D = ABCD[1, 1]

        rho = sympy.simplify((A * self.rho) + (B * self.theta))
        theta = sympy.simplify((C * self.rho) + (D * self.theta))

        return Ray(rho, theta)


def image_distance(ABCD):
    'Get image distance for optical system with symbolic ray matrix `ABCD`.'
    B = ABCD[0, 1]
    D = ABCD[1, 1]
    return sympy.simplify(-B / D)
