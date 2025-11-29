#  Trigonmetric and Geometric Functions

#  acos(x)      Return the arc cosine (measured in radians) of x.
#  acosh(x)     Return the inverse hyperbolic cosine of x.
#  asin(x)      Return the arc sine (measured in radians) of x.
#  asinh(x)     Return the inverse hyperbolic sine of x.
#  atan(x)      Return the arc tangent (measured in radians) of x.
#  atanh(x)     Return the inverse hyperbolic tangent of x.
#  cos(x)       Return the cosine of x (measured in radians).
#  cosh(x)      Return the hyperbolic cosine of x.
#  degrees(x)   Convert angle x from radians to degrees.
#  dist(p, q)   Return the Euclidean distance between two points p and q.
#  hypot(x, y)  Return the Euclidean distance, sqrt(x*x + y*y).
#  radians(x)   Convert angle x from degrees to radians.
#  sin(x)       Return the sine of x (measured in radians).
#  sinh(x)      Return the hyperbolic sine of x.
#  tan(x)       Return the tangent of x (measured in radians).
#  tanh(x)      Return the hyperbolic tangent of x.

import math

angle_degrees = 60
angle_radians = math.radians(angle_degrees)
sin_value = math.sin(angle_radians)
print(f"Sine of {angle_degrees} degrees is {sin_value}")