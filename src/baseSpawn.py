from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def run_spawn(spawn):
    if (not spawn.spawning) and spawn.store.energy >= 300:
        queue = spawn.room.memory.spawn_queue
        if _.size(queue):
            job = queue.pop()
            typ = job["type"]
            if typ == "harvester":
                spawn_harvester(spawn, job)
            elif typ == "courier":
                spawn_courier(spawn, job)
            elif typ == "builder":
                spawn_builder(spawn, job)

def _getName(prefix, spawn):
    return "{}{}".format(prefix, Game.time)

def _spawnRandom(spawn):
    _.sample([spawn_courier, spawn_builder])(spawn)

def spawn_harvester(spawn, job):
    print("spawning harvester")
    spawn.spawnCreep([WORK, WORK, CARRY, MOVE], _getName(job["type"], spawn), 
            {"memory": {
                "type": job["type"],
                "target": job["target"],
                "targetContainer": job["targetContainer"]}
            })

def spawn_courier(spawn, job):
    print("spawning courier")
    typ = "courier"
    spawn.spawnCreep([CARRY, CARRY, CARRY, MOVE, MOVE, MOVE], _getName(job["type"], spawn), {"memory": {"type": typ}})

def spawn_builder(spawn, job):
    print("spawning builder")
    spawn.spawnCreep([WORK, WORK, CARRY, MOVE], _getName(job["type"], spawn), {"memory": {"type": job["type"]}})

def spawn_bootstrapHarvester(spawn, job):
    print("spawning bootstrap harvester")
    spawn.spawnCreep([WORK, CARRY, MOVE, MOVE], _getName(job["type"], spawn), {"memory": {"type": job["bootstrapHarvester"]}})
