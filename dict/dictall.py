Dict = {1: 'madhav', 2: 'narayan', 3: 'khullar'} 
print(Dict)
Dict = dict([(1, 'madhav'), (2, 'ragahv')]) 
print(Dict)
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print(Dict) 
Dict['Value_set'] = 2, 3, 4
print(Dict) 
Dict[2] = 'Welcome'
print(Dict) 
print(Dict[1])
del Dict[1]  
print(Dict)
pop_ele = Dict.popitem()
print(Dict) 
Dict.clear()
print(Dict)