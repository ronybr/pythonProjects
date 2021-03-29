import csv
def solution(S):
    # write your code in Python 3.6
    new_dt = list()
    with open(S, "r") as file:
        file1 = csv.reader(file, delimiter=",")
        #lines = file.readlines()
        for i in file1:
            new_dt.append(i)
            for x in i:
                if x == "NULL":
                    new_dt.remove(i)
        return new_dt

def solution2(S):
    with open(S, "r") as file:
        var = list(map(lambda x: x.remove(x) if x == "NULL" else x, file))
    return var


file = "test-input.txt"
print(solution2(file))

