def file_reader():
    with open('input_file_to_map.txt') as f:
        d = f.readlines()
    return d


def mapper_code():
    total_words = 0
    list_final = []

    for i_each in json_record:
        list_form = json_record[i_each].split()
        for i_ in list_form:
            total_words += 1
            key = 1
            value_ = i_
            record = {value_: key}
            list_final.append(record)

    return list_final


def reducer_code(records):
    for i_each in records:
        for key, value_ in i_each.items():
            try:
                final_json[key] = final_json[key] + 1
            except Exception as e:
                final_json[key] = 1

    return final_json


def write_output(json_records):
    import json
    dumped = json.dumps(json_records, indent=4, sort_keys=True, ensure_ascii=False)
    with open('output.json', 'w') as f_:
        f_.write(dumped)


if __name__ == '__main__':
    cnt = 0
    json_record = {}
    data = file_reader()
    for i in data:
        cnt += 1
        value = i.replace('\n', '').strip()
        json_record.update({cnt: value})
    print(json_record)
    final_json = {}
    list_records = mapper_code()
    json_record_final = reducer_code(list_records)
    write_output(json_record_final)
