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

    def get_dfa(self):
        alfabet=set()
        for state in self.delta.keys():
            for letter in self.delta[state]:
                if letter !='#':
                    alfabet|=set([letter])
        alfabet=list(alfabet)
        
        M=[]
        for state in self.states:
            M.append([None]*len(alfabet))
        for i,state in enumerate(self.states):
            for j,value in enumerate(alfabet):
                M[i][j]=self.super_choose(state,value),state,value
        for line in M:
            print(*line)

                

