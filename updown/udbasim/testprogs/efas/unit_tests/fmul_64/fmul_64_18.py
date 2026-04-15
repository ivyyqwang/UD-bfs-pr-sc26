from EFA_v2 import *
def fmul_64_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6030124124758545725, 16977358209019364652]
    tran0.writeAction("movir X16 21423")
    tran0.writeAction("slorii X16 X16 12 1247")
    tran0.writeAction("slorii X16 X16 12 327")
    tran0.writeAction("slorii X16 X16 12 3057")
    tran0.writeAction("slorii X16 X16 12 1341")
    tran0.writeAction("movir X17 60315")
    tran0.writeAction("slorii X17 X17 12 2837")
    tran0.writeAction("slorii X17 X17 12 1881")
    tran0.writeAction("slorii X17 X17 12 660")
    tran0.writeAction("slorii X17 X17 12 1324")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
