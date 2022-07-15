"""
Task Details: https://mixolydian-bugle-21c.notion.site/Weather-Report-83c9f514a3974e5986aea2568f6f0c15
"""


import data_manager
from reports.annual_min_max_report import AnnualMinMaxReport
from reports.hottest_day_report import HottestDayReport


if __name__ == '__main__':
    from data_manager import DataManager

    manager = DataManager()

    manager.import_data('./data')

    report = AnnualMinMaxReport(manager)

    report.printReport()

    reportB = HottestDayReport(manager)

    reportB.printReport()
