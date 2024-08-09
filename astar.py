from collections import deque

class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
    
    def get_neighbors(self, v):
        return self.adjac_lis[v]
    
    def h(self, n):
        H = {
            'A': 5,
            'B': 10,
            'C': 7,
            'D': 13,
            'E': 5,
            'F': 7,
            'G': 0,
            'I': 5,
            'M': 8,
            'L': 3,
            'H': 3,
            'K': 2
        }
        return H[n]
    
    def a_star_algorithm(self, start, stop):
        open_lst = set([start])
        close_lst = set([])
        g = {}
        g[start] = 0
        par = {}
        par[start] = start
        
        while len(open_lst) > 0:
            n = None
            for v in open_lst:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v
            
            if n == None:
                print('Path does not exist!')
                return None
            
            if n == stop:
                reconst_path = []
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
                reconst_path.append(start)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path
            
            for (m, weight) in self.get_neighbors(n):
                if m not in open_lst and m not in close_lst:
                    open_lst.add(m)
                    par[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        par[m] = n
                        if m in close_lst:
                            close_lst.remove(m)
                            open_lst.add(m)
            
            open_lst.remove(n)
            close_lst.add(n)
        
        print('Path does not exist')
        return None

adjac_lis = {
    'A': [('B', 4), ('C', 8), ('D', 12)],
    'B': [('E', 3), ('F', 5)],
    'C': [('M', 2)],
    'D': [('L', 5)],
    'E': [('H', 6)],
    'F': [('I', 1)],
    'M': [('L', 3)],
    'I': [('F', 1), ('L', 2), ('K', 5)],
    'L': [('I', 2), ('M', 3), ('D', 5), ('G', 6)],
    'H': [('G', 2)],
    'G': [('H', 2), ('K', 1), ('L', 6)]
}

graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('A', 'G')
    
