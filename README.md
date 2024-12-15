# Convex Hull Visualization and Benchmarking

This project implements and visualizes three convex hull algorithms—**Jarvis March**, **Graham Scan**, and **Chan's Algorithm**. It supports benchmarking the algorithms and visualizing their step-by-step construction for various dataset distributions.

- Compatible with **Python 3.8** and above.
- Developed and tested on **Python 3.11**.

## Features
- Visualizations:
  - Animated and static plots.
  - Step-by-step animations for better understanding of algorithms.
- Algorithms:
  - Jarvis March
  - Graham Scan
  - Chan's Algorithm
- Data Distributions:
  - Rectangular
  - Circular
  - Grid
  - Clustered
  - Gaussian
  - Spiral
- Benchmarking:
  - Compare algorithm performance across distributions and dataset sizes.
  - Generates a CSV file with benchmark results.

## Setup and Usage

### Steps to Run (Mac or Linux)
1. Navigate to the Project Root Directory:
   ```bash
   cd path/to/project
   ```

2. Create a Virtual Environment:
   ```bash
   python3 -m venv .venv
   ```

3. Activate the Virtual Environment:
   ```bash
   source .venv/bin/activate
   ```

4. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the Project:
   ```bash
   python main.py
   ```

