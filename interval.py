import instrument
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
                str_list += '{:<4} '.format(role.name)
                if role == Role.SOLO:
                    str_list += '{:<1} '.format(self.repeat)
                for instrument in self.role_cats[role]:
                    str_list += '{} '.format(instrument)
        else:
            str_list += '{:<12} {:<12} {:<4}'.format(
                "TACIT", "ALL", self.repeat)
        return ''.join(str_list)


class Head(Interval):
    def __init__(self, repeat, band):
        super().__init__(repeat)
        self.role_cats[Role.HEAD] = [e for e in band]


class Chorus(Interval):
    def __init__(self, soloist, instrument, repeat, rest_of_band):
        super().__init__(repeat)
        self.role_cats[Role.SOLO] = [soloist]
        if instrument != Instrument.Drums:
            self.role_cats[Role.COMP] = [
                e for e in rest_of_band \
                if (rest_of_band[e] in [Instrument.Drums]) or (
                        instrument not in [Instrument.Drums, Instrument.Bass])]
