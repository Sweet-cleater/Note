a = [ ['Py','PyA'],['Py','PyB'],['Py','PyC'],['Pe','PeA'],['Pe','PeC'] ]
t = {}
for n in a:
    if n[0] in t: t[n[0]].append(n[1])
    else: t[n[0]] = [n[1]]

print(t)