from EFA_v2 import *
def srsubii_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3468252145640800772, 1, 927]
    tran0.writeAction("movir X16 12321")
    tran0.writeAction("slorii X16 X16 12 2895")
    tran0.writeAction("slorii X16 X16 12 876")
    tran0.writeAction("slorii X16 X16 12 1664")
    tran0.writeAction("slorii X16 X16 12 516")
    tran0.writeAction("srsubii X16 X17 1 927")
    tran0.writeAction("yieldt")
    return efa
