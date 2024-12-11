import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from algorithms.jarvis_march import jarvis_march
from algorithms.graham_scan import graham_scan
from algorithms.chans_algorithm import chans_algorithm
from matplotlib.cm import get_cmap

def animate_jarvis_march(points, interval=750):
  fig, ax = plt.subplots()
  ax.scatter(points[:, 0], points[:, 1], label="Points")
  line, = ax.plot([], [], "r-", label="Convex Hull")
  candidate_line, = ax.plot([], [], "b-", label="Candidate Edge")
  comparison_point, = ax.plot([], [], "o", color="orange", label="Current Comparison")

  generator = jarvis_march(points, visualize=True)

  def update(data):
    try:
      hull, next_point, point = next(generator)

      if len(hull) > 1:
        hull_points = np.array(hull)
        line.set_data(hull_points[:, 0], hull_points[:, 1])

      if next_point is not None:
        candidate_line.set_data([hull[-1][0], next_point[0]], [hull[-1][1], next_point[1]])
      else:
        candidate_line.set_data([hull[-2][0], hull[0][0]], [hull[-2][1], hull[0][1]])
        candidate_line.set_color("r")

      if point is not None:
        comparison_point.set_data([point[0]], [point[1]])

      return line, candidate_line, comparison_point
    except StopIteration:
      ani.event_source.stop()

  ani = animation.FuncAnimation(fig, update, interval=interval)
  plt.legend()
  plt.show()

def animate_graham_scan(points, interval=750):
  fig, ax = plt.subplots()
  ax.scatter(points[:, 0], points[:, 1], label="Points")
  line, = ax.plot([], [], "r-", label="Convex Hull")
  candidate_line, = ax.plot([], [], "b-", label="Candidate Edge")
  # comparison_point, = ax.plot([], [], "go", label="Current Comparison")

  generator = graham_scan(points, visualize=True)

  def update(data):
    try:
      hull, point = next(generator)

      if len(hull) > 1:
        hull_points = np.array(hull)
        line.set_data(hull_points[:, 0], hull_points[:, 1])

      if point is not None and point is not hull[0]:
        candidate_line.set_data([hull[-1][0], point[0]], [hull[-1][1], point[1]])
        candidate_line.set_color("b")
      else:
        candidate_line.set_data([hull[-1][0], hull[0][0]], [hull[-1][1], hull[0][1]])
        candidate_line.set_color("r")

      return line
    except StopIteration:
      ani.event_source.stop()

  ani = animation.FuncAnimation(fig, update, interval=interval)
  plt.legend()
  plt.show()

def animate_chans_algorithm(points, interval=750):
  fig, ax = plt.subplots()
  ax.set_xlim(points[:, 0].min() - 10, points[:, 0].max() + 10)
  ax.set_ylim(points[:, 1].min() - 10, points[:, 1].max() + 10)
  ax.scatter(points[:, 0], points[:, 1], color="black", label="Points")

  local_hull_lines = []
  global_hull_line, = ax.plot([], [], "r-", label="Global Hull")
  candidate_lines = []
  current_point_marker, = ax.plot([], [], "ro", label="Current Hull Point")
  next_point_marker, = ax.plot([], [], "go", label="Next Point")
  m_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12)

  generator = chans_algorithm(points, visualize=True)

  def update(data):
    try:
      hulls, merged_hull, on_hull, tangent_points, next_point, m = next(generator)
      # print("m: ", m)
      # print("local hulls: ", hulls)

      cmap = get_cmap("tab10")

      while len(local_hull_lines) < len(hulls):
        line, = ax.plot([], [], "-", alpha=0.8, label="Local Hull")
        local_hull_lines.append(line)
      for i, hull in enumerate(hulls):
        if len(hull) > 0:
          hull_points = np.array(hull)
          hull_points = np.vstack([hull_points, hull_points[0]])
          local_hull_lines[i].set_data(hull_points[:, 0], hull_points[:, 1])
          local_hull_lines[i].set_color(cmap(i % 10))
        else:
          local_hull_lines[i].set_data([], [])
      for i in range(len(hulls), len(local_hull_lines)):
        local_hull_lines[i].set_data([], [])

      if len(merged_hull) > 1:
        global_hull_line.set_data(np.array(merged_hull)[:, 0], np.array(merged_hull)[:, 1])

      while len(candidate_lines) < len(tangent_points):
        line, = ax.plot([], [], "b--", alpha=0.5, label="Candidate Line")
        candidate_lines.append(line)
      for i, tangent in enumerate(tangent_points):
        if on_hull is not None:
          candidate_lines[i].set_data([on_hull[0], tangent[0]], [on_hull[1], tangent[1]])
        else:
          candidate_lines[i].set_data([], [])
      for i in range(len(tangent_points), len(candidate_lines)):
        candidate_lines[i].set_data([], [])

      if on_hull is not None:
        on_hull = np.asarray(on_hull).flatten()
        current_point_marker.set_data([on_hull[0]], [on_hull[1]])
      else:
        current_point_marker.set_data([], [])

      if next_point is not None:
        next_point = np.asarray(next_point).flatten()
        next_point_marker.set_data([next_point[0]], [next_point[1]])
      else:
        next_point_marker.set_data([], [])

      m_text.set_text(f"m = {m}")

      return (
        local_hull_lines
        + [global_hull_line]
        + candidate_lines
        + [current_point_marker, next_point_marker, m_text]
      )

    except StopIteration:
      ani.event_source.stop()

  ani = animation.FuncAnimation(fig, update, interval=interval)
  plt.legend()
  plt.show()


