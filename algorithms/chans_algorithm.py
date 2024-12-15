from math import ceil
from .graham_scan import graham_scan
from .helpers import orientation, polar_angle, distance
import numpy as np

def chans_algorithm(points, chan=True, visualize=False):
  if visualize:
    return _chans_algorithm_generator(points)
  else:
    return _chans_algorithm(points, chan)

def _chans_algorithm_generator(points, chan=True):
  n = len(points)
  if n <= 1:
    yield points, [], None, [], []
    return

  t = 0
  while True:
    m = 2 ** (2 ** t) if chan else 2 ** (t + 1)
    t += 1
    c = ceil(n / m)

    subsets = [points[i: i + c] for i in range(0, n, c)]

    hulls = [graham_scan(subset) for subset in subsets]

    merged_hull = []
    leftmost_idx = np.argmax(points[:, 0])
    left_point = tuple(points[leftmost_idx])
    on_hull = left_point

    for _ in range(m):
      merged_hull.append(on_hull)

      tangent_points = [_find_tangent(hull, on_hull) for hull in hulls]
      next_point = tangent_points[0]

      for candidate in tangent_points[1:]:
        o = orientation(on_hull, next_point, candidate)
        if o == 1 or (o == 0 and distance(on_hull, candidate) > distance(on_hull, next_point)):
          next_point = candidate

      # print("next_point: ", next_point)
      yield hulls, merged_hull, on_hull, tangent_points, next_point, m

      if np.array_equal(next_point, left_point):
        merged_hull.append(left_point)
        yield hulls, merged_hull, None, [], None, m
        return

      on_hull = next_point

def _chans_algorithm(points, chan=True):
  n = len(points)
  if n <= 1: return points

  t = 0
  while True:
    m = 2 ** (2 ** t) if chan else 2 ** (t + 1)
    t += 1
    # print(m)
    c = ceil(n / m)

    subsets = [points[i : i + c] for i in range(0, n, c)]

    hulls = [graham_scan(subset) for subset in subsets]

    merged_hull = []
    leftmost_idx = np.argmax(points[:,0])
    left_point = tuple(points[leftmost_idx])
    on_hull = left_point

    for _ in range(m):
      merged_hull.append(on_hull)
      # print("hulls: ", hulls)
      tangent_points = [_find_tangent(hull, on_hull) for hull in hulls]
      # print("tangent_points: ", tangent_points)
      next_point = tangent_points[0]
      for candidate in tangent_points[1:]:
        o = orientation(on_hull, next_point, candidate)
        if o == 1 or (o == 0 and distance(on_hull, candidate) > distance(on_hull, next_point)):
          next_point = candidate

      if np.array_equal(next_point, on_hull):
        break

      if np.array_equal(next_point, left_point):
        merged_hull.append(left_point)
        return merged_hull

      on_hull = next_point
    
    # merged_hull.append(left_point)

# linear scan to find the tangent
# TODO: implement binary search
def _find_tangent(hull, point):
  best = hull[0]
  for p in hull[1:]:
    o = orientation(point, best, p)
    if o > 0 or (o == 0 and distance(point, p) > distance(point, best)):
      best = p
  return best
