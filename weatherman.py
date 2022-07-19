import argparse
import os
import sys

import constants
from data_manager.data_manager import DataManager
from reports.annual_min_max_report import AnnualMinMaxReport
from reports.hottest_day_report import HottestDayReport
from reports.report import Report

parser = argparse.ArgumentParser(prog='weatherman',
                                 description=constants.parser_description, formatter_class=argparse.RawTextHelpFormatter)


parser.add_argument('ReportNumber', metavar='[report#]',
                    type=int, help=constants.report_number_help_text)

parser.add_argument('Path', metavar='[data_dir]', type=str,
                    help=constants.data_directory_help_text)

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
