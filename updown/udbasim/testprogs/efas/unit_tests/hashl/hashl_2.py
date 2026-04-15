from EFA_v2 import *
def hashl_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4590020268560102786, 7620704870083578226, 87303485682860444]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 49228")
    tran0.writeAction("slorii X17 X17 12 3982")
    tran0.writeAction("slorii X17 X17 12 636")
    tran0.writeAction("slorii X17 X17 12 2588")
    tran0.writeAction("slorii X17 X17 12 2686")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 27074")
    tran0.writeAction("slorii X17 X17 12 747")
    tran0.writeAction("slorii X17 X17 12 1023")
    tran0.writeAction("slorii X17 X17 12 1724")
    tran0.writeAction("slorii X17 X17 12 2418")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 310")
    tran0.writeAction("slorii X17 X17 12 672")
    tran0.writeAction("slorii X17 X17 12 3779")
    tran0.writeAction("slorii X17 X17 12 3196")
    tran0.writeAction("slorii X17 X17 12 412")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
