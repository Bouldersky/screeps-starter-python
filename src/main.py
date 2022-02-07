import baseCreep
import roomManager
import baseSpawn

from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def main():
    for room in _.filter(Game.rooms, lambda r: r.controller.my):
        roomManager.update_room(room)

    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]
        baseCreep.run_creep(creep)

    for name in Object.keys(Game.spawns):
        sp = Game.spawns[name]
        baseSpawn.run_spawn(sp)

    if Game.time % 200 == 0:
        cleanMemory()

def cleanMemory():
    print("Cleaning memory")
    for creep in Object.keys(Memory.creeps):
        if not Object.keys(Game.creeps).includes(creep):
            del Memory.creeps[creep]

module.exports.loop = main
