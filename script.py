import exifread
import matplotlib.pyplot as plt
import numpy as np
import os, glob

from collections import Counter

def matplot_hist(seq) -> None:
  # An "interface" to matplotlib.axes.Axes.hist() method
  n, bins, patches = plt.hist(x=seq, bins='auto', color='#0504aa',
                              alpha=0.7, rwidth=0.85)
  plt.grid(axis='y', alpha=0.75)
  plt.xlabel('FocalLengthIn35mmFilm')
  plt.ylabel('Frequency')
  plt.title('Focal lengths used')
  maxfreq = n.max()
  # Set a clean upper y-axis limit.
  plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
  plt.savefig('photos/focallength.png')

def ascii_histogram(seq) -> None:
    """A horizontal frequency-table/histogram plot."""
    counted = Counter(seq)
    for k in sorted(counted):
        print('{0:5d} {1}'.format(k, '+' * counted[k]))

def get_focal_length(ratio) -> float:
  f = [int(n) for n in ratio.split('/')]
  if (len(f) == 1):
    return f[0]
  return f[0] / f[1]

# files = os.listdir('photos')
files = glob.glob('photos/*.jpg')

fl = []
for file in files:
  # Open image file for reading (binary mode)
  f = open(file, 'rb')

  # Return Exif tags
  tags = exifread.process_file(f, details=False)
  for tag in tags.keys():
    # if tag == 'EXIF FocalLength':
    if 'FocalLengthIn35mmFilm' in tag:
      fl.append(get_focal_length("%s" % tags[tag]))

matplot_hist(fl)
