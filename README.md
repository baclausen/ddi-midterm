![alt text](images/video_piracy1.png)

## Table of Contents
1. [**Project Overview**](https://github.com/baclausen/ddi-midterm?tab=readme-ov-file#overview)
2. [**Exploratory Focuses**](https://github.com/baclausen/ddi-midterm?tab=readme-ov-file#exploratory-focuses)
3. [**Cleaning**](https://github.com/baclausen/ddi-midterm?tab=readme-ov-file#cleaning)
4. [**Visual Aides**](https://github.com/baclausen/ddi-midterm?tab=readme-ov-file#visualization-of-data)
5. [**Conclusion**](https://github.com/baclausen/ddi-midterm?tab=readme-ov-file#conclusion)
6. [**Sources**](https://github.com/baclausen/ddi-midterm?tab=readme-ov-file#sources)

## Overview
Digital piracy in the United States is a persistent and costly issue, primarily impacting the film, TV, and music sectors. It costs the U.S. economy billions of dollars annually in lost revenue and contributes to substantial job losses, with illegal streaming now the dominant method of infringement. Despite the availability of numerous legal streaming platforms, high costs and content fragmentation are cited as reasons, particularly by younger consumers, who continue to drive unauthorized content consumption. The fight against piracy focuses on reinforcing intellectual property protections and coordinated global enforcement efforts.

This exploratory data analysis observes trends and/correlations in pirated video files to identify what categories of video content are the most susceptible.

## Exploratory Focuses
- Which content had the highest views/downloads?
- What was the average amount of time for a video to be posted?
- Which directors' work is pirated the most?
- What correlations exist between the amount of time a file is posted, the number of downloads, download rate, and IMDb rating?

## Cleaning
The original dataset contained a lot of poorly formatted data. Nearly all values, to include dates, counts of views/downloads, runtimes were stored as strings with inconsistent formats.

1. **Initial Filtering**
   The data contained content derived from various parts of the world. I created and applied a mask onto the dataframe to view only content identified to have originated in the United States.

2. **Dropping the Dead Weight**
   There were a number of columns which were of no use or of which I had no interest for my exploration. I opted to drop these columns rather than correct any missing or erroneous data.

3. **Formatting**
   Numbers were converted from strings, dates were converted and given a uniform format, and uniform runtimes were derived from several varying formats.

4. **Removing Duplicates**
   Once everything was formatted nicely I removed duplicates by grouping on the *title, director, and release date* to ensure I wasn't removing an entry unnecessarily if different movies share the same name. I kept the instance with the highest download rate (duplicates are likely the result of several different uploads of the same movie).

5. **Filling the blanks**
   Columns with string variables were provided an instance of 'Not available' for null values. Missing numeric data was filled using the mean value of the available numeric values.

6. **Additional Engineering**
   New columns performing useful calculations were added before the entirety of the data was organized logically and sorted. Additional filters functions were created for analysis.

## Visualization of Data
*insert charts*
heatmap of numeric data

## Conclusion
*insert findings*

## Sources
The original data was sourced from Kaggle and uploaded by user Arsalan ur Rehman.
The image in the header is AI generated from Google Gemini