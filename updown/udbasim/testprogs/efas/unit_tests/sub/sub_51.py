from EFA_v2 import *
def sub_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5460315136791385924, -7141024826562183019]
    tran0.writeAction("movir X16 19398")
    tran0.writeAction("slorii X16 X16 12 3834")
    tran0.writeAction("slorii X16 X16 12 4058")
    tran0.writeAction("slorii X16 X16 12 569")
    tran0.writeAction("slorii X16 X16 12 1860")
    tran0.writeAction("movir X17 40165")
    tran0.writeAction("slorii X17 X17 12 4028")
    tran0.writeAction("slorii X17 X17 12 328")
    tran0.writeAction("slorii X17 X17 12 2112")
    tran0.writeAction("slorii X17 X17 12 149")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
