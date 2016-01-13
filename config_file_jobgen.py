#!/usr/bin/env python

from prody import *
from pylab import *
import numpy as np
from os.path import basename
import fnmatch
import os

f = open("config_joblist", 'w')

f.write("#!/bin/bash\n")
f.write("echo config jobs started\n")

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*_config.conf'):
        config = file
        file_name_wh_ex = str(os.path.splitext(config)[0])
        logfile = str(file_name_wh_ex+".log")
        f.write("namd2 +p8 %s > %s\n" % (str(config), str(logfile)))
        f.write("echo job for %s is finished\n" % str(config))

f.close()