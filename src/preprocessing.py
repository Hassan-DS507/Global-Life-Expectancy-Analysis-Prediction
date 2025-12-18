import pandas as pd
import numpy as np

def Check_Pattern(missing, null_col):

  """
  This function checks the missing pattern mechanism of a DataFrame.

  Parameters
  ----------
  missing : pandas.DataFrame of other columns values when the missed column is NaN.

  Returns
  -------
  pandas.DataFrame
      The DataFrame with the unique values for feature that has one or 2 unique value when a spasific feature is missed.

  """
  missing = missing.drop(null_col, axis=1, errors='ignore')
  # Create a new DataFrame to store the unique values for each feature
  unique_df = pd.DataFrame(data = np.random.rand(2))

  # Iterate over the columns of the DataFrame
  for col in missing.columns:

      # Get the number of unique values in the column
      nunique = missing[col].nunique()

      # If the number of unique values is 1 or 2, add the unique values to the DataFrame
      if nunique in [0, 1, 2]:
          unique_df.loc[:nunique, col + '_unique_vals'] = missing[col].unique()

  # Drop the first row from the DataFrame
  unique_df.drop(0, axis=1, inplace=True)

  # Interpret the result of unique_df
  if unique_df.empty:
      print(f'\t- Missing values in `{null_col}` are randomly distributed across the dataset')
      print(f'\t- So that the missing pattern mechanism should be: Missing Completely At Random (MCAR)')
  else:
      print(f'\t- Missing values in `{null_col}` depend on the values of other columns. Columns that have 1 or 2 unique are: {list(unique_df.columns)}')
      print(f'\t- So that the missing pattern mechanism should be: Missing At Random (MAR) or Missing Not At Random (MNAR)')
  # Return the DataFrame with the unique values for feature that has one or 2 unique value when a spasific feature is missed.
  return unique_df
###############################################################################################################################################
# Investigate the patterns of missing values in each column
def Missing_Pattern(col, top_3, df):
    print(f"\nFeature: {col}")
    print('-'*33)
    print(f"\t- Number of missing values: {top_3[col]}")
    print(f"\t- Percentage of missing values: {(top_3[col]/len(df))*100:.2f}%")
    print(f"\t- Data type: {df[col].dtype}")
    print(f"\t- Number of unique values: {df[col].nunique()}")
    print(f"\t- Most common value: {df[col].value_counts().idxmax()}")
    print(f"\nMissing value pattern:")
    print('-'*30)
    # other features values when col is missed
    missing = df[df[col].isna()]
    unique_df = Check_Pattern(missing, col)
    return missing, unique_df
