

def csv_reader(file_name):
    for row_ in open(file_name, "r"):
        yield row_


if __name__ == '__main__':
    row_count = 0

    csv_gen = csv_reader('../hadoop_concepts/input_file_to_map.txt')

    for row in csv_gen:
        print(row)
        if row != '\n':
            row_count += 1

    print(f"Row count is {row_count}")


