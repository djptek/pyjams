from interval import Head, Chorus, Interval
from instrument import Instrument


class Arrangement:
    def __init__(self, title, heads, choruses, band):
        self.title = title
        self.heads = heads
        self.choruses = choruses
        self.band = band
        self.intervals = []

    def __generate__(self):
        print('{}\n'.format(self.title))
        # add heads
        print('Play {} x Head,'.format(self.heads))
        for head in range(self.heads):
            self.intervals.append(Head(head + 1, self.band))

        # add choruses for cats
        for cat in self.band:
            print('{} {} x Chorus,'.format(cat, self.choruses))
            for chorus in range(self.choruses):
                self.intervals.append(Chorus(
                    cat, self.band[cat], \
                    chorus + 1, \
                    {e:self.band[e] for e in self.band if e != cat}))

        # add closing head
        print('Play 1 x Head\n'.format(self.heads))
        self.intervals.append(Head(1, self.band))
        # add closing tacit while buffer catches up
        self.intervals.append(Interval(1))

        print('{:<4} {:<35} || {:<4} {:<35}'.format(
            '+++ Interval 1 +++\nPLAY', self.intervals[0].__roles__(), 'HEAR', 'nothing, buffering...'))
        for i in range(1, self.intervals.__len__()):
            print('+++ Interval {} +++\n{:<4} {:<35} || {:<4} {:<35}'.format(
                i + 1, 'PLAY', self.intervals[i].__roles__(), 'HEAR', self.intervals[i - 1].__roles__()))
