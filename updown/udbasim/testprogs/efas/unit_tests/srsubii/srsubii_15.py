from EFA_v2 import *
def srsubii_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3532475861736177611, 0, 1197]
    tran0.writeAction("movir X16 12549")
    tran0.writeAction("slorii X16 X16 12 3585")
    tran0.writeAction("slorii X16 X16 12 1172")
    tran0.writeAction("slorii X16 X16 12 1747")
    tran0.writeAction("slorii X16 X16 12 4043")
    tran0.writeAction("srsubii X16 X17 0 1197")
    tran0.writeAction("yieldt")
    return efa
