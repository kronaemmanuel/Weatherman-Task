Here is the next assignment. Only the standard python library is allowed.

**Weather Man**

Attached file contains weather data for Lahore from 1996 to 2011. Your task is to write an application that generates reports on the given data.

1. Annual Max/Min Temp: Print a table as follows

```python
Year        MAX Temp        MIN Temp        MAX Humidity        MIN Humidity
--------------------------------------------------------------------------
1996        40              2               94                  20
1997        40              1               86                  10
1998        40              3               80                  30
```

2. Hottest days of each year

```python
Year        Date          Temp
------------------------------
2006        21/6/2006     45
2007        21/6/2007     47
2008        21/6/2008     46
2009        21/6/2009     43
```

Program should take two parameters: report number and weather data directory. If no parameter is provided print the application usage info. According to above reports a usage output could be like

```python
Usage: weatherman [report#] [data_dir]

[Report #]
1 for Annual Max/Min Temperature
2 for Hottest day of each year

[data_dir]
Directory containing weather data files
```

Let me know if you have any questions. Once the assignment is done please push it to github and add me as a reviewer