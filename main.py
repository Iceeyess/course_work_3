from classes.classes import Check
from classes.functions import get_json_file


# gets json file to variable data
data = get_json_file()
# Gets list of instances for class Check
checks_list = [Check(check_file.get('id'), check_file.get('state'), check_file.get('date'),
                     check_file.get('operationAmount'), check_file.get('description'), check_file.get('from'),
                     check_file.get('to')) for check_file in data if check_file]
# Sorting by date.
checks_list.sort(key=lambda a: a.date, reverse=True)
