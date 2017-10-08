def find_lower_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node, processed

def prepare_data():
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    graph["fin"] = {}

    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity

    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None
    return graph, costs, parents

if __name__ == "__main__":
    graph, costs, parents = prepare_data()
    #print(graph, costs, parents)

    processed = []
    node, processed  = find_lower_cost_node(costs, processed)
    #print(node, processed)
    while node is not None:
        #print(type(node))
        neighbours = graph[node]
        for n in neighbours.keys():
            updated_cost = costs[node] + neighbours[n]
            if updated_cost <= costs[n]:
                costs[n] = updated_cost
                parents[n] = node
        processed.append(node)
        node, processed = find_lower_cost_node(costs, processed)
    print(parents)
