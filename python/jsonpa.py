import json
with open("newj.json") as f:
    python_dic=json.load(f)
print(python_dic)
print(type(python_dic))
employe='{"name":"ram","age":20,"place":"calicut"}'
print(employe)
print(type(employe))
employedict=json.loads(employe)
print(employedict)
print(type(employedict))
employe=json.dumps(employedict)
print(employe)
print(type(employe))