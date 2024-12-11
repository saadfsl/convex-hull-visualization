from .helpers import orientation, distance, polar_angle
import numpy as np

def graham_scan(points, visualize=False):
  if visualize:
    return _graham_scan_generator(points)
  else:
    return _graham_scan(points)
  
def _graham_scan_generator(points):
  p0 = min(points, key=lambda point: (point[0], point[1]))
  sorted_points = sorted(points.tolist(), key=lambda point: (polar_angle(p0, point), distance(p0, point)))
  points = np.array(sorted_points)
  hull = []

  for i in range(len(points)):
    # yield hull, points[i]
    while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) != 1:
      hull.pop()
      yield hull, points[i]
    hull.append(points[i])
    yield hull, points[i]

  yield hull, None

  hull.append(p0)
  yield hull, hull[0]

def _graham_scan(points):
  p0 = min(points, key=lambda point: (point[1], point[0]))
  sorted_points = sorted(points.tolist(), key=lambda point: (polar_angle(p0, point), distance(p0, point)))
  points = np.array(sorted_points)
  hull = []

  for i in range(len(points)):
    while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) <= 0:
      hull.pop()
    hull.append(points[i])

  hull.append(p0)
  return hull
