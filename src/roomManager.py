from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def update_room(room):
    if not room.memory.spawn_queue:
        room.memory.spawn_queue = []
    if not room.memory.courier_queue:
        room.memory.courier_queue = []

    spawnHarvesters(room)
    spawnBootstrapHarvesters(room)
    # spawnBuilders(room)


def spawnHarvesters(room):
    spawn_q = room.memory.spawn_queue
    containers = room.find(FIND_MY_STRUCTURES, lambda s: s.structureType == STRUCTURE_CONTAINER)
    harvesters = _.filter(room.find(FIND_MY_CREEPS), {"filter" : lambda c: c.memory.type == "harvester"})
    occupiedContainers = _.map(harvesters, {"filter": lambda c, i, j: c.memory.target})
    freeContainers = _.filter(containers, {"filter": lambda c: not occupiedContainers.includes(c.id)})

    while (freeContainers[0]):
        c = freeContainers.pop()
        room.memory.spawn_queue.push({"type": "harvester",
            "target": c.pos.findClosestByRange(FIND_SOURCES_ACTIVE).id,
            "targetContainer": c.id})

def spawnBuilders(room):
    if countBuilders(room) < 3:
        room.memory.spawn_queue.push({"type": "builder"})

def countBuilders(room):
    buildCount = _.size(room.find(FIND_MY_CREEPS, {"filter" : lambda c: c.memory.type == "builder"}))
    buildCount += _.size(room.find(FIND_MY_SPAWNS, {"filter" : lambda s: s.spawning != None and s.spawning.name.includes("builder")}))
    buildCount += _.size(_.filter(room.memory.spawn_queue, lambda x: x["type"] == "builder"))
    return buildCount

def spawnBootstrapHarvesters(room):
    if countBootstrapHarvesters(room) < 8:
        room.memory.spawn_queue.push({"type": "bootstrapHarvester"})
        

def countBootstrapHarvesters(room):
    harvCount = _.size(room.find(FIND_MY_CREEPS, {"filter" : lambda c: c.memory.type == "bootstrapHarvester"}))
    harvCount += _.size(room.find(FIND_MY_SPAWNS, {"filter" : lambda s: s.spawning != None and s.spawning.name.includes("bootstrapHarvester")}))
    harvCount += _.size(_.filter(room.memory.spawn_queue, lambda x: x["type"] == "bootstrapHarvester"))
    return harvCount
