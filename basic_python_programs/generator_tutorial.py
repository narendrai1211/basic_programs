

def csv_reader(file_name):
    for row_ in open(file_name, "r"):
        yield row_


if __name__ == '__main__':
    row_count = 0

    csv_gen = csv_reader('../hadoop_concepts/input_file_to_map.txt')

    for row in csv_gen:
        print(row)

    print(f"Row count is {row_count}")


