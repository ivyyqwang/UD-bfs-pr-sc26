from EFA_v2 import *
def div_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3018232374967298930, -6040945648938704911]
    tran0.writeAction("movir X16 10722")
    tran0.writeAction("slorii X16 X16 12 3749")
    tran0.writeAction("slorii X16 X16 12 2703")
    tran0.writeAction("slorii X16 X16 12 2086")
    tran0.writeAction("slorii X16 X16 12 2930")
    tran0.writeAction("movir X17 44074")
    tran0.writeAction("slorii X17 X17 12 1023")
    tran0.writeAction("slorii X17 X17 12 71")
    tran0.writeAction("slorii X17 X17 12 2321")
    tran0.writeAction("slorii X17 X17 12 4081")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
