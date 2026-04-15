from EFA_v2 import *
def fmadd_32_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3190528623, 1928515545, 403090208]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 190")
    tran0.writeAction("slorii X16 X16 12 697")
    tran0.writeAction("slorii X16 X16 12 2671")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 114")
    tran0.writeAction("slorii X17 X17 12 3884")
    tran0.writeAction("slorii X17 X17 12 4057")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 24")
    tran0.writeAction("slorii X18 X18 12 106")
    tran0.writeAction("slorii X18 X18 12 2848")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
