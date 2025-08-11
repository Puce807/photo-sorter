from sorter import *

source_folder = file_browser("Please select a folder to sort")
answer = input(f"Are you sure you want to select {source_folder}? [y/n] ")
if answer == "n":
    source_folder = file_browser("Please select a folder to sort")
print(f"You have selected {source_folder}")

destination_folder = file_browser("Please select a destination folder")

