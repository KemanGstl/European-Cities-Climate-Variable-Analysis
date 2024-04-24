# Geneva Climate Variables Analysis
This document outlines my process of analysing various climate aspects of Geneva. 
The goal is to better understand how the climate changed during a specific time period.

Note: This is a personal project which aims to teach me how to drive a climate analysis, hone my Python coding skills for data analysis, its processes and other knowledge I find interesting or am passionate about (e.g., climate change, coding, analysis and many more, related or not, to this project). Everything is done on my spare time, continuous learning being a personal value. Any constructive feedback is appreciated. This .md file acts as a journal, with the problems I will encounter and the solutions I will find.


## Table of contents

- [Introduction](#introduction)
- [CDS data access with API](#cds-data-access-with-api)
- [Visualisation in QGIS](#visualisation-with-qgis)
- 

## Introduction
Analysis of Climate Variables of Geneva, from 2008 to 2017, using data from the [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/cdsapp#!/dataset/sis-urban-climate-cities?tab=overview).
Multiple variables will be analysed, including Air Temperature, Wind speed, Relative humidity & more.
Data is requested from the Copernicus Climate Data Store (CDS), using an API key.
I am starting with the Air Temperature data. 

## CDS data access with API
Before any analysis can happen, data needs to be requested from CDS. The use of an API key is not necessary at this scale but an interesting thing to learn. Especially since it can be a transferable skill.
[Here](https://github.com/KemanGstl/European-Cities-Climate-Variable-Analysis/blob/main/CDS_Data_Access_With_API.md) is the process I went through for my first data set request, the Air Temperature variable.
The data is locally downloaded as monthly files (hourly data) for each year. 

## Concatenate the data
A total of 120 NetCDF (.nc) files for Geneva's air temperature have been downloaded for a total of about 3.3GB (spoiler: my PC cannot handle so much at once for manipulation). [Appending](https://github.com/KemanGstl/Geneva-Climate-Variables-Analysis/blob/main/AirTempAppend.py) the data is necessary for process and analysis in both Python and QGIS.

## Visualisation in QGIS
A new project is started, with the Coordinate Reference System (CRS) EPSG:4326 (based on WGS84 datum).

The file being too large for manipulation, I have selected the month of January 2017. It is added as a raster layer to the project, under the OpenStreetMap layer to view the city of Geneva and the air temperture data. The symbology for the air temp is modified to better fit its meaning, the render type is switched to Singleband pseudocolor and inversed to fit cold temperature with cold colours and vice versa.
One big issue quickly arises, the air temperature data is not showing on the street map but completely out of bounds. It also seems that the scale is off by an earth (non-official unit). As it can be seen in the following screenshot:
![image](https://github.com/KemanGstl/Geneva-Climate-Variables-Analysis/assets/146002850/51e201b4-b036-4627-a0fe-6a90a625c18e)


### Issue 1
After multiple days of research and attempding to troubleshoot by changing the CRS or explore the data, I found a video from the European Organisation for the Exploitation of Meteorological Satellites (EUMETSAT) youtube channel where Daniel Lee goes through the steps of [visualising data in NetCDF format](https://www.youtube.com/watch?v=XqoetylQAIY).
In this video, he goes on to troubleshoot coordinate systems. The filter has been mirrored, the north & south axis have been reversed, same with the west & east axis. Using this, I am able to "repair" the system, by changing the format of the file, from NetCDF (.nc) to GeoTIFF (.tiff).

### Issue 2
Now that the alignement has been taken care of, I can see that the minimum temperature is set at 0 K. Logging a natural absolute zero at Earth surface would have made the news, therefore there has been an issue during formatting.
To tackle this issue, considering the potential use of dozens of files, Python will be used to conserve the integrity of the data, as shown [here]().

Currently loading QGIS training manual in my skillset, please wait...



