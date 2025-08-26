import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Assuming summary_df DataFrame exists from the previous experiment code
if 'summary_df' in globals() and isinstance(summary_df, pd.DataFrame):
    # Create the plot
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=summary_df, x='MAX_WORKERS', y='Duration (seconds)')
    plt.title('Execution Time vs. Number of Parallel Workers')
    plt.xlabel('Number of Parallel Workers')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()

    # Calculate and display performance metrics
    min_duration = summary_df['Duration (seconds)'].min()
    print(f"Minimum execution time observed: {min_duration:.4f} seconds")

    # Find worker counts near the minimum time (e.g., within 10%)
    near_optimal_workers = summary_df[summary_df['Duration (seconds)'] <= min_duration * 1.1]['MAX_WORKERS'].tolist()
    print(f"Worker counts with execution time near the minimum (within 10%): {near_optimal_workers}")

else:
    print("Error: summary_df not found or is not a DataFrame. Please run the experiment code first.")
