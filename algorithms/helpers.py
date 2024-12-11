import numpy as np

def orientation(a, b, c):
  d = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
  if d > 0: # Counter-clockwise
    return 1
  elif d < 0: # Clockwise
    return -1
  else: # Collinear
    return 0
  
def distance(p1, p2):
  return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def polar_angle(p0, p):
  return np.arctan2(p[1] - p0[1], p[0] - p0[0])