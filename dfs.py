def dfs(graph, start, goal, visualize=False, save_path=None):
    explored = []
    stack = [[start]]
    
    if start == goal:
        result = [start]
        if visualize:
            from visualizer import visualize_graph
            visualize_graph(
                graph,
                result,
                explored,
                title="Depth-first search",
                save_path=save_path,
            )
        return result
        
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node not in explored:
            neighbours = graph.get(node, [])
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                stack.append(new_path)
                
                if neighbour == goal:
                    if visualize:
                        from visualizer import visualize_graph
                        visualize_graph(
                            graph,
                            new_path,
                            explored,
                            title="Depth-first search",
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
            title="Depth-first search",
            save_path=save_path,
        )
    return None
