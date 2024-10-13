import pandas as pd
import os
import datetime
import requests


def merge_files(my_sorted_list, my_directory):
    try:

        merged_df = pd.DataFrame()

        for file in my_sorted_list:
            if file.startswith('daily'):
                continue
            file_path = os.path.join(my_directory, file)
            print(f"Reading file: {file}")
            source_df = pd.read_csv(file_path)
            # if columnName not in source_df.columns:
            #     source_df[columnName] = defaultValue

            merged_df = pd.concat([merged_df, source_df], ignore_index=True)
        # print( merged_df )

        # Save the merged DataFrame to a new CSV file
        # Save the merged DataFrame to a new CSV file with the timestamp
        save_path = os.path.join(my_directory,'daily-treasury-rates.csv')
        merged_df.to_csv(save_path, index=False)
        return merged_df

    except requests.exceptions.RequestException as e:
        print(f"Error adding column: {e}")


# Sort the files by the first 4 characters (year) in descending order
# 2024, 2023, 2022, 2021
def sort_file_names(my_directory):
    try:
        unsorted_csv_files = [
            f for f in os.listdir(my_directory)
            if f.endswith('.csv')
        ]
        return sorted(unsorted_csv_files, key=lambda x: x[:4], reverse=True)

    except requests.exceptions.RequestException as e:
        print(f"Error sorting directory file list")
