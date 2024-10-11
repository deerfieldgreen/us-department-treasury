import pandas as pd
import os
import datetime
import requests



def merge_files(my_timestamp, my_sorted_list, my_directory, columnName, defaultValue):
	try:	
		
		merged_df = pd.DataFrame()


		for file in my_sorted_list:
			file_path = os.path.join( my_directory, file)
			print(f"Reading file: {file}")
			source_df = pd.DataFrame()
			source_df = pd.read_csv( file_path )
			if columnName not in source_df.columns:
				source_df[columnName] = defaultValue


			merged_df = pd.concat([merged_df, source_df], ignore_index=True)
			#print( merged_df )

		
		# Save the merged DataFrame to a new CSV file
		merged_df.to_csv('daily-treasury-rates.csv', index=False)
		# Save the merged DataFrame to a new CSV file with the timestamp
		merged_df.to_csv(f'{my_timestamp}-merged-daily-treasury-rates.csv-snapshot', index=False)
	



	except requests.exceptions.RequestException as e:
		print(f"Error adding column: {e}")

	


# Sort the files by the first 4 characters (year) in descending order
# 2024, 2023, 2022, 2021
def sort_file_names( my_directory ):
	try:
		unsorted_csv_files = [
        	f for f in os.listdir( my_directory ) 
            	if f.endswith('.csv.m')
            	]
		return sorted( unsorted_csv_files, key=lambda x: x[:4], reverse=True)

	except requests.exceptions.RequestException as e:
		print( f"Error sorting directory file list")

    



