from EFA_v2 import *
def sladdii_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7215731509794902958, 8, 1560]
    tran0.writeAction("movir X16 25635")
    tran0.writeAction("slorii X16 X16 12 1753")
    tran0.writeAction("slorii X16 X16 12 987")
    tran0.writeAction("slorii X16 X16 12 3761")
    tran0.writeAction("slorii X16 X16 12 942")
    tran0.writeAction("sladdii X16 X17 8 1560")
    tran0.writeAction("yieldt")
    return efa
