import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
file_path = r"C:\Users\HP\Desktop\task\online_courses_uses.csv"
df = pd.read_csv(file_path)
available_categories = df['Category'].unique().tolist()
print("Available categories:", ", ".join(available_categories))
category_input = input("Category (Available categories are listed above, press Enter to skip): ").strip()
if category_input and category_input not in available_categories:
    print(f"Invalid category '{category_input}'. Please choose from the available categories.")
    category_input = None 
def parse_range(input_string):
    try:
        if '-' in input_string:
            start, end = map(float, input_string.split('-'))
            return start, end
        else:
            single_value = float(input_string)
            return single_value, single_value
    except ValueError:
        print("Invalid range input. Please use a single value or a range (e.g., 3-10).")
        return None, None
duration_input = input("Duration (hours, range e.g., 3-10 or single value, press Enter to skip): ").strip()
price_input = input("Price ($, range e.g., 50-100 or single value, press Enter to skip): ").strip()
rating_input = input("Rating (out of 5, range e.g., 3-4.5 or single value, press Enter to skip): ").strip()
filtered_df = df
if category_input:
    filtered_df = filtered_df[filtered_df['Category'] == category_input]
if duration_input:
    start, end = parse_range(duration_input)
    if start is not None:
        filtered_df = filtered_df[(filtered_df['Duration (hours)'] >= start) & (filtered_df['Duration (hours)'] <= end)]
if price_input:
    start, end = parse_range(price_input)
    if start is not None:
        filtered_df = filtered_df[(filtered_df['Price ($)'] >= start) & (filtered_df['Price ($)'] <= end)]
if rating_input:
    start, end = parse_range(rating_input)
    if start is not None:
        filtered_df = filtered_df[(filtered_df['Rating (out of 5)'] >= start) & (filtered_df['Rating (out of 5)'] <= end)]
print("\nRecommended Courses based on your input:")
if not filtered_df.empty:
    print(filtered_df.head(10))
else:
    print("No courses match your criteria.")
def evaluate_system(predicted_ratings, actual_ratings):
    rmse = np.sqrt(mean_squared_error(actual_ratings, predicted_ratings))
    mae = mean_absolute_error(actual_ratings, predicted_ratings)
    return rmse, mae
if not filtered_df.empty:
    predicted_ratings = filtered_df['Rating (out of 5)'].head(5)
    actual_ratings = filtered_df['Rating (out of 5)'].head(5) 
    rmse, mae = evaluate_system(predicted_ratings, actual_ratings)
    print("\nEvaluation Metrics:")
    print(f"RMSE: {rmse:.2f}")
    print(f"MAE: {mae:.2f}")
