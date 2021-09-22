### Task 4.3
# File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
# This file contains the student’s names, age and average mark.
# 1) Implement a function which receives file path and returns names of top performer students
# ```python
# def get_top_performers(file_path, number_of_top_students=5):
#     pass
#
# print(get_top_performers("students.csv"))
# >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
# ```
#
# 2) Implement a function which receives the file path with srudents info and writes CSV student information to the new file in descending order of age.
# Result:
# ```
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27
# ```
import pandas
import csv


def main():
    print(get_top_performers("../data/students.csv"))
    new_csv_sorted_by_age("../data/students.csv")


def get_top_performers(file_path, number_of_top_students=5):
    with open("../data/students.csv", "r") as file:
        read_f = pandas.read_csv(file)
        read_f = read_f.sort_values(["average mark"], ascending=False)  # сортируем от большего к меньшему
        return list(read_f["student name"][0:number_of_top_students])


def new_csv_sorted_by_age(file_path, name_of_new=""):
    with open("../data/students.csv", "r") as file:
        read_f = pandas.read_csv(file)
        read_f = read_f.sort_values(["age"], ascending=False)

    with open("../data/sorted_students.csv", mode="w", encoding="utf-8") as w_file:
        write_f = csv.writer(w_file, lineterminator="\r")
        write_f.writerow(read_f)
        for el in read_f.values:
            write_f.writerow([el[0], el[1], el[2]])


if __name__ == '__main__':
    main()
