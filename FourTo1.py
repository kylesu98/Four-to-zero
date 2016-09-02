"""GamesCrafters Homework assgnment one: Four to Zero"""

def primitive(state):
    if state==0:
        return 'L'
    return "U"
def init_pos():
    return 4
def do_move(action, state):
    if action==1:
        return state-1
    return state-2
def gen_moves(state):
    if state==1 :
        return [1]
    return [1,2]

def evaluate(state):
    if primitive(state)!= 'U':
        return primitive(state)
    moves=gen_moves(state)
    children_evaluations = []
    for move in moves:
        newstate= do_move(move, state)
        children_evaluations.append(evaluate(newstate)) 
    if 'L' in children_evaluations :
        return "W"
    return "L" 

def solve():
    initial_pos = init_pos()
    return evaluate(initial_pos)

print(solve())
