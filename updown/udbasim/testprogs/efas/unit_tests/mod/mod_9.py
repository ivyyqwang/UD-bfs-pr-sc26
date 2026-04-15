from EFA_v2 import *
def mod_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4487243514623524332, -308590430889257878]
    tran0.writeAction("movir X16 15941")
    tran0.writeAction("slorii X16 X16 12 3651")
    tran0.writeAction("slorii X16 X16 12 957")
    tran0.writeAction("slorii X16 X16 12 3319")
    tran0.writeAction("slorii X16 X16 12 3564")
    tran0.writeAction("movir X17 64439")
    tran0.writeAction("slorii X17 X17 12 2730")
    tran0.writeAction("slorii X17 X17 12 857")
    tran0.writeAction("slorii X17 X17 12 3117")
    tran0.writeAction("slorii X17 X17 12 1130")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
