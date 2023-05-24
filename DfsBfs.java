package Final;
import java.util.*;

public class DfsBfs {
    private static List<LinkedList<Integer>> adjacencyList;

    public static void addEdge(int source, int destination) {
        adjacencyList.get(source).add(destination);
        adjacencyList.get(destination).add(source);
    }

    public static void DFS(int vertex, Set<Integer> visited) {
        visited.add(vertex);
        System.out.print(vertex + " ");
        for (int adjacentVertex : adjacencyList.get(vertex)) {
            if (!visited.contains(adjacentVertex)) {
                DFS(adjacentVertex, visited);
            }
        }
    }

    public static void BFS(Queue<Integer> queue, Set<Integer> visited) {
        if (queue.isEmpty()) {
            return;
        }
        int vertex = queue.poll();
        visited.add(vertex);
        System.out.print(vertex + " ");
        for (int adjacentVertex : adjacencyList.get(vertex)) {
            if (!visited.contains(adjacentVertex)) {
                visited.add(adjacentVertex);
                queue.add(adjacentVertex);
            }
        }
        BFS(queue, visited);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of vertices in the graph: ");
        int vertices = scanner.nextInt();
        adjacencyList = new ArrayList<>(vertices);
        for (int i = 0; i < vertices; i++) {
            adjacencyList.add(new LinkedList<>());
        }

        System.out.print("Enter the number of edges in the graph: ");
        int edges = scanner.nextInt();
        System.out.println("Enter the source and destination vertices of each edge (separated by a space):");
        for (int i = 0; i < edges; i++) {
            int source = scanner.nextInt();
            int destination = scanner.nextInt();
            addEdge(source, destination);
        }

        System.out.println("Enter the starting vertex for DFS: ");
        int startVertexDFS = scanner.nextInt();
        System.out.println("DFS starting from vertex " + startVertexDFS + ":");
        Set<Integer> visitedDFS = new HashSet<>();
        DFS(startVertexDFS, visitedDFS);
        System.out.println();

        System.out.println("Enter the starting vertex for BFS: ");
        int startVertexBFS = scanner.nextInt();
        System.out.println("BFS starting from vertex " + startVertexBFS + ":");
        Set<Integer> visitedBFS = new HashSet<>();
        Queue<Integer> queueBFS = new LinkedList<>();
        visitedBFS.add(startVertexBFS);
        queueBFS.add(startVertexBFS);
        BFS(queueBFS, visitedBFS);
        System.out.println();

        scanner.close();
    }
}
