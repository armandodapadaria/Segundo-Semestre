diamantes = 0
lefthalf = 0
righthalf = 0
n = input("DIGITE OS DIAMANTES: ")
for i in range(len(n)):
  if n[i]=='<':
    lefthalf+=1
  if n[i]=='>':
    righthalf+=1
if lefthalf>righthalf:
    x = lefthalf
    y = righthalf
else:
    y = lefthalf
    x = righthalf
diamantes = y
print(diamantes)