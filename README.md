# Digital Piracy of US Content
![alt text](images/video_piracy1.png)

## Table of Contents
1. **Project Overview**
2. **Exploratory Focuses**
3. **Cleaning**
4. **Visual Aides**
5. **Conclusion**
6. **Sources**

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

4. **Filling the blanks**
   Columns with string variables were provided an instance of 'Not available' for null values. Missing numeric data was filled using the mean value of the available numeric values.

5. **Additional Engineering**
   New columns performing useful calculations were added before the entirety of the data was organized logically and sorted. Additional filters functions were created for analysis.

## Visualization of Data
*insert charts*

## Conclusion
*insert findings*

## Sources
1. **Data set**
The original data was sourced from Kaggle and uploaded by user Arsalan ur Rehman.
The image in the header can be located at www.freepik.com