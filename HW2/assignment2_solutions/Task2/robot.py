import sys
import numpy as np
def read_file(filename):
    try:
        with open(filename) as file:
            contents = file.readlines()
            return contents
    except:
        print("File read failed.")


def ParseRobotAndVacuumContent(contents):
    grid_number = int(contents[0].strip())
    robot_movement_matrix = []
    for line in contents[1:grid_number + 1]:
        position = list(line.strip())
        robot_movement_matrix.append(position)
    vacuum_cycle_length = int(contents[grid_number + 1].strip())
    vacuum_cycle_positions = []

    for line in contents[grid_number + 2 : grid_number + 2 + vacuum_cycle_length]:
        position = list(map(int, line.strip().split()))
        vacuum_cycle_positions.append(position)

    return grid_number, robot_movement_matrix, vacuum_cycle_length, vacuum_cycle_positions


def makeRobotMove(room, direction, robot_position):
    room[robot_position[0]][robot_position[1]] = 0
    if (direction == '<'):
        robot_position[0] += 0
        robot_position[1] -= 1

    if (direction == '>'):
        robot_position[0] += 0
        robot_position[1] += 1

    if (direction == 'v'):
        robot_position[0] += 1
        robot_position[1] += 0

    if (direction == '^'):
        robot_position[0] -= 1
        robot_position[1] += 0

def CollapseCalculator(grid_number, robot_movement_matrix, vacuum_cycle_length, vacuum_cycle_positions):
    robot_position = [0, 0]
    room = [[0 for i in range(grid_number)] for j in range(grid_number)]
    direction = robot_movement_matrix[robot_position[0]][robot_position[1]]
    timestep = 0
    dust_position = MakeDustMove(room, timestep, vacuum_cycle_length, vacuum_cycle_positions, None)
    visited = {}
    dust_position_in_cycle_start = None
    visited[tuple(robot_position)] = True
    cycleCount = 0
    room[robot_position[0]][robot_position[1]] = 1
    timestep += 1
    cycle_detected = False


    while cycle_detected == False:
        PrintRoomWithTimestep(room, timestep)
        direction = robot_movement_matrix[robot_position[0]][robot_position[1]]
        makeRobotMove(room, direction, robot_position)

        dust_position = MakeDustMove(room,timestep, vacuum_cycle_length, vacuum_cycle_positions, dust_position)
        if robot_position == list(dust_position):
            print("Robot and Dust collapsed" , timestep)
            break

        if tuple(robot_position) in visited and cycleCount < 3:
            if (dust_position_in_cycle_start == dust_position):
                print("Never")
                break
            dust_position_in_cycle_start = dust_position
            visited = {}
            cycleCount += 1

        visited[tuple(robot_position)] = True

        if robot_position == [0, 0] and timestep % vacuum_cycle_length == 0 :
            print("Never")
            break


        room[robot_position[0]][robot_position[1]] = 1
        timestep += 1
        if timestep > 16:
            print("Stopping.")
            break


def MakeDustMove(room, timestep, vacuum_cycle_length, vacuum_cycle_positions, previous_dust_position):
    dust_position = vacuum_cycle_positions[timestep % vacuum_cycle_length]

    if previous_dust_position is not None:
        room[previous_dust_position[0]][previous_dust_position[1]] = 0

    room[dust_position[0]][dust_position[1]] = -2

    return dust_position


def PrintRoomWithTimestep(room, timestep):
    print("timestep:", timestep)
    for i in room:
        print (str(i))



def main():
    filename = sys.argv[1]
    contents = read_file(filename)
    grid_number, robot_movement_matrix, vacuum_cycle_length, vacuum_cycle_positions = ParseRobotAndVacuumContent(contents)
    #print(grid_number, robot_movement_matrix,vacuum_cycle_length, vacuum_cycle_positions)
    return CollapseCalculator(grid_number, robot_movement_matrix, vacuum_cycle_length, vacuum_cycle_positions)

if __name__ == "__main__":
    main()