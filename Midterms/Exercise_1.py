# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 23:04:27 2024

@author: MADT
"""

def upright_cone(r, h):
  """
  Defines an upright cone in cylindrical and Cartesian coordinates.

  Args:
      r: Base radius of the cone.
      h: Height of the cone.

  Returns:
      A tuple containing cylindrical and Cartesian equations as strings.
  """
  cylindrical_eq = f"0 <= z <= {h}\n0 <= phi <= 2*pi\nrho <= {r}"
  cartesian_eq = f"x**2 + y**2 <= {r**2}\n0 <= z <= {h}\nz = {h/r} * sqrt(x**2 + y**2)"
  return cylindrical_eq, cartesian_eq

def inverted_cone(r, h):
  """
  Defines an inverted cone in cylindrical and Cartesian coordinates.

  Args:
      r: Base radius of the cone.
      h: Height of the cone (positive value).

  Returns:
      A tuple containing cylindrical and Cartesian equations as strings.
  """
  cylindrical_eq = f"0 <= phi <= 2*pi\nrho <= {r}\n-h <= z <= 0"
  cartesian_eq = f"x**2 + y**2 <= {r**2}\n-{h} <= z <= 0\nz = -({h/r}) * sqrt(x**2 + y**2)"
  return cylindrical_eq, cartesian_eq

# Example usage
cone_radius = 2
cone_height = 3
upright_cyl, upright_cart = upright_cone(cone_radius, cone_height)
inverted_cyl, inverted_cart = inverted_cone(cone_radius, cone_height)

print("Upright Cone:")
print("Cylindrical:", upright_cyl)
print("Cartesian:", upright_cart)

print("\nInverted Cone:")
print("Cylindrical:", inverted_cyl)
print("Cartesian:", inverted_cart)