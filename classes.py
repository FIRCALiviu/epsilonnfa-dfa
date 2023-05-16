import queue
import graphviz
class graf:
    def __init__(self,initial_state,final_states,states,d=None):
        if d is None:
            self.delta=dict()
            self.initial_state=initial_state
            self.final_states=final_states
            self.states=states
        else:
            self.delta=d
            self.initial_state=initial_state
            self.final_states=final_states
            self.states=states
    def closure(self,node:str,l=None):
        if l is None:
            l=set([node])
            if self.delta.get(node):
                if self.delta[node].get("#"):
                    for s in self.delta[node]["#"]:
                        self.closure(s,l)
                    return l
                else:
                    return l
            else:
                return l
        else:
            if node not in l:
                if self.delta.get(node) is not None:
                    if self.delta[node].get('#') is not None:
                        l|=set([node])
                        for s in self.delta[node]['#']:
                            self.closure(s,l)
                    else:
                        l|=set([node])
                else:
                    l|=set([node])
    
    def super_pos(self,states,letter):
        res=set()
        for state in states:
            if self.delta.get(state) is not None:
                if self.delta[state].get(letter) is not None:
                    res|=set(self.delta[state][letter])
        return res
                
    def super_choose(self,state:str,letter):# letter cannot be lambda
        res=self.closure(state)
        states=self.super_pos(res,letter)
        final_res=set()
        for s in states:
            final_res|=self.closure(s)
        
        return final_res
    
    def __str__(self):
        return str(self.delta)+'\n Final states:\n'+str(self.final_states)+'\n Initial_state:\n'+str(self.initial_state)
    def add(self,s,simbol,new):
        if self.delta.get(s) is not None:
            if self.delta[s].get(simbol) is not None:
                if new not in self.delta[s][simbol]:
                    self.delta[s][simbol].append(new)
            
            else:
                self.delta[s][simbol]=[new]
        else:
            self.delta[s]={simbol:[new]}

    def get_dfa(self):
        alfabet=set()
        for state in self.delta.keys():
            for letter in self.delta[state]:
                if letter !='#':
                    alfabet|=set([letter])
        alfabet=list(alfabet)
        
        M={}
        
        for letter in alfabet:
            
            for state in self.states:
                if M.get(letter) is None:
                    M[letter]={}
                    
                    M[letter]={state:self.super_choose(state,letter)}
                    
                else:
                    
                    if M[letter].get(state) is None:
                        M[letter][state]=self.super_choose(state,letter)
                    else:
                        raise RuntimeError
        new_states=set()
        initial_state=self.closure(self.initial_state)
        new_states.add(frozenset(initial_state))
        delta=dict()
        q=queue.Queue()
        q.put(frozenset(initial_state))
        while not q.empty():
            states=q.get()
            for letter in alfabet:
                value=set()
                for state in states:
                    value|=M[letter][state]
                
                value=frozenset(value)
                if value in new_states:
                    if delta.get(states) is None:
                        delta[states]={letter:value}
                    else:
                        delta[states][letter]=value
                else:
                    new_states.add(value)
                    q.put(value)  
                    if delta.get(states) is None:
                        delta[states]={letter:value}
                    else:
                        delta[states][letter]=value   
        new_final_states=set()
        for states in new_states:
            for state in states:
                if state in self.final_states:
                    new_final_states.add(states)
                    break
        return graf(self.closure(self.initial_state),new_final_states,list(new_states),delta)


                
class visualizer:
    def __init__(self,dfa):
        self.dfa=dfa

    def show(self,DFA=None):
        visual=graphviz.Digraph()
        if DFA is None:
            for state in self.dfa.states:
                if state in self.dfa.final_states:
                    visual.attr("node",shape='doublecircle')
                    visual.node(" ".join([i for i in state]))
                else:
                    visual.attr("node",shape='circle')
                    visual.node(" ".join([i for i in state]))
            visual.attr('node',shape='none')
            visual.node("start")
            visual.edge("start"," ".join([i for i in self.dfa.initial_state]))

            for state in self.dfa.delta:
                for letter in self.dfa.delta[state]:
                    visual.edge(" ".join([i for i in state])," ".join([i for i in self.dfa.delta[state][letter]]),label=letter)
            visual.render("DFA",view=True)
        else:
            temp=self.dfa
            self.dfa=DFA
            self.show()
            self.dfa=temp
    
        
