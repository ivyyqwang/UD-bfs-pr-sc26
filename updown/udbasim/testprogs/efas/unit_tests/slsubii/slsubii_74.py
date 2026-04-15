from EFA_v2 import *
def slsubii_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4266349316806546408, 13, 1710]
    tran0.writeAction("movir X16 15157")
    tran0.writeAction("slorii X16 X16 12 481")
    tran0.writeAction("slorii X16 X16 12 2427")
    tran0.writeAction("slorii X16 X16 12 4033")
    tran0.writeAction("slorii X16 X16 12 1000")
    tran0.writeAction("slsubii X16 X17 13 1710")
    tran0.writeAction("yieldt")
    return efa
