from EFA_v2 import *
def div_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3231116965944655573, -7537418267189615754]
    tran0.writeAction("movir X16 54056")
    tran0.writeAction("slorii X16 X16 12 3139")
    tran0.writeAction("slorii X16 X16 12 3353")
    tran0.writeAction("slorii X16 X16 12 536")
    tran0.writeAction("slorii X16 X16 12 299")
    tran0.writeAction("movir X17 38757")
    tran0.writeAction("slorii X17 X17 12 2912")
    tran0.writeAction("slorii X17 X17 12 1372")
    tran0.writeAction("slorii X17 X17 12 2550")
    tran0.writeAction("slorii X17 X17 12 886")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
