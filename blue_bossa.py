from arrangement import Arrangement
from instrument import Instrument

Title = "Blue Bossa"
Heads = 2
Choruses_per_instrument = 2
Band = {'horn': Instrument.Horn, \
        'guitar': Instrument.Guitar, \
        'drummer': Instrument.Drums, \
        'bassist': Instrument.Bass}

Arrangement(Title, Heads, Choruses_per_instrument, Band).__generate__()

