from EFA_v2 import *
def slsubii_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9128880058247821299, 8, 1894]
    tran0.writeAction("movir X16 33103")
    tran0.writeAction("slorii X16 X16 12 2879")
    tran0.writeAction("slorii X16 X16 12 1074")
    tran0.writeAction("slorii X16 X16 12 4060")
    tran0.writeAction("slorii X16 X16 12 2061")
    tran0.writeAction("slsubii X16 X17 8 1894")
    tran0.writeAction("yieldt")
    return efa
