"""
Task Details: https://mixolydian-bugle-21c.notion.site/Weather-Report-83c9f514a3974e5986aea2568f6f0c15
"""

import os
import sys
import argparse
from data_manager.data_manager import DataManager
from reports.annual_min_max_report import AnnualMinMaxReport
from reports.hottest_day_report import HottestDayReport
from reports.report import Report


parser = argparse.ArgumentParser(prog='weatherman',
                                 description='Generate weatherman reports on given csv data folder', formatter_class=argparse.RawTextHelpFormatter)

REPORT_NUMBER_HELP_TEXT = '1 for Annual Max/Min Temperature\n2 for Hottest day of each year'

parser.add_argument('ReportNumber', metavar='[report#]',
                    type=int, help=REPORT_NUMBER_HELP_TEXT)

parser.add_argument('Path', metavar='[data_dir]', type=str,
                    help='Directory containing weather data files')

args = parser.parse_args()

data_folder_path = args.Path
if not os.path.isdir(data_folder_path):
    print('The path specified does not exist: ', data_folder_path)
    sys.exit()
DataManager = DataManager(data_folder_path)
DataManager.import_data()

report_number = args.ReportNumber
if report_number not in (1, 2):
    print('The report number specified is invalid')
    sys.exit()

REPORTS = [AnnualMinMaxReport, HottestDayReport]
report: Report = REPORTS[report_number - 1](DataManager)
report.printReport()
