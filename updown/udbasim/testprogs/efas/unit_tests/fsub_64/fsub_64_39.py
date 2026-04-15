from EFA_v2 import *
def fsub_64_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9278189186545054362, 5376260083915566158]
    tran0.writeAction("movir X16 32962")
    tran0.writeAction("slorii X16 X16 12 3070")
    tran0.writeAction("slorii X16 X16 12 2110")
    tran0.writeAction("slorii X16 X16 12 3639")
    tran0.writeAction("slorii X16 X16 12 666")
    tran0.writeAction("movir X17 19100")
    tran0.writeAction("slorii X17 X17 12 1280")
    tran0.writeAction("slorii X17 X17 12 4041")
    tran0.writeAction("slorii X17 X17 12 3682")
    tran0.writeAction("slorii X17 X17 12 3150")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
