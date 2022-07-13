"""
Task Details: https://mixolydian-bugle-21c.notion.site/Weather-Report-83c9f514a3974e5986aea2568f6f0c15
"""


import data_manager


if __name__ == '__main__':
    from data_manager import DataManager

    manager = DataManager()

    manager.import_data('./data')
    manager.printData()
