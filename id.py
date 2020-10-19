import json

def unique_id():
    check_id_file = open('angajati.json', 'r')
    dict_from_json = json.load(check_id_file)
    check_id_file.close()

    calculate_key = []

    for i in dict_from_json:
        calculate_key.append(i)
    calculate_key.sort()
    try:
        id = int(calculate_key[-1]) + 1
    except:
        id = 1
    return id