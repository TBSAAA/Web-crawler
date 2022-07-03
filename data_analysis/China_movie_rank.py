import csv
from itertools import islice


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def top_20_rank():
    top_list = []
    lowest = 0
    with open("data/China_move_rank.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in islice(reader, 1, None):
            # If there is no box office data, skip the movie.
            if not is_number(row[3]):
                continue
            if len(top_list) < 20:
                top_list.append(row)
                lowest = min(top_list, key=lambda x: float(x[3]))
            else:
                if float(row[3]) > float(lowest[3]):
                    top_list.append(row)
                    top_list.remove(lowest)
                    lowest = min(top_list, key=lambda x: float(x[3]))
                else:
                    continue
    top_list.sort(key=lambda x: float(x[3]), reverse=True)
    for i in top_list:
        print(i)

def bottom_20_rank():
    bottom_list = []
    highest = 0
    with open("data/China_move_rank.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in islice(reader, 1, None):
            # If there is no box office data, skip the movie.
            if not is_number(row[3]):
                continue
            if len(bottom_list) < 20:
                bottom_list.append(row)
                highest = max(bottom_list, key=lambda x: float(x[3]))
            else:
                if float(row[3]) < float(highest[3]):
                    bottom_list.append(row)
                    bottom_list.remove(highest)
                    highest = max(bottom_list, key=lambda x: float(x[3]))
                else:
                    continue
    bottom_list.sort(key=lambda x: float(x[3]), reverse=False)
    for i in bottom_list:
        print(i)


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
