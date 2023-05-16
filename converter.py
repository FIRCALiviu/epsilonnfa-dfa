import classes
import graphviz
filename='input.txt'
file = open(filename)

g=classes.graf(file.readline().strip(),file.readline().split(),file.readline().split())

lines=file.read().splitlines()
for line in lines:
    g.add(*line.split())


visual=graphviz.Digraph()
dfa=g.get_dfa()
for state in dfa.states:
    if state in dfa.final_states:
        visual.attr("node",shape='doublecircle')
        visual.node(" ".join([i for i in state]))
    else:
        visual.attr("node",shape='circle')
        visual.node(" ".join([i for i in state]))
visual.attr('node',shape='none')
visual.node("__starter__")
visual.edge("__starter__"," ".join([i for i in dfa.initial_state]))

for state in dfa.delta:
    for letter in dfa.delta[state]:
        visual.edge(" ".join([i for i in state])," ".join([i for i in dfa.delta[state][letter]]),label=letter)
visual.render("DFA",view=True)