from EFA_v2 import *
def sraddii_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3536667453736995213, 0, 237]
    tran0.writeAction("movir X16 12564")
    tran0.writeAction("slorii X16 X16 12 3140")
    tran0.writeAction("slorii X16 X16 12 4004")
    tran0.writeAction("slorii X16 X16 12 2780")
    tran0.writeAction("slorii X16 X16 12 2445")
    tran0.writeAction("sraddii X16 X17 0 237")
    tran0.writeAction("yieldt")
    return efa
