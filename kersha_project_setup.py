"""
Module: kersha_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Kersha Broussard

"""
#####################################
# Import Modules at the Top
#####################################
import pathlib
import time  # For time.sleep in the periodic folder creation function
import os  # For folder names

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")


    pass

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")
    for year in range(start_year, end_year + 1):
        folder_path = project_path.joinpath(str(year))
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")


def create_folders_from_list(folder_list: list) -> None:
    '''
    Create folders from a list of folder names.
    
    Arguments:
    folder_list -- A list of folder names to create.
    '''
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}")
    for folder_name in folder_list:
        folder_path = project_path.joinpath(folder_name)
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")


def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create folders with a given prefix applied to each name in the list.
    
    Arguments:
    folder_list -- A list of folder names to create.
    prefix -- A string to prepend to each folder name.
    '''
    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix={prefix}")
    for folder_name in folder_list:
        folder_path = project_path.joinpath(f"{prefix}{folder_name}")
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")


def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create folders periodically, one every few seconds.
    
    Arguments:
    duration_seconds -- The delay between folder creation in seconds.
    '''
    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds}")
    folder_index = 1
    while folder_index <= 3:  # Create 3 folders
        folder_path = project_path.joinpath(f"periodic_folder_{folder_index}")
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")
        folder_index += 1
        time.sleep(duration_seconds)


def create_folders_from_list_with_options(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders from a list of folder names with optional modifications.
    
    Arguments:
    folder_list -- A list of folder names to create.
    to_lowercase -- Convert folder names to lowercase.
    remove_spaces -- Remove spaces from folder names.
    '''
    print(f"FUNCTION CALLED: create_folders_from_list_with_options with folder_list={folder_list}, to_lowercase={to_lowercase}, remove_spaces={remove_spaces}")
    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "_")
        folder_path = project_path.joinpath(folder_name)
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")

#####################################
# Define Main Function
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    create_folders_for_range(start_year=2020, end_year=2023)

    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    duration_secs = 2
    create_folders_periodically(duration_secs)

    regions = ["North America", "South America", "Europe", "Asia", "Africa", "Oceania", "Middle East"]
    create_folders_from_list_with_options(regions, to_lowercase=True, remove_spaces=True)

    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()


