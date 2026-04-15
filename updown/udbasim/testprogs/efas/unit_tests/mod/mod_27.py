from EFA_v2 import *
def mod_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4823979338781945787, -5197838375102819055]
    tran0.writeAction("movir X16 48397")
    tran0.writeAction("slorii X16 X16 12 3205")
    tran0.writeAction("slorii X16 X16 12 2452")
    tran0.writeAction("slorii X16 X16 12 321")
    tran0.writeAction("slorii X16 X16 12 69")
    tran0.writeAction("movir X17 47069")
    tran0.writeAction("slorii X17 X17 12 2328")
    tran0.writeAction("slorii X17 X17 12 2436")
    tran0.writeAction("slorii X17 X17 12 421")
    tran0.writeAction("slorii X17 X17 12 1297")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
