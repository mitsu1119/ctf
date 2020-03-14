import angr

f = "autorev_assemble"

p = angr.Project(f)
state = p.factory.entry_state()
simgr = p.factory.simulation_manager(state)

simgr.explore(find=0x408953, avoid=0x408961)
found = simgr.found[0]
print(found.posix.dumps(0))
