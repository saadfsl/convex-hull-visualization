import matplotlib.pyplot as plt
import numpy as np
from algorithms.jarvis_march import jarvis_march
from algorithms.graham_scan import graham_scan
from algorithms.chans_algorithm import chans_algorithm

def static_jarvis_march(points):
  fig, ax = plt.subplots()
  ax.scatter(points[:, 0], points[:, 1], label="Points")
  hull = jarvis_march(points)
  hull_points = np.array(hull)
  ax.plot(hull_points[:, 0], hull_points[:, 1], "r-", label="Convex Hull")
  plt.legend()
  plt.show()

def static_graham_scan(points):
  fig, ax = plt.subplots()
  ax.scatter(points[:, 0], points[:, 1], label="Points")
  hull = graham_scan(points)
  # print(hull)
  hull_points = np.array(hull)
  ax.plot(hull_points[:, 0], hull_points[:, 1], "r-", label="Convex Hull")
  # plot the first point again to close the loop
  ax.plot([hull[0][0], hull[-1][0]], [hull[0][1], hull[-1][1]], "r-")
  plt.legend()
  plt.show()

def static_chans_algorithm(points):
  fig, ax = plt.subplots()
  ax.scatter(points[:, 0], points[:, 1], label="Points")
  hull = chans_algorithm(points)
  hull_points = np.array(hull)
  ax.plot(hull_points[:, 0], hull_points[:, 1], "r-", label="Convex Hull")
  # plot the first point again to close the loop
  # ax.plot([hull[0][0], hull[-1][0]], [hull[0][1], hull[-1][1]], "r-")
  plt.legend()
  plt.show()
