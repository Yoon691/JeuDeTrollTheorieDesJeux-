from os import stat
import numpy as np
from pulp.constants import LpMaximize
from pulp.pulp import LpProblem
from scipy.optimize import linprog
import pulp

def gen_cle(nb_p1, nb_p2, troll_pos):
    return '{}-{}-{}'.format(nb_p1, nb_p2, troll_pos)

class Helpers:
    def __init__(self, player1, player2, init_troll):
        #self.cache = {}
        self.size = 5
        self.triplet_table = np.zeros((player1, player2))
        self.table = np.zeros((player1, player2))
        self.player1 = player1
        self.player2 = player2
        self.init_troll = -init_troll
        self.probas = []
        pass
    
    def gain(self, p1, p2, t, cache):
        if t == 2: #(self.size - 1) / 2:
            return 1
        elif t == -2: #-(self.size - 1) / 2:
            return -1
        elif p1 == p2 and t == 0:
            return 0
        elif p1 == 0:
            if p2 == t:
                return 0
            elif p2 < t:
                return 1
            else:
                return -1
        elif p2 == 0:
            if p1 + t < 0:
                return -1
            elif p1 + t == 0:
                return 0
            else:
                # print(p1, p2, t)
                return 1
        else:
            return self.PL(p1,p2,self.fill(p1,p2,t,cache))


    def fill_table(self, cache):
        # print('fill_table')
        self.troll_positions()
        #print('self.triplet_table : ', self.triplet_table)
        for i in range(self.player1):
            for j in range(self.player2):
                t = self.triplet_table[i, j]
                #print('le t de for : ', t)
                cle = gen_cle(i, j, t)
                if not cle in cache.keys():
                    self.table[i][j] = self.gain(i, j, t, cache)
                    cache[cle] = self.table[i][j]
                self.table[i][j] = cache[cle]
                #print('self.table[i][j]', i, j,' : ', self.table[i][j])
                pass
        #print('self.table : ', self.table)
        pass

    def troll_positions(self):
        for i in range(self.player1 ):
            for j in range(self.player2 ):
                if self.player1 - i == self.player2 - j:
                    # print("=",self.player1 - i , self.player2 - j , self.init_troll)
                    self.triplet_table[i, j] = self.init_troll
                elif self.player1 - i > self.player2 - j:
                    self.triplet_table[i, j] = self.init_troll + 1
                    # print("+",self.player1 - i, self.player2 - j, self.init_troll +1)
                else:
                    self.triplet_table[i, j] = self.init_troll - 1
                    # print("-",self.player1 - i, self.player2 - j, self.init_troll -1)
        # print("troll",self.triplet_table)

    def fill(self,p1,p2,t, cache):
        tab = np.zeros((p1, p2))
        trip_tab = self.trolll(p1,p2,t)
        # print(self.triplet_table)
        for i in range(p1):
            for j in range(p2):
                t = trip_tab[i, j]
                cle = gen_cle(i, j, t)
                if not cle in cache.keys():
                    tab[i][j] = self.gain(i, j, t, cache)
                    cache[cle] = tab[i][j]
                tab[i][j] = cache[cle]
               # tab[i][j] = self.gain(i, j, t)
        return tab

    def trolll(self,p1,p2,t):
        trip_tab = np.zeros((p1, p2))
        for i in range(p1):
            for j in range(p2):
                if p1 - i == p2 - j:
                    trip_tab[i, j] = t
                elif p1 - i > p2 - j:
                    trip_tab[i, j] = t + 1
                else:
                    trip_tab[i, j] = t - 1
        # print(trip_tab)
        return trip_tab

    def eliminate_dominated_strategy(self, p1, p2, matr):
        strateg = np.arange(len(matr),0,-1)
        # print(strateg)
        sub_table = matr
        # sub_table = np.array(self.table[:p1, :p2])
        while True:
            change1 = False
            change2 = False
            
            for i in range(len(sub_table)):
                for j in range(len(sub_table)):
                    if i != j:
                        if self.compare_two_strategy_p1(
                                sub_table[i, :len(sub_table[0])],
                                sub_table[j, :len(sub_table[0])]):
                            sub_table = np.delete(sub_table, j, 0)
                            strateg = np.delete(strateg,j)
                            change1 = True
                            break
                if change1:
                    break
            if change1:
                continue
            
            for i1 in range(len(sub_table[0])):
                for j1 in range(len(sub_table[0])):
                    if i1 != j1:
                        if self.compare_two_strategy_p2(
                                sub_table[:len(sub_table), i1],
                                sub_table[:len(sub_table), j1]):
                            sub_table = np.delete(sub_table, j1, 1)
                            change2 = True
                            break
                if change2:
                    break
            if not change1 and not change2:
                break
        return sub_table, strateg

    def compare_two_strategy_p1(self, A, B):
        return (A >= B).all()

    def compare_two_strategy_p2(self, A, B):
        return (A <= B).all()

    def simplex_sub(self, p1, p2, matr):
        initial = matr
        c = np.zeros(len(initial))
        c = np.append(c, [-1])
        A = initial.transpose()
        A = np.insert(A, len(A[0]) , 1, axis=1)
        constrainte_count = len(A) 
        b = np.zeros(constrainte_count)
        A_eq = np.ones((1,len(initial)))
        A_eq = np.insert(A_eq, len(A_eq[0]) , 0, axis=1)
        b_eq = [1]
        t_bounds = (None, None)
        var_bounds = (0, None)
        bounds = []
        for i in range(len(initial)):
            bounds.append(var_bounds)
        bounds.append(t_bounds)
        res = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
        print('res simplex_sub : ', res)
        return round(res.fun,2)
    
    def PL(self,p1,p2,matr):
        initial, strat = self.eliminate_dominated_strategy(p1, p2, matr)
        A = initial.transpose()
        my_lp_problem = pulp.LpProblem("MyLPProblem", pulp.LpMaximize)
        #my_lp_problem.solve(pulp.PULP_CBC_CMD(msg=0))
        char = 97
        variables = []
        for i in range(len(initial)):
            variables.append(pulp.LpVariable(chr(char), lowBound=0, cat='Continuous'))
            char += 1
        variables.append(pulp.LpVariable('x4', lowBound=-10000, cat='Continuous'))
        my_lp_problem += variables[-1], "Z"
        # Constraints
        for row in A:
            constraint = None
            for i in range(len(row)):
                constraint += row[i] * variables[i]
            constraint += - variables[-1]
            my_lp_problem += constraint >= 0

        constraint = None
        for var in variables[:len(variables) - 1]:
            constraint += var
        my_lp_problem += constraint == 1
        # print(my_lp_problem)
        my_lp_problem.solve(pulp.PULP_CBC_CMD(msg=0))
     
        return pulp.value(my_lp_problem.objective)
        
    def PL_final(self,p1,p2,matr):
        #print('matr PL_Final : ', matr)
        initial, strat = self.eliminate_dominated_strategy(p1, p2, matr)
        #print('initial Pl_final : ', initial)
        A = initial.transpose()
        my_lp_problem = pulp.LpProblem("MyLPProblem", pulp.LpMaximize)
        char = 97
        variables = []
        for i in range(len(initial)):
            variables.append(pulp.LpVariable(chr(char), lowBound=0, cat='Continuous'))
            char += 1
        variables.append(pulp.LpVariable('x4', lowBound=-10000, cat='Continuous'))
        my_lp_problem += variables[-1], "Z"
        # Constraints
        for row in A:
            constraint = None
            for i in range(len(row)):
                constraint += row[i] * variables[i]
            constraint += - variables[-1]
            my_lp_problem += constraint >= 0

        constraint = None
        for var in variables[:len(variables) - 1]:
            constraint += var
        my_lp_problem += constraint == 1
       
        my_lp_problem.solve(pulp.PULP_CBC_CMD(msg=0))
        for variable in my_lp_problem.variables()[:len(initial)]:
           self.probas.append(variable.varValue)
        
        return self.probas, strat
