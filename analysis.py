import pandas as pd

# Ensure summary_df exists
if 'summary_df' in globals() and isinstance(summary_df, pd.DataFrame):
# Calculate the percentage change in Duration (seconds)
# Shift to get the value of the previous row and calculate the difference from the current value
summary_df['Duration_Change'] = summary_df['Duration (seconds)'].diff().abs()

# Calculate the percentage change (NaN for the first row, since there is no reference)
# Percentage change compared to the previous execution time
summary_df['Duration_Change_Percent'] = (summary_df['Duration_Change'] / summary_df['Duration (seconds)'].shift(1)) * 100

print("--- Analysis of Duration Change ---")
display(summary_df[['MAX_WORKERS', 'Duration (seconds)', 'Duration_Change', 'Duration_Change_Percent']])

# Identify the point where the change rate becomes small (e.g., the first point where the change rate becomes less than 1%)
# Consider excluding the first few points (e.g., the first 5 points) because they usually have large changes.
threshold_percent = 1.0 # Threshold for change rate (e.g., 1%)
# Check the change rate from the first number of workers
# Note that the first row's change rate will be NaN because of the shift(1) operation.
plateau_start_index = summary_df[summary_df['Duration_Change_Percent'] < threshold_percent].index.min()

if pd.notna(plateau_start_index):
# Get the initial number of workers where Plateau starts
plateau_start_worker = summary_df.loc[plateau_start_index, 'MAX_WORKERS']
print(f"\nExecution time change becomes less than {threshold_percent}% per worker increase around MAX_WORKERS = {plateau_start_worker}") 
else: 
print(f"\nExecution time change did not drop below {threshold_percent}% within the tested range.")

else: 
print("Error: summary_df not found. Please run the experiment cell first.")
