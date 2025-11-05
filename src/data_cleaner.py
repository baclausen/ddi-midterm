# Import libraries
import numpy as np
import pandas as pd
import midterm_functions as mf
import matplotlib.pyplot as plt
import seaborn as sns

'''Change the working directory to the src folder, if needed'''

if __name__ == '__main__':

    # Import the data
    df = pd.read_csv('../data/pirated_video.csv')

    # Run our cleaning pipeline and inspect the results
    df = mf.total_clean(df)

    # Write the results to file
    df.to_csv('../data/cleaned_pirated_video.csv', index=False)