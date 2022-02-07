from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def run_harvester(creep):
    container = Game.getObjectById(creep.memory.targetContainer)
    if creep.pos.getRangeTo(container) > 0:
        creep.moveTo(container)
    else:
        if (creep.store.getFreeCapacity() == 0):
            creep.drop(RESOURCE_ENERGY)
        else:
            creep.harvest(Game.getObjectById(creep.memory.target))
