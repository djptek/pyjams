band = ['horn', 'guitar', 'drums', 'bass']

def play_hear(playing_now, play_buffer):
    print 'PLAY {:<30} HEAR {:<30}'.format(playing_now, play_buffer)
    return playing_now

heads = 2
choruses_per_cat = 2
intervals = heads+choruses_per_cat*len(band)+heads
play_buffer = 'tacit'

for interval in range(intervals+1):
    print '+++ Interval '+str(interval+1)+' +++'
    if interval <= 1 or interval == intervals-1:
        play_buffer = play_hear('all play head', play_buffer)
    elif interval == intervals:
        play_buffer = play_hear('tacit', play_buffer)
    elif interval / choruses_per_cat <= len(band):
        play_buffer = play_hear(
            band[(interval/choruses_per_cat)-1] \
            +' solo chorus '+str((interval % choruses_per_cat)+1) ,play_buffer)
    else:
        play_buffer = play_hear('all play head', play_buffer)

