class graf:
    def __init__(self,final_states,initial_state,d=None):
        if d is None:
            self.delta=dict()
            self.initial_state=initial_state
            self.final_states=final_states
        else:
            self.delta=d
            self.initial_state=initial_state
            self.final_states=final_states
    def closure(self,node:str,l=None):
        if l is None:
            l=set([node])
            if self.delta.get(node):
                if self.delta[node].get("#"):
                    for s in self.delta[node]["#"]:
                        self.closure(self,s,l)
                    return l
                else:
                    return l
            else:
                return l
        else:
            if node not in l:
                if self.delta.get(node) is not None:
                    if self.delta[node].get('#') is not None:
                        l|=set(node)
                        for s in self.delta[node]['#']:
                            self.closure(self,s,l)
                    else:
                        l|=set(node)
                else:
                    l|=set(node)
    def __str__(self):
        return str(self.delta)
    def add(self,s,simbol,new):
        if self.delta.get(s) is not None:
            if self.delta[s].get(simbol) is not None:
                if new not in self.delta[s][simbol]:
                    self.delta[s][simbol].append(new)
            
            else:
                self.delta[s][simbol]=[new]
        else:
            self.delta[s]={simbol:[new]}


                

