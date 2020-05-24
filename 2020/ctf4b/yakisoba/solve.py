import angr

base = 0x400000
addr_succeeded = base+0x6d2
addr_failed = base+0x6f7
addr_main = base + 0x680

p = angr.Project("./yakisoba", load_options={'auto_load_libs': False})

state = p.factory.entry_state()
simgr = p.factory.simulation_manager(state)

simgr.explore(find=addr_succeeded, avoid=addr_failed)
found = simgr.found[0]
print(found.posix.dumps(0))
