
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

cone_height = 3  # Define h before the function
def upright_cone(r, h, theta_range=(0, 2*np.pi), z_range=(0, cone_height)):
  """
  Defines an upright cone and plots it in 3D space.

  Args:
      r: Base radius of the cone.
      h: Height of the cone.
      theta_range: Tuple defining the range of theta values (default: 0 to 2*pi).
      z_range: Tuple defining the range of z values (default: 0 to h).

  Returns:
      A 3D plot of the upright cone.
  """
  theta = np.linspace(*theta_range)
  rho = r

  # Convert cylindrical to Cartesian coordinates
  x = rho * np.cos(theta)
  y = rho * np.sin(theta)
  z = np.linspace(*z_range)

  # Create the plot
  fig = plt.figure(figsize=(8, 6))
  ax = fig.add_subplot(111, projection='3d')
  ax.plot_trisurf(x, y, z, cmap='viridis', linewidth=0.2)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  ax.set_title('Upright Cone')
  ax.set_xlim(-r - r/5, r + r/5)
  ax.set_ylim(-r - r/5, r + r/5)
  ax.set_zlim(-h/5, h + h/5)
  plt.show()

def inverted_cone(r, cone_height, theta_range=(0, 2*np.pi), z_range=(-cone_height, 0)):
  """
  Defines an inverted cone and plots it in 3D space.

  Args:
      r: Base radius of the cone.
      h: Height of the cone (positive value).
      theta_range: Tuple defining the range of theta values (default: 0 to 2*pi).
      z_range: Tuple defining the range of z values (default: -h to 0).

  Returns:
      A 3D plot of the inverted cone.
  """
  # Similar approach as upright_cone, adjust for negative z-range
  theta = np.linspace(*theta_range)
  rho = r

  x = rho * np.cos(theta)
  y = rho * np.sin(theta)
  z = np.linspace(*z_range)

  fig = plt.figure(figsize=(8, 6))
  ax = fig.add_subplot(111, projection='3d')
  ax.plot_trisurf(x, y, z, cmap='viridis', linewidth=0.2)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  ax.set_title('Inverted Cone')
  ax.set_xlim(-r - r/5, r + r/5)
  ax.set_ylim(-r - r/5, r + r/5)
  ax.set_zlim(-cone_height - cone_height/5, cone_height/5)
  plt.show()

# Example usage
cone_radius = 2
cone_height = 3
upright_cone(cone_radius, cone_height)
inverted_cone(cone_radius, cone_height)