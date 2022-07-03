import csv
from itertools import islice


# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False

# def int_to_money(str):
#     str_list = list(str)
#     final_list = []
#     length = len(str_list)
#     for i in range(1, length+1):
#         final_list.append(str_list.pop(-1))
#         if i % 3 == 0:
#             final_list.append(",")
#         if i == length:
#             final_list.append("$")
#     final_list.reverse()
#     print("".join(final_list))


def top_20_rank():
    top_list = []
    lowest = 0
    with open("data/worldwide_movie_rank.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in islice(reader, 1, None):
            row[2] = row[2].replace(",", "").replace("$", "")
            if len(top_list) < 20:
                top_list.append(row)
                lowest = min(top_list, key=lambda x: int(x[2]))
            else:
                if int(row[2]) > int(lowest[2]):
                    top_list.append(row)
                    top_list.remove(lowest)
                    lowest = min(top_list, key=lambda x: int(x[2]))
                else:
                    continue
    top_list.sort(key=lambda x: int(x[2]), reverse=True)
    for i in top_list:
        print(i[1], "${:,}".format(int(i[2])), i[0])


def bottom_20_rank():
    bottom_list = []
    highest = 0
    with open("data/worldwide_movie_rank.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in islice(reader, 1, None):
            row[2] = row[2].replace(",", "").replace("$", "")
            if len(bottom_list) < 20:
                bottom_list.append(row)
                highest = max(bottom_list, key=lambda x: int(x[2]))
            else:
                if int(row[2]) < int(highest[2]):
                    bottom_list.append(row)
                    bottom_list.remove(highest)
                    highest = max(bottom_list, key=lambda x: int(x[2]))
                else:
                    continue
    bottom_list.sort(key=lambda x: int(x[2]), reverse=False)
    for i in bottom_list:
        print(i[1], "${:,}".format(int(i[2])), i[0])



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
