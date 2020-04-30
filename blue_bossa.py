from interval import Head, Chorus, Interval
from instrument import Instrument

Heads = 2
Choruses_per_instrument = 4
intervals = []
# add heads
for head in range(Heads):
    intervals.append(Head(head+1))

# add choruses for cats
for instrument in list(Instrument):
    for chorus in range(Choruses_per_instrument):
        intervals.append(Chorus(instrument, chorus+1))

# add closing head
intervals.append(Head(1))
# add closing tacit while buffer catches up
intervals.append(Interval(1))

print('{:<4} {:<40} || {:<4} {:<40}'.format(
    'PLAY', intervals[0].__roles__(), 'HEAR', 'nothing, buffering...'))
for i in range(1, intervals.__len__()):
    print('{:<4} {:<40} || {:<4} {:<40}'.format(
        'PLAY', intervals[i].__roles__(), 'HEAR', intervals[i-1].__roles__()))

