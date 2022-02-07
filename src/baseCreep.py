from builder import *
from courier import *
from harvester import * 
from bootstrapHarvester import *

from defs import *
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def run_creep(creep):
    creepType = creep.memory.type
    if creepType == "harvester":
        run_harvester(creep)
    elif creepType == "courier":
        run_courier(creep)
    elif creepType == "builder":
        run_builder(creep)
    elif creepType == "bootstrapHarvester":
        run_bootstrapHarvester(creep)
