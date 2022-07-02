import csv
from itertools import islice


def top_20_rank():
    top_list = []
    lowest = 0
    with open("China_move_rank.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in islice(reader, 1, None):
            if len(top_list) < 20:
                top_list.append(row)
            else:
                lowest = min(top_list, key=lambda x: int(x[3]))
                if row[3] > lowest and row[3].isdigit():
                    top_list.append(row)
                    top_list.remove(lowest)
    # top_list.sort(key=lambda x: int(x[3]), reverse=True)

def bottom_20_rank():
    with open("China_move_rank.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
            break


if __name__ == "__main__":
    while True:
        print("************* Start *************")
        print("Please select the function you need:")
        print("1. Top 20 highest grossing movies.")
        print("2. The bottom 20 movies with the lowest grossing.")
        print("3. Exit.")
        input_num = input("Please input the number: ")
        if input_num == "1":
            top_20_rank()
        elif input_num == "2":
            bottom_20_rank()
        elif input_num == "3":
            print("Exit.")
            exit()
        else:
            print("Invalid input.")
