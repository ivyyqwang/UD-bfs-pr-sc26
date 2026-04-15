from EFA_v2 import *
def vmadd_b16_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15922, 40025, 34387, 30541, 10733, 51030, 1601, 19291, 38091, 7325, 27979, 25503, 9]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1908")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 2149")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 2501")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 995")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1205")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 100")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 3189")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 670")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1593")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 1748")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 457")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 2380")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("vmadd.b16 X19 X17 X18 9 ")
    tran0.writeAction("yieldt")
    return efa
