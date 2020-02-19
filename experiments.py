# -*- coding: UTF-8 -*-

#import testlib2 as lib

#----- Settings ends -----#

from testlib2 import *

start_time = time.time()
log = Log('ExperimentsLog.txt')
log.sep()

FlucIcen	= Parameter('FlucIcen', 200, 300, step=10)
FlucJcen	= Parameter('FlucJcen', 1100, 1200, step=10)

# Experiment
n_parameters_test(FlucJcen, FlucIcen, log=log.q)

# For tests
# set_parameter('FlucNe0', 0.3e19)
# n_parameters_test(FlucIcen, FlucJcen, log=log.q)
# parameter_test(Parameter('FlucBuild', 0, 0, n=1), log=log.q)

finish_time = time.time()
log.q('Program finished. Seconds elapsed: {}.'.format(finish_time - start_time))