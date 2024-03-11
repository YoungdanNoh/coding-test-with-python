# BFS는 간선의 비용이 모두 동일한 상황에서 최단거리 문제를 해결하기 위한 목적으로도 사용될 수 있다.

from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        # 해당 원소와 연결되어 있고 아직 방문하지 않은 원소라면 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
