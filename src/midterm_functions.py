import numpy as np
import pandas as pd

# STEP 1-----------------------------------------------------------------------

def us_english_subset(dataframe):
    '''Filter our dataframe by creating a mask of only Hollywood content'''

    only_us = dataframe[dataframe['industry'] == 'Hollywood / English']
    return only_us.reset_index(drop=True)


# STEP 2-----------------------------------------------------------------------

def drop_unwanted_col(dataframe):
    '''Drops specified columns from a list'''
    
    unwanted_cols = ['Unnamed: 0', 'id', 'language', 'writer', 'industry']
    for col in unwanted_cols:
        if col not in dataframe.columns:
            print(f'Skipping {col} which was not found.')
            continue
    dropped_cols = dataframe.drop(unwanted_cols, axis=1)
    return dropped_cols


# STEP 3-----------------------------------------------------------------------

def unavailable_str(dataframe):
    '''Replace null values with a string stating 'Not available' in specified columns'''
    
    text_columns = ['director', 'storyline', 'appropriate_for']
    for col in text_columns:
        if col not in dataframe.columns:
            print(f'Skipping {col} which was not found.')
            continue
        dataframe[col] = dataframe[col].fillna('Not available')
    return dataframe


# STEP 4-----------------------------------------------------------------------

def str_to_int(dataframe):
    '''Converts a string representation of an integer to an actual integer in specified columns'''
    
    nums_as_text = ['views', 'downloads']
    for col in nums_as_text:
        if col not in dataframe.columns:
            print(f'Skipping {col} which was not found.')
            continue
        no_commas = dataframe[col].str.replace(',', '')
        as_float = pd.to_numeric(no_commas, errors='coerce')
        dataframe[col] = as_float.astype(int)
    return dataframe


# STEP 5-----------------------------------------------------------------------

def download_rate(dataframe):
    """Calculate the download rate as a float/percentage of downloads to views."""
    
    site_user_data = ['views', 'downloads']
    for col in site_user_data:
        if col not in dataframe.columns:
            print(f'Skipping {col} which was not found.')
            continue
    if dataframe['views'].dtype == int and dataframe['downloads'].dtype == int and dataframe['views'].gt(0).any():
        dataframe['download_rate'] = round((dataframe['downloads'] / dataframe['views']) * 100, 2)
    return dataframe


# STEP 6-----------------------------------------------------------------------

def date_formatting(dataframe, release_date, posted_date):
    '''Convert date strings from 'MMM DD YYYY' and 'DD MMM, YYYY' formats to uniform datetime objects.'''

    if release_date not in dataframe.columns or posted_date not in dataframe.columns:
        print("Columns do not exist in the dataframe.")
        return dataframe
    
    dataframe[f'{release_date}'] = pd.to_datetime(dataframe[release_date], format="%b %d %Y", errors='coerce')
    dataframe[f'{posted_date}'] = pd.to_datetime(dataframe[posted_date], format="%d %b, %Y", errors='coerce')
    return dataframe


# STEP 6.APPLY-----------------------------------------------------------------------

def standard_run_time(run_time):
    '''Convert run time strings in various formats to integer values representing total minutes'''
    
    run_time = str(run_time)
    total_minutes = 0

    if isinstance(run_time, str):
        format_runtime = run_time = run_time.replace(' hours', 'h ').replace('hours', 'h ').replace(' hour', 'h ').replace('hour', 'h ').replace(' hr', 'h ').replace('hr', 'h ').replace(' h', 'h ')\
                                            .replace(' minutes', 'm').replace('minutes', 'm').replace('min', 'm').replace(' min', 'm').replace(' m', 'm').replace('mins', 'm').replace(' mins', 'm').replace('Not Available', '0h 0m')
        new_runtime = format_runtime.replace('  ', ' ')
        time_split = new_runtime.split()
        for half in time_split:
            if 'h' in half:
                hours = int(half.replace('h', ''))
                total_minutes += hours * 60
            elif 'm' in half:
                minutes = int(half.replace('m', ''))
                total_minutes += minutes
            else:
                other_run_times = pd.to_numeric(run_time, errors='coerce')
                total_minutes += other_run_times
    return total_minutes


# STEP 7-----------------------------------------------------------------------

def avg_value(dataframe):
    '''Fills empty numeric rows with the average completed rows'''
    
    avg_cols = ['IMDb-rating', 'run_time']
    for col in avg_cols:
        dataframe[col] = dataframe[col].fillna(dataframe[col].mean().round(1))
    return dataframe


# STEP 8-----------------------------------------------------------------------

def days_before_posted(dataframe):
    '''Calculates the time between the release and posted dates'''
    
    dataframe['days_before_posted'] = dataframe['posted_date'] - dataframe['release_date']
    return dataframe


# STEP 9-----------------------------------------------------------------------

def polish_dataframe(dataframe):
    '''Organizes the columns in a logical manner for the user to observe and interpret, then sorts the movie data by release date'''
    
    clean_df = dataframe[['title', 'director', 'storyline', 'run_time', 'appropriate_for', 'IMDb-rating',\
                          'release_date', 'posted_date', 'days_before_posted', 'views', 'downloads', 'download_rate']]
    return clean_df.sort_values(by='release_date').reset_index(drop=True)


# -----------------------------------------------------------------------------

def modern_age_movies(dataframe):
    '''Filter our dataframe to contain only movies produced after internet availability'''

    modern_movies = dataframe[dataframe['release_date'] >= '1993-06-24']
    return modern_movies

# EVERYTHING, EVERYWHERE, ALL AT ONCE------------------------------------------

def total_clean(df):
    """Apply all cleaning functions above to the dataframe."""
    
    step_1 = us_english_subset(df)
    step_2 = drop_unwanted_col(step_1)
    step_3 = unavailable_str(step_2)
    step_4 = str_to_int(step_3)
    step_5 = download_rate(step_4)
    step_6 = date_formatting(step_5, 'release_date', 'posted_date')
    step_7 = days_before_posted(step_6)
    step_7['run_time'] = step_7['run_time'].apply(standard_run_time)
    step_8 = avg_value(step_7)
    step_8['run_time'] = step_8['run_time'].astype(int)
    step_9 = polish_dataframe(step_8)
    return step_9


# TESTING AREA-----------------------------------------------------------------

if __name__ == "__main__":
    run_time = '3 h 29 m'
    print(standard_run_time(run_time))