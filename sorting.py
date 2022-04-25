import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row_ind, row in enumerate(reader):
            if row_ind == 0:
                output = dict()
                for key in row:
                    output[key] = []
            for key in row:
                output[key].append(int(row[key]))


    return output

def selection_sort(nums, direction):
    for start_idx in range(len(nums)):
        smallest_num = nums[start_idx]
        smallest_idx = start_idx

        for index in range(start_idx + 1, len(nums)):
            if direction == "<":
                if nums[index] < smallest_num:
                    smallest_num = nums[index]
                    smallest_idx = index
            elif direction == ">":
                if nums[index] > smallest_num:
                    smallest_num = nums[index]
                    smallest_idx = index
        nums[start_idx], nums[smallest_idx] = nums[smallest_idx], nums[start_idx]

    return nums

def bubble_sort(nums):
    for i in range(len(nums)):
        for k in range(len(nums)-(i+1)):
            if nums[k] > nums[k+1]:
                nums[k], nums[k+1] = nums[k+1], nums[k]

    return nums

def insertion_sort(nums):
    for i in range(1, len(nums)):
        key_num = nums[i]
        j = i - 1
        while nums[j] > key_num and j >= 0:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key_num
    return nums






def main():
    nums = read_data("numbers.csv")
    print(nums["series_3"])
    print(selection_sort(nums["series_3"], ">"))
    print(bubble_sort(nums["series_1"]))
    print(insertion_sort(nums["series_3"]))

if __name__ == '__main__':
    main()
