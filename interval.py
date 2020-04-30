from instrument import Instrument
from role import Role


class Interval:

    def __init__(self, repeat):
        self.role_cats = {}
        self.repeat = repeat

    def __roles__(self):
        str_list = ''
        if self.role_cats.__len__() > 0:
            for role in self.role_cats.keys():
                str_list += '{:<5} {:<1} '.format(role.name, self.repeat)
                for instrument in self.role_cats[role]:
                    str_list += '{} '.format(instrument)
        else:
            str_list += '{:<12} {:<12} {:<4}'.format(
                "TACIT", "ALL", self.repeat)
        return ''.join(str_list)


class Head(Interval):
    def __init__(self, repeat):
        super().__init__(repeat)
        self.role_cats[Role.HEAD] = [e.name for i,e in enumerate(Instrument)]


class Chorus(Interval):
    def __init__(self, soloist, repeat):
        super().__init__(repeat)
        self.role_cats[Role.SOLO] = [soloist.name]
        self.role_cats[Role.COMP] = [e.name for i,e in enumerate(Instrument) if e!=soloist]
