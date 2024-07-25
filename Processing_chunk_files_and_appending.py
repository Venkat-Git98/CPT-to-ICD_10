import pandas as pd
import os
import sys

def add_index_column(df, index_column_name='Index'):
    """
    Adds an index column to a DataFrame if not already present.
    
    Args:
    df (DataFrame): The pandas DataFrame to modify.
    index_column_name (str): The name of the new index column.
    
    Returns:
    DataFrame: The modified DataFrame with a new index column.
    """
    if index_column_name not in df.columns:
        df.reset_index(drop=False, inplace=True)
        df.rename(columns={'index': index_column_name}, inplace=True)
    return df

def verify_and_concatenate_csvs(folder_path, output_file, index_column_name='Index'):
    """
    Verifies column consistency across CSV files, adds an index column, and concatenates them into a single CSV file.
    
    Args:
    folder_path (str): Directory path containing the CSV files.
    output_file (str): Path to save the concatenated CSV file.
    index_column_name (str): Name for the index column to be added to each file.
    """
    all_data = []
    template_cols = None

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)

            # Check for column consistency
            if template_cols is None:
                template_cols = df.columns.tolist()
            elif set(template_cols) != set(df.columns.tolist()):
                print(f"Column mismatch in {filename}. Expected {template_cols}, but got {df.columns.tolist()}")
                continue

            # Add index column
            df = add_index_column(df, index_column_name)

            # Ensure columns are in the same order
            df = df[template_cols + [index_column_name] if index_column_name not in template_cols else template_cols]

            all_data.append(df)

    # Concatenate all data
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv(output_file, index=False)
    print(f"Merging complete. Output file created: {output_file}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python csv_processing_tool.py [folder_path] [output_file]")
        sys.exit(1)
    folder_path = "[Folder path containing all the chunk csv files"
    output_file = "[Output_file_name"]
    folder_path = sys.argv[1]
    output_file = sys.argv[2]
    verify_and_concatenate_csvs(folder_path, output_file)

if __name__ == "__main__":
    main()

