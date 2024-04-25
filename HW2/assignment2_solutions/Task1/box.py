#For sorting the boxes corresponding to their lengths I will be using the method in the following link,
# https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list

import sys
from operator import itemgetter
def read_file(filename):
    try:
        with open(filename) as file:
            contents = file.readlines()
            return contents
    except:
        print("File read failed.")


def ParseBoxContent(contents):
    box_number = int(contents[0].strip())
    box_dimensions = []

    for line in contents[1:]:
        dimensions = list(map(float, line.split()))
        box_dimensions.append(dimensions)

    return box_number, box_dimensions


def FindMaximumNumberOfNestingBoxes(box_number, box_dimensions):
    box_dimensions.sort(key=lambda x: (x[0]))
    #print(box_dimensions)
    box_number = int(box_number)

    dp = [1] * (box_number)


    for item in range(box_number):
        for previousItem in range(item):
            if (PreviousItemFits(box_dimensions, item, previousItem)):
                dp[item] = max(dp[previousItem] + 1, dp[item])
        #print(dp)

    return max(dp)


def PreviousItemFits(box_dimensions_sorted, item, previousItem):
    lengthCheck = (box_dimensions_sorted[item][0] > box_dimensions_sorted[previousItem][0])
    widthCheck = (box_dimensions_sorted[item][1] > box_dimensions_sorted[previousItem][1])
    heightCheck = (box_dimensions_sorted[item][2] > box_dimensions_sorted[previousItem][2])

    check = (lengthCheck and widthCheck and heightCheck)
    #print("checking items, item: ", item , " " , box_dimensions_sorted[item] , "and previous item:", previousItem, " ", box_dimensions_sorted[previousItem] , "and will return:" , check)
    return check

def main():
    filename = sys.argv[1]
    contents = read_file(filename)
    box_number, box_dimensions = ParseBoxContent(contents)

    #print("Box number: " + str(box_number))
    #print("Box dimensions: " + str(box_dimensions))

    maxNumberOfNestedBoxes = FindMaximumNumberOfNestingBoxes(box_number,box_dimensions)
    print(maxNumberOfNestedBoxes)

if __name__ == "__main__":
    main()