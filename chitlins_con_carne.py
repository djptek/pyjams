from instrument import Instrument
from arrangement import Arrangement

Title = "Chitlins Con Carne"
Heads = 1
Choruses_per_instrument = 4
Band = {'guitar1': Instrument.Guitar, \
        'keys': Instrument.Keys, \
        'guitar2': Instrument.Guitar,\
        'drummer': Instrument.Drums, \
        'bassist': Instrument.Bass}

Arrangement(Title, Heads, Choruses_per_instrument, Band).__generate__()

