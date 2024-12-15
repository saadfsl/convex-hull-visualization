import numpy as np

def generate_points(distribution="rectangular", **kwargs):
  if distribution == "rectangular":
    return _generate_rectangular_points(**kwargs)
  elif distribution == "circular":
    return _generate_circular_points(**kwargs)
  elif distribution == "grid":
    return _generate_grid_points(**kwargs)
  elif distribution == "clustered":
    return _generate_clustered_points(**kwargs)
  elif distribution == "gaussian":
    return _generate_gaussian_points(**kwargs)
  elif distribution == "spiral":
    return _generate_spiral_points(**kwargs)
  else:
    raise ValueError(f"Unknown distribution: {distribution}")

def _generate_rectangular_points(num_points, x_range=(0, 100), y_range=(0, 100)):
  x = np.random.uniform(x_range[0], x_range[1], num_points)
  y = np.random.uniform(y_range[0], y_range[1], num_points)
  return np.column_stack((x, y))

def _generate_circular_points(num_points, center=(50, 50), radius=30):
  angles = np.random.uniform(0, 2 * np.pi, num_points)
  radii = np.sqrt(np.random.uniform(0, 1, num_points)) * radius  # sqrt for uniform density
  x = center[0] + radii * np.cos(angles)
  y = center[1] + radii * np.sin(angles)
  return np.column_stack((x, y))

def _generate_grid_points(grid_size=(10, 10), x_range=(0, 100), y_range=(0, 100)):
  x = np.linspace(x_range[0], x_range[1], grid_size[0])
  y = np.linspace(y_range[0], y_range[1], grid_size[1])
  grid_x, grid_y = np.meshgrid(x, y)
  return np.column_stack((grid_x.ravel(), grid_y.ravel()))

def _generate_clustered_points(num_clusters, points_per_cluster, x_range=(0, 100), y_range=(0, 100), cluster_radius=10):
  cluster_centers = _generate_rectangular_points(num_clusters, x_range, y_range)
  points = []
  for center in cluster_centers:
      points.extend(_generate_circular_points(points_per_cluster, center=center, radius=cluster_radius))
  return np.array(points)

def _generate_gaussian_points(num_points, mean=(50, 50), cov=[[10, 0], [0, 10]]):
  points = np.random.multivariate_normal(mean, cov, num_points)
  return points

def _generate_spiral_points(num_points, num_spirals=3, center=(50, 50), radius=30):
  angles = np.linspace(0, 2 * np.pi * num_spirals, num_points)
  radii = np.linspace(0, radius, num_points)
  x = center[0] + radii * np.cos(angles)
  y = center[1] + radii * np.sin(angles)
  return np.column_stack((x, y))

