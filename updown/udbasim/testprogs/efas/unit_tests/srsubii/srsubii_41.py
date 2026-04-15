from EFA_v2 import *
def srsubii_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8331850496079138751, 6, 1072]
    tran0.writeAction("movir X16 29600")
    tran0.writeAction("slorii X16 X16 12 2782")
    tran0.writeAction("slorii X16 X16 12 468")
    tran0.writeAction("slorii X16 X16 12 1880")
    tran0.writeAction("slorii X16 X16 12 4031")
    tran0.writeAction("srsubii X16 X17 6 1072")
    tran0.writeAction("yieldt")
    return efa
