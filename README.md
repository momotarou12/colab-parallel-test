# colab-parallel-test

# Python Parallel Performance Experiment

This repository contains Python code to experiment with the performance of parallel processing using `concurrent.futures.ThreadPoolExecutor`. It helps visualize how increasing the number of parallel workers affects the execution time of I/O-bound tasks (simulated here).

## Files

-   `parallel_experiment.py` (or similar): The main Python script containing the parallel execution experiment logic.
-   (Optional) `plot_results.ipynb` or add plotting code within the main script: Code to visualize the experiment results.

## Setup

No external dependencies beyond standard Python libraries (`time`, `concurrent.futures`, `random`, `pandas`, `matplotlib`, `seaborn`) are strictly required if you run this in an environment like Google Colab or a standard Python installation with these libraries.

## How to Run the Experiment

1.  Save the provided experiment code into a Python file (e.g., `parallel_experiment.py`).
2.  Run the script from your terminal:
    ```bash
    python parallel_experiment.py
    ```
    Or, if using a Jupyter Notebook/Google Colab, paste and run the code cells.

The script will test a range of `MAX_WORKERS` values and print a summary table of execution times.

## How to Visualize Results

If you have the plotting code (either in the same script or a separate notebook), run it after the experiment completes. It will generate a line plot showing Execution Time vs. Number of Parallel Workers.

## Code Description

-   `classify_tag(tag)`: A mock function simulating a task with latency (like an API call).
-   `parallel_classify(tags, max_workers)`: Executes the mock task in parallel using `ThreadPoolExecutor` and measures the duration.
-   The main part of the script loops through `worker_counts_to_test`, runs the `parallel_classify` for each, and collects results.
-   The plotting code uses `matplotlib` and `seaborn` to create a line graph from the collected results (`summary_df`).

## Customization

-   You can change the size of the dummy data (`tags_to_classify_test`).
-   Modify `worker_counts_to_test` to test a different range or granularity of worker counts.
-   Adjust the `time.sleep()` duration in `classify_tag` to simulate different task latencies.

## License

[Specify your license here, e.g., MIT License]
