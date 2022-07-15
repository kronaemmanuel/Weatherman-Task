"""
Task Details: https://mixolydian-bugle-21c.notion.site/Weather-Report-83c9f514a3974e5986aea2568f6f0c15
"""

import sys

from data_manager import DataManager
from reports.annual_min_max_report import AnnualMinMaxReport
from reports.hottest_day_report import HottestDayReport
from reports.report import Report

USAGE_TEXT = """
Usage: weatherman [report#] [data_dir]

[Report #]
1 for Annual Max/Min Temperature
2 for Hottest day of each year

[data_dir]
Directory containing weather data files
"""

REPORTS = [AnnualMinMaxReport, HottestDayReport]

if __name__ == '__main__':
    try:
        data_folder_path = sys.argv[1]
        data_manager = DataManager(data_folder_path)

        report_number = int(sys.argv[2])
        if report_number not in (1, 2):
            raise ValueError
    except:
        print('Invalid arguments')
        print(USAGE_TEXT)

    data_manager.import_data()
    report: Report = REPORTS[report_number - 1](data_manager)
    report.printReport()
