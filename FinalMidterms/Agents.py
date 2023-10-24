from Problems import *
from Algorithms import *
import math
import random

class NQueenBFSAgent(BFS):

    def __init__(self,n=8):
        self.board = NQueenProblem(n=n)
        super().__init__(initial_state=self.board.placement,goal_state=None)
            
    def getAdjacents(self,node):
        temp = []
        temp = NQueenProblem.getAdjacents(node.name)
        return temp
    
    def checkGoal(self,node):
        if None not in node.name:
            return True



class NQueenDFSAgent(DFS):

    def __init__(self,n=8):
        self.board = NQueenProblem(n=n)
        super().__init__(initial_state=self.board.placement,goal_state=None)
            
    def getAdjacents(self,node):
        temp = []
        temp = NQueenProblem.getAdjacents(node.name)
        return temp
    
    def checkGoal(self,node):
        if None not in node.name:
            return True
        else:
            return False





class NQueenHillClimbingAgent(HillClimbing):
    def __init__(self,n=8):
        self.board = NQueenIncrementalProblem.getPlacement(n=n)
        super().__init__(initial_state=self.board,goal_state=None)
            
    def getAdjacents(self,node):
        temp = []
        temp = NQueenIncrementalProblem.getAdjacents(node.name)
        return temp
    
    def getValue(self,placement):
        return NQueenIncrementalProblem.errorCheck(placement)



class NQueenRRHillClimbingAgent(RRHillClimbing):
    def __init__(self,n=8,steps=1):
        self.n = n
        self.board = NQueenIncrementalProblem.getPlacement(n=self.n)
        super().__init__(steps=steps)
            
    def getAdjacents(self,node):
        temp = []
        temp = NQueenIncrementalProblem.getAdjacents(node.name)
        return temp
    
    def getValue(self,placement):
        return NQueenIncrementalProblem.errorCheck(placement)
    
    def getInitialState(self):
        return NQueenIncrementalProblem.getPlacement(n=self.n)



class NQueenUCSAgent(UCS):

    def __init__(self,n=8):
        self.board = NQueenProblem(n=n)
        super().__init__(initial_state=self.board.placement,goal_state=None)
            
    def getAdjacents(self,node):
        temp_1 = []
        temp_2 = NQueenProblem.getAdjacents(node.name)
        for item in temp_2:
            temp_1.append([item,1])
    
    def checkGoal(self,node):
        if None not in node.name:
            return True
        else:
            return False


class NQueenAStarAgent(AStar):

    def __init__(self,n=8):
        self.board = NQueenProblem(n=n)
        super().__init__(initial_state_h_value=n,initial_state=self.board.placement,goal_state=None)
            
    def getAdjacents(self,node):
        temp_1 = []
        temp_2 = NQueenProblem.getAdjacents(node.name)
        for item in temp_2:
            temp_1.append([item,1,0])
    
    def checkGoal(self,node):
        if None not in node.name:
            return True
        else:
            return False


class NQueenDLSAgent(DLS):

    def __init__(self,n=8):
        self.board = NQueenProblem(n=n)
        super().__init__(initial_state=self.board.placement,goal_state=None)
            
    def getAdjacents(self,node):
        temp = []
        temp = NQueenProblem.getAdjacents(node.name)
        return temp
    
    def checkGoal(self,node):
        if None not in node.name:
            return True
        else:
            return False


#Map Coloring Agents

class MapColoringCSPAgent(CSP):
    
    def __init__(self,map_name,color_count=3,forward_checking=False,arc_consistency=False,mrv_heuristic=False,degree_heuristic=False,lcv_heuristic=False):
        if color_count == 3:
            domain_values = ['red','blue','green']
        elif color_count == 4:
            domain_values = ['red','blue','green','yellow']
            
        graph = MapColoringProblem.graphs[map_name]
        assignments = {}
        domains = {}
        unassigned_vars = 0
        degree_of_unassigned_vars = {}
        for key, adjacents in graph.items(): 
            domains[key] = copy.deepcopy(domain_values)
            assignments[key] = None
            degree_of_unassigned_vars[key] = len(adjacents)
            unassigned_vars += 1
        
        initial_state = CSPNode(assignments,domains,degree_of_unassigned_vars,unassigned_vars)
        super().__init__(graph,initial_state,len(domain_values),forward_checking=False,MRV_heuristic=mrv_heuristic,degree_heuristic=degree_heuristic,arc_consistency=arc_consistency,lcv_heuristic=lcv_heuristic)

class NQueenLocalBeamAgent(LocalBeamSearch):
    def __init__(self,n=8,k=1):
        temp_board = []
        for i in range(k):
            board = NQueenIncrementalProblem.getPlacement(n=n)
            temp_board.append(board)
        super().__init__(initial_states=temp_board,goal_state=None,k=k)
            
    def getAdjacents(self,node):
        temp = []
        temp = NQueenIncrementalProblem.getAdjacents(node.name)
        return temp
    
    def getValue(self,placement):
        return NQueenIncrementalProblem.errorCheck(placement)
    
    def checkGoal(self,array):
        if array[1] != 0:
            return False
        else:
            return True



class NQueenGeneticAlgorithmAgent(GenticAlgorithm):
    def __init__(self,n,population,steps=10,mutation_prob=.2):
        temp_board = []
        self.population = population
        self.n = n
        self.max_error = ((self.n) * (self.n - 1)) / 2
        
        for i in range(self.population):
            board = NQueenIncrementalProblem.getPlacement(n=n)
            temp_board.append(board)
        super().__init__(initial_chromosomes=temp_board,max_fitness=self.max_error,steps=steps,mutation_prob=mutation_prob)
            
    
    def getValue(self,placement):
        n_error = NQueenIncrementalProblem.errorCheck(placement)
        return self.max_error - n_error
    
    


class NQueenSimulatedAnnealingAgent(SimulatedAnnealing):
    def __init__(self,n=8,T=1000,coefficient=.999,threshold=.005):
        self.board = NQueenIncrementalProblem.getPlacement(n=n)
        self.n = n
        self.max_error = (n * (n - 1)) / 2
        super().__init__(initial_state=self.board,goal_state=None,T=T,coefficient=coefficient,threshold=threshold)
        
    def getAdjacents(self,node):
        temp = []
        temp = NQueenIncrementalProblem.getAdjacents(node.name)
        return temp
    
    def getValue(self,placement):
        return self.max_error - NQueenIncrementalProblem.errorCheck(placement)