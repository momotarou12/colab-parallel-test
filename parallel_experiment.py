import time
from concurrent.futures import ThreadPoolExecutor
import random
import pandas as pd

# Mock classification function (simulates API latency)
def classify_tag(tag):
    """
    Simulates a classification task with random latency.
    """
    time.sleep(random.uniform(0.05, 0.2))  # Simulate API latency
    return {"tag": tag, "category": f"category_{random.randint(1,5)}"}

# Parallel classification function
def parallel_classify(tags, max_workers=5):
    """
    Classifies tags in parallel using ThreadPoolExecutor.
    Measures and returns the execution duration.
    """
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(classify_tag, tags))
    end_time = time.time()
    duration = end_time - start_time
    return pd.DataFrame(results), duration

# --- Experiment Setup ---

# Generate a dummy tag list for testing
tags_to_classify_test = [f"tag_{i}" for i in range(300)] # Example: 300 dummy tags

# List of MAX_WORKERS values to test
worker_counts_to_test = list(range(1, 101)) # Test from 1 to 100 workers

print(f"Starting parallel workers experiment with {len(tags_to_classify_test)} tags.")

results_summary = []

# Run the experiment for each worker count
for max_workers in worker_counts_to_test:
    print(f"\nTesting with MAX_WORKERS = {max_workers}...")
    df_result, duration = parallel_classify(tags_to_classify_test, max_workers=max_workers)
    print(f"Finished in {duration:.4f} seconds.")
    results_summary.append({'MAX_WORKERS': max_workers, 'Duration (seconds)': duration})

print("\n--- Experiment Summary ---")
# Create a DataFrame from the summary results
summary_df = pd.DataFrame(results_summary)
print(summary_df)

# Optional: Display results of the last run
# print("\n--- Last Run Results (MAX_WORKERS = {}) ---".format(worker_counts_to_test[-1]))
# print(df_result.head())
