from EFA_v2 import *
def divi_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8099360241595584312, -14157]
    tran0.writeAction("movir X16 36761")
    tran0.writeAction("slorii X16 X16 12 1196")
    tran0.writeAction("slorii X16 X16 12 1475")
    tran0.writeAction("slorii X16 X16 12 3167")
    tran0.writeAction("slorii X16 X16 12 200")
    tran0.writeAction("divi X16 X17 -14157")
    tran0.writeAction("yieldt")
    return efa
