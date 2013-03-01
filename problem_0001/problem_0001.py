print 'Project Euler Problem 0001'

start = 0
stop = 1000

total = sum(list(set(range(start, stop, 5) + range(start, stop, 3))))

print 'Sum is %s' % total