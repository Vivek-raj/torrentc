import libtorrent as lbt
import time
import sys
 
ses = lbt.session()
ses.listen_on(4000, 4001)
 
info = lbt.torrent_info(sys.argv[1])
h = ses.add_torrent({'ti': info, 'save_path': './'})
print 'starting', h.name()
 
while (not h.is_seed()):
   s = h.status()
 
   state_str = ['Queued', 'Checking', 'Metadata', \
      'Downloading', 'Completed', 'Seeding', 'Allocating', 'Checking resume']
   print '\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d seeds: %d ) %s' % \
      (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
      s.num_peers,s.num_seeds, state_str[s.state]),
   sys.stdout.flush()
 
   time.sleep(1)
 
print h.name(), 'Complete'
