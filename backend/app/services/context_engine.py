class ContextEngine:

def __init__(self):
self.memory={}

def store(self,conv_id,key,value):

if conv_id not in self.memory:
self.memory[conv_id]={}

self.memory[conv_id][key]=value

def retrieve(self,conv_id,key):

return self.memory.get(conv_id,{}).get(key)
