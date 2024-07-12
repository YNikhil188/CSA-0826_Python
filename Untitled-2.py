import numpy as np

print("Number of Sunday in November 2020:",
      np.busday_count('2020-11', '2020-12', weekmask='Sun'))

yearMonth = '2017-05'
