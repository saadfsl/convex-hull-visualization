import time
import pandas as pd
from algorithms.jarvis_march import jarvis_march
from algorithms.graham_scan import graham_scan
from algorithms.chans_algorithm import chans_algorithm
from data.data_generator import generate_points

def benchmark_algorithm(algorithm, points):
  start_time = time.perf_counter()
  algorithm(points)
  end_time = time.perf_counter()
  return end_time - start_time

def run_benchmarks(distributions, num_points_list, algorithms):
  results = []

  for distribution in distributions:
    for num_points in num_points_list:
      if distribution == "grid":
        grid_size = (int(num_points**0.5), int(num_points**0.5))
        points = generate_points(distribution=distribution, grid_size=grid_size)
      elif distribution == "clustered":
        num_clusters = max(1, num_points // 100)
        points_per_cluster = num_points // num_clusters
        points = generate_points(distribution=distribution, num_clusters=num_clusters, points_per_cluster=points_per_cluster)
      else:
        points = generate_points(distribution=distribution, num_points=num_points)

      for algorithm_name, algorithm in algorithms.items():
        exec_time = benchmark_algorithm(algorithm, points)
        results.append({
          "Algorithm": algorithm_name,
          "Distribution": distribution,
          "Num Points": num_points,
          "Execution Time (s)": exec_time,
        })

  results_df = pd.DataFrame(results)
  return results_df

def save_benchmark_results(results_df, filename="benchmark_results.csv"):
  results_df.to_csv(filename, index=False)
  print(f"Results saved to {filename}")

def main():
  algorithms = {
    "Jarvis March": jarvis_march,
    "Graham Scan": graham_scan,
    "Chan's Algorithm": chans_algorithm,
  }

  distributions = ["rectangular", "circular", "grid", "clustered", "gaussian", "spiral"]
  num_points_list = [10, 100, 1000, 5000]

  print("Running benchmarks...")
  results_df = run_benchmarks(distributions, num_points_list, algorithms)

  save_benchmark_results(results_df)

  print("\nBenchmark Results:")
  print(results_df)

if __name__ == "__main__":
  main()