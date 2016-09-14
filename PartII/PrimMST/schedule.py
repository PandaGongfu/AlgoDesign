from operator import itemgetter

fh = open('jobs.txt', 'r')
lines = fh.read().split('\n')

njobs = int(lines[0])
jobs = []
for k, l in enumerate(lines[1:-1]):
    jw = l.split(' ')
    jobs.append({'weight': int(jw[0]), 'length': int(jw[1]), 'diff': int(jw[0]) - int(jw[1])})
    # jobs.append({'weight': int(jw[0]), 'length': int(jw[1]), 'diff': float(int(jw[0]) / int(jw[1]))})

sorted_jobs = sorted(jobs, key=itemgetter('diff', 'weight'), reverse=True)

length = sorted_jobs[0]['length']
running_sum = sorted_jobs[0]['length'] * sorted_jobs[0]['weight']
for job in sorted_jobs[1:]:
    length += job['length']
    running_sum += length * job['weight']
