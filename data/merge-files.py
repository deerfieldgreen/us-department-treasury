import pandas as pd
import os
import datetime
import requests
from utils import *

columnName = '4 Mo'
defaultValue = '...'

# Get today's date and time as a string
today_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Specify the directory containing the CSV files
directory = os.getcwd() + "/"

my_sorted_list = [ '' ]


my_sorted_list = sort_file_names( directory )
print(my_sorted_list)

merge_files(today_str, my_sorted_list, directory, columnName, defaultValue)



