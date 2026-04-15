from EFA_v2 import *
def mul_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1727351821895596861, 7776138563708660964]
    tran0.writeAction("movir X16 6136")
    tran0.writeAction("slorii X16 X16 12 3221")
    tran0.writeAction("slorii X16 X16 12 1154")
    tran0.writeAction("slorii X16 X16 12 863")
    tran0.writeAction("slorii X16 X16 12 2877")
    tran0.writeAction("movir X17 27626")
    tran0.writeAction("slorii X17 X17 12 1613")
    tran0.writeAction("slorii X17 X17 12 750")
    tran0.writeAction("slorii X17 X17 12 290")
    tran0.writeAction("slorii X17 X17 12 3300")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
