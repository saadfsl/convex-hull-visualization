from visualization.animated_plot import animate_jarvis_march, animate_graham_scan, animate_chans_algorithm
from visualization.static_plot import static_jarvis_march, static_graham_scan, static_chans_algorithm
from data.data_generator import generate_points
from benchmarks import main as run_benchmarks

def main():
  print("1. Run Benchmarks")
  print("2. Visualize an Algorithm")
  choice = input("Enter 1 or 2: ")

  if choice == "1":
    run_benchmarks()
  elif choice == "2":
    print("Visualization Options:")
    print("1. Animated Plot")
    print("2. Static Plot")
    plot_type = input("Enter 1 for Animated or 2 for Static: ")

    print("Available Algorithms:")
    print("1. Jarvis March")
    print("2. Graham Scan")
    print("3. Chan's Algorithm")
    algo_choice = input("Choose an algorithm (1-3): ")

    print("Available Distributions:")
    distributions = ["rectangular", "circular", "grid", "clustered", "gaussian", "spiral"]
    for i, dist in enumerate(distributions, 1):
      print(f"{i}. {dist.capitalize()}")
    dist_choice = int(input("Choose a distribution (1-6): ")) - 1

    if distributions[dist_choice] == "grid":
      grid_rows = int(input("Enter the number of rows for the grid: "))
      grid_cols = int(input("Enter the number of columns for the grid: "))
      points = generate_points(distribution="grid", grid_size=(grid_rows, grid_cols))
    elif distributions[dist_choice] == "clustered":
      num_clusters = int(input("Enter the number of clusters: "))
      points_per_cluster = int(input("Enter the number of points per cluster: "))
      points = generate_points(distribution="clustered", num_clusters=num_clusters, points_per_cluster=points_per_cluster)
    else:
      num_points = int(input("Enter the number of points: "))
      points = generate_points(distribution=distributions[dist_choice], num_points=num_points)

    if plot_type == "1":
      animation_speed = input("Enter animation speed in milliseconds (default 750): ")
      try:
        animation_speed = int(animation_speed)
      except ValueError:
        animation_speed = 750

      if algo_choice == "1":
        animate_jarvis_march(points, interval=animation_speed)
      elif algo_choice == "2":
        animate_graham_scan(points, interval=animation_speed)
      elif algo_choice == "3":
        animate_chans_algorithm(points, interval=animation_speed)
      else:
        print("Invalid algorithm choice.")
    elif plot_type == "2":
      if algo_choice == "1":
        static_jarvis_march(points)
      elif algo_choice == "2":
        static_graham_scan(points)
      elif algo_choice == "3":
        static_chans_algorithm(points)
      else:
        print("Invalid algorithm choice.")
    else:
      print("Invalid plot type choice.")
  else:
    print("Invalid choice.")

if __name__ == "__main__":
  main()
