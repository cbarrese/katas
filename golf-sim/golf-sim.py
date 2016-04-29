import random
p = [4, 3, 4, 4, 5, 3, 5, 4, 4, 5, 4, 4, 3, 4, 5, 4, 3, 4]
b = ['b', 0, 'B']
f = [{i: [0, 0] for i in range(4)} for z in range(3)]
w = None
for r in range(3):
    c = True
    a = [0, 1, 2, 3]
    m = None
    while c:
        t = [map(lambda x: random.randint(x-1, x+1), p) for i in range(4)]
        s = [sum(i) for i in t]
        g = [[l if b[l-p[i]+1] == 0 else b[l-p[i]+1] for i, l in enumerate(l)] for l in t]
        m = min(s)
        if s.count(m) == 1:
            c = False
    if w is not None:
        l = max(s)
        i = s.index(l)
        f[r][w] = [l, g[i]]
        del s[i]
        del g[i]
        a.remove(w)
    for i in range(len(a)):
        f[r][a[i]] = [s[i], g[i]]
    w = s.index(min(s))
for r in f:
    print "Round %d" % (f.index(r)+1)
    for p, q in sorted(r.iteritems(), key=lambda (x, y): y[0]):
        print "Player %d: %s - %d" % ((p+1), reduce(lambda x, y: '{} {}'.format(x, y), q[1]), q[0])
