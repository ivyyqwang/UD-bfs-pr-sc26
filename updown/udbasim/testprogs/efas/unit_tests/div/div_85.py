from EFA_v2 import *
def div_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7825252443688867275, 4778577335029834755]
    tran0.writeAction("movir X16 37735")
    tran0.writeAction("slorii X16 X16 12 485")
    tran0.writeAction("slorii X16 X16 12 3272")
    tran0.writeAction("slorii X16 X16 12 686")
    tran0.writeAction("slorii X16 X16 12 2613")
    tran0.writeAction("movir X17 16976")
    tran0.writeAction("slorii X17 X17 12 3756")
    tran0.writeAction("slorii X17 X17 12 1194")
    tran0.writeAction("slorii X17 X17 12 762")
    tran0.writeAction("slorii X17 X17 12 1027")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
