import pulp
'''
MAX Z = 0x1 + 0x2 + 0x3 + x4
subject to
-x1 - x4 >= 0
-x3 - x4 >= 0
x1 + x2 + x3 = 1
and x1,x2,x3 >= 0 and x4 unrestricted in sign
'''
my_lp_problem = pulp.LpProblem("MyLPProblem", pulp.LpMaximize)
x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')
x3 = pulp.LpVariable('x3', lowBound=0, cat='Continuous')
x4 = pulp.LpVariable('x4', lowBound=-10000, cat='Continuous')
my_lp_problem += x4, "Z"
# Constraints
my_lp_problem += -x1 - x4 >= 0
my_lp_problem += -x3 - x4 >= 0
my_lp_problem += x1 + x2 + x3 == 1
# print(my_lp_problem)
my_lp_problem.solve()
print(pulp.value(my_lp_problem.objective))
for variable in my_lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))
