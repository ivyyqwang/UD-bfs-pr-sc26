from EFA_v2 import *
def sladdii_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2031067501463176818, 11, 726]
    tran0.writeAction("movir X16 7215")
    tran0.writeAction("slorii X16 X16 12 3282")
    tran0.writeAction("slorii X16 X16 12 427")
    tran0.writeAction("slorii X16 X16 12 2264")
    tran0.writeAction("slorii X16 X16 12 1650")
    tran0.writeAction("sladdii X16 X17 11 726")
    tran0.writeAction("yieldt")
    return efa
