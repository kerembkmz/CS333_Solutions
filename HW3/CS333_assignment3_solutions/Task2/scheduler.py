import sys


def read_file(filename):
    try:
        with open(filename) as file:
            contents = file.readlines()
            return contents
    except:
        print("File read failed.")


def ParseContentIntoShiftsAndWorkers(contents):
    blend_shift_worker_num = int(contents[0].split()[1])
    blend_times_needed_to_complete = list(map(int, contents[1].split()))

    cook_shift_worker_num = int(contents[2].split()[1])
    cook_times_needed_to_complete = list(map(int, contents[3].split()))

    strain_shift_worker_num = int(contents[4].split()[1])
    strain_times_needed_to_complete = list(map(int, contents[5].split()))

    finish_shift_worker_num = int(contents[6].split()[1])
    finish_times_needed_to_complete = list(map(int, contents[7].split()))

    num_employees = int(contents[8].split()[1])
    employees = []

    for i in range(num_employees):
        employee_stations = contents[9 + i * 2].split()
        employee_available_times = list(map(int, contents[10 + i * 2].split()))

        employees.append((employee_stations, employee_available_times))

    return blend_shift_worker_num, blend_times_needed_to_complete, cook_shift_worker_num, cook_times_needed_to_complete, strain_shift_worker_num, strain_times_needed_to_complete, finish_shift_worker_num, finish_times_needed_to_complete, num_employees, employees

def construct_network_flow(b_req_worker, b_times, c_req_worker, c_times, s_req_worker, s_times, f_req_worker, f_times,
                           num_employees, employees):
    graph = {'S': {}}
    graph['T'] = {}

    station_time_mapping = {'b': b_times, 'c': c_times, 's': s_times, 'f': f_times}
    station_name_mapping = {'b': 'blend', 'c': 'cook', 's': 'strain', 'f': 'finish'}

    for employee_no, (skill, times) in enumerate(employees): # Creating employee layer and adding edges with S node
        emp_node = 'emp'+str(employee_no)
        graph['S'][emp_node] = len(times)
        graph[emp_node] = {}

        for workable, available_time_slot in enumerate(times): # Creating time layer with edges to employee layer and setting all edges to 1
            time_node = emp_node + "time" + str(workable)
            graph[emp_node][time_node] = 1
            graph[time_node] = {}

            for station_name in station_name_mapping.keys():
                for required_time in range(len(station_time_mapping[station_name])):
                    job_node = station_name + str(required_time)
                    if (job_node not in graph):
                        graph[job_node] = {}
                    if (time_node not in graph[job_node]):
                        graph[job_node][time_node] = 0
                    if (station_name_mapping[station_name] in skill):
                        graph[time_node][job_node] = 1

    for station_name, required_worker, times in [('b', b_req_worker, b_times), ('c', c_req_worker, c_times),('s', s_req_worker, s_times), ('f', f_req_worker, f_times)]:
        for i in range(len(times)):
            job_node = station_name + str(i)
            graph[job_node]['T'] = required_worker

    return graph

# bfs and ford-fulkerson algorithm implementation link: https://github.com/Mushahid2521/Data-Structures-and-Algorithms-in-Python/blob/master/graph/Maximul_flow_Ford_Fulkerson.py
def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = []
    visited[source] = True
    queue.append(source)

    while queue:
        node = queue.pop(0)

        for id, val in enumerate(graph[node]):
            if visited[id] == False and val > 0:
                visited[id] = True
                queue.append(id)
                parent[id] = node
                if id == sink:
                    return True

    return False


def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while (s != source):
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while (v != source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow

def main():
    filename = sys.argv[1]
    contents = read_file(filename)

    b_req_worker, b_times, c_req_worker, c_times, s_req_worker, s_times, f_req_worker, f_times, num_employees, employees = ParseContentIntoShiftsAndWorkers(
        contents)

    graph = construct_network_flow(b_req_worker, b_times, c_req_worker, c_times, s_req_worker, s_times, f_req_worker, f_times,
                         num_employees, employees)

    nodes = list(graph.keys())
    int_graph = [[0] * len(nodes) for _ in nodes]

    for node in nodes:
        node_index = nodes.index(node)
        for edge, capacity in graph[node].items():
            edge_index = nodes.index(edge)
            int_graph[node_index][edge_index] = capacity

    max_flow = ford_fulkerson(int_graph, nodes.index('S'), nodes.index('T'))
    #print('Maximum flow:', max_flow)

    max_flow_equality_condition = int(b_req_worker) * len(b_times) + int(c_req_worker) * len(c_times) + int(s_req_worker) * len(s_times) + int(f_req_worker) * len(f_times)
    print(max_flow == max_flow_equality_condition)


if __name__ == "__main__":
    main()
