# Weatherman

Weatherman is a command line application which creates reports from historical weather data `csv` files.

## Usage
**Required:** Python3

```
python weatherman.py [report_number] [data_directory_path]
```
There are two types of reports that can be generated:

1. Annual min/max temperature:
```
python weatherman.py 1 ./data

Output:
Year        MAX Temp        MIN Temp        MAX Humidity        MIN Humidity
--------------------------------------------------------------------------
1996        40              2               94                  20
1997        40              1               86                  10
1998        40              3               80                  30
```

2. Hottest day of each year:
```
python weatherman.py 2 ./data

Output:
Year        Date          Temp
------------------------------
2006        21/6/2006     45
2007        21/6/2007     47
2008        21/6/2008     46
2009        21/6/2009     43
```

### Debug Mode
If you want to print debug information, you can change `debug_mode` in `constants.py` file to `True`

## Directory Structure

Data directory must be of the following structure and follow the same naming convention:
```
directory-name:
├── lahore_weather_YEAR_MONTH.txt
├── lahore_weather_2000_Jan.txt
├── ...
└── lahore_weather_2011_May.txt
```
- Sub-directories are not supported
- YEAR is a 4 digit string
- MONTH is a 3 character ISO string
- File extension may be .txt or .csv but it will be read as a csv file
- First line of the file is empty
- Second line contains the header
- Indexes(zero-base) of data in the CSV file are as follows:
    - Max Temperature: 1
    - Min Temperature: 3
    - Max Humidity: 7
    - Min Humidity: 9