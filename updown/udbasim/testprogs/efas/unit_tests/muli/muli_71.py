from EFA_v2 import *
def muli_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6191202702123060147, -25277]
    tran0.writeAction("movir X16 43540")
    tran0.writeAction("slorii X16 X16 12 1759")
    tran0.writeAction("slorii X16 X16 12 479")
    tran0.writeAction("slorii X16 X16 12 2115")
    tran0.writeAction("slorii X16 X16 12 1101")
    tran0.writeAction("muli X16 X17 -25277")
    tran0.writeAction("yieldt")
    return efa
