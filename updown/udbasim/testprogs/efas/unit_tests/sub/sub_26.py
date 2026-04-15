from EFA_v2 import *
def sub_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2200009437508125850, 8011067504146976362]
    tran0.writeAction("movir X16 7816")
    tran0.writeAction("slorii X16 X16 12 14")
    tran0.writeAction("slorii X16 X16 12 3425")
    tran0.writeAction("slorii X16 X16 12 732")
    tran0.writeAction("slorii X16 X16 12 1178")
    tran0.writeAction("movir X17 28461")
    tran0.writeAction("slorii X17 X17 12 119")
    tran0.writeAction("slorii X17 X17 12 856")
    tran0.writeAction("slorii X17 X17 12 1456")
    tran0.writeAction("slorii X17 X17 12 3690")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
