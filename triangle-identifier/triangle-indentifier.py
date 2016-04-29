i = input("Triangle sides (comma separated):")
p = ['Equilateral', 'Isosceles', 'Scalene']
a = map(float, i)
print p[len(set(map(lambda x: x/min(a), a)))-1]
