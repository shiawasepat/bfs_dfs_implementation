def bfs(graph, start, goal, visualize=False, save_path=None):
    explored = []
    queue = [[start]]
    
    if start == goal:
        result = [start]
        if visualize:
            from visualizer import visualize_graph
            visualize_graph(
                graph,
                result,
                explored,
                title="Breadth-first search",
                save_path=save_path,
            )
        return result
        
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in explored:
            neighbours = graph.get(node, [])
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == goal:
                    if visualize:
                        from visualizer import visualize_graph
                        visualize_graph(
                            graph,
                            new_path,
                            explored,
                            title="Breadth-first search",
                            save_path=save_path,
                        )
                    return new_path
            explored.append(node)
    if visualize:
        from visualizer import visualize_graph
        visualize_graph(
            graph,
            None,
            explored,
            title="Breadth-first search",
            save_path=save_path,
        )
    return None
