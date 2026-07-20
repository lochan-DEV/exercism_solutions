"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    x,y=record
    return y

def convert_coordinate(coordinate):
    return coordinate[0],coordinate[1]


def compare_records(azara_record, rui_record):
    azara_record=convert_coordinate(azara_record[1])
    if azara_record==rui_record[1]:
        return True
    else:
        return False


def create_record(azara_record, rui_record):
    x=compare_records(azara_record, rui_record)
    if x is True:
        return azara_record+rui_record
    else:
        return "not a match"

def clean_up(combined_record_group):
    report = ""
    for record in combined_record_group:
        new_record = (record[0],record[2],record[3],record[4])
        report += str(new_record) + "\n"
    return report
   