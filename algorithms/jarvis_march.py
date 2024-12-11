from .helpers import orientation

def jarvis_march(points, visualize=False):
  if visualize:
    return _jarvis_march_generator(points)
  else:
    return _jarvis_march(points)


def _jarvis_march_generator(points):
  hull = []
  left_point = min(points, key=lambda point: point[0])
  on_hull = left_point

  while True:
    hull.append(on_hull)
    next_point = points[0]

    for point in points:
      if (next_point == on_hull).all() or orientation(on_hull, next_point, point) == 1:
        next_point = point
      yield hull, next_point, point

    on_hull = next_point

    if (on_hull == left_point).all():
      break 

  hull.append(left_point)
  yield hull, None, None


def _jarvis_march(points):
  hull = []
  left_point = min(points, key=lambda point: point[0])
  on_hull = left_point

  while True:
    hull.append(on_hull)
    next_point = points[0]

    for point in points:
      if (next_point == on_hull).all() or orientation(on_hull, next_point, point) == 1:
        next_point = point

    on_hull = next_point

    if (on_hull == left_point).all():
      break

  hull.append(left_point)
  return hull

