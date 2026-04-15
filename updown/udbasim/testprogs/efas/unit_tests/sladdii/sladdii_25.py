from EFA_v2 import *
def sladdii_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7805580217117453320, 15, 881]
    tran0.writeAction("movir X16 37805")
    tran0.writeAction("slorii X16 X16 12 34")
    tran0.writeAction("slorii X16 X16 12 1524")
    tran0.writeAction("slorii X16 X16 12 3677")
    tran0.writeAction("slorii X16 X16 12 1016")
    tran0.writeAction("sladdii X16 X17 15 881")
    tran0.writeAction("yieldt")
    return efa
