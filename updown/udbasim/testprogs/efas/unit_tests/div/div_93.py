from EFA_v2 import *
def div_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7340466236357578771, 6110884543931867348]
    tran0.writeAction("movir X16 39457")
    tran0.writeAction("slorii X16 X16 12 1741")
    tran0.writeAction("slorii X16 X16 12 2424")
    tran0.writeAction("slorii X16 X16 12 646")
    tran0.writeAction("slorii X16 X16 12 4077")
    tran0.writeAction("movir X17 21710")
    tran0.writeAction("slorii X17 X17 12 913")
    tran0.writeAction("slorii X17 X17 12 3496")
    tran0.writeAction("slorii X17 X17 12 1982")
    tran0.writeAction("slorii X17 X17 12 212")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
