
def isInCycle(match_scores,donor_friends,query):
    return False

def take_input():
    n = int(input())
    m = int(input())
    donor_friends = input().split(',')
    for i in range(len(donor_friends)):
        donor_friends[i] = int(donor_friends[i])
    match_scores = []
    for i in range(m):
        match_row = input().split(',')
        for j in range(len(match_row)):
            match_row[j] = int(match_row[j])
        match_scores.append(match_row)
    query = int(input())
    print(isInCycle(match_scores,donor_friends,query))

take_input()
