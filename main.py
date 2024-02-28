import os.path

from classes.classes import Check
from classes.functions import get_json_file

link = os.path.join('source', 'operations.json')
# gets json file to variable data
data = get_json_file(link)
# Gets list of instances for class Check
checks_list = [Check(check_file.get('id'), check_file.get('state'), check_file.get('date'),
                     check_file.get('operationAmount'), check_file.get('description'), check_file.get('from'),
                     check_file.get('to')) for check_file in data if check_file]
# Sorting by date.
checks_list.sort(key=lambda a: a.date, reverse=True)

# While count unequals to 5 iterations , then circle will be going on.
count, index = 5, 0
while count != index:
    if checks_list[index].state == 'EXECUTED':
        checks_list[index].print_check()
        index += 1
    else:
        count += 1
        index += 1