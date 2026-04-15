from EFA_v2 import *
def sraddii_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1572323690997138371, 9, 263]
    tran0.writeAction("movir X16 59949")
    tran0.writeAction("slorii X16 X16 12 4030")
    tran0.writeAction("slorii X16 X16 12 3838")
    tran0.writeAction("slorii X16 X16 12 755")
    tran0.writeAction("slorii X16 X16 12 3133")
    tran0.writeAction("sraddii X16 X17 9 263")
    tran0.writeAction("yieldt")
    return efa
