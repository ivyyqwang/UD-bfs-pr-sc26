from EFA_v2 import *
def modi_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2712802064615128934, 18602]
    tran0.writeAction("movir X16 55898")
    tran0.writeAction("slorii X16 X16 12 782")
    tran0.writeAction("slorii X16 X16 12 1328")
    tran0.writeAction("slorii X16 X16 12 2740")
    tran0.writeAction("slorii X16 X16 12 154")
    tran0.writeAction("modi X16 X17 18602")
    tran0.writeAction("yieldt")
    return efa
