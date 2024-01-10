import numpy as np
import pandas as pd

# Sample data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# Create a DataFrame
df = pd.DataFrame(exam_data)

# Count the number of rows and columns
num_rows = len(df)
num_columns = len(df.columns)

# Display the result
print("Number of Rows:", num_rows)
print("Number of Columns:", num_columns)
