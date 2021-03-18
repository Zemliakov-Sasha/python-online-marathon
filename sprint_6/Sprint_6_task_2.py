import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def parse_user(output_file, *input_files):
    res = []
    names = []
    for file in input_files:
        try:
            myFile = open(str(file), mode="r", encoding="utf_8")
            list = json.load(myFile)
            for person_data in list:
                keys = person_data.keys()
                val = "name" if "name" in keys else "Name"

                if person_data[val] not in names:
                    res.append(person_data)
                    names.append(person_data[val])
            myFile.close()
        except FileNotFoundError:
            print(f"root - ERROR - File {file} doesn't exists")
    # print(res)
    result = open(output_file, mode="w", encoding="utf_8")

    json.dump(res, result)




parse_user("Sprint_6_task_2_res.json","Sprint_6_task_1.json", "Sprint_6_task_2.json", "Sprint_6_task_8.json", "Sprint_6_task_8.json")

