from EFA_v2 import *
def slsubii_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4866300009277603499, 0, 794]
    tran0.writeAction("movir X16 48247")
    tran0.writeAction("slorii X16 X16 12 1758")
    tran0.writeAction("slorii X16 X16 12 3232")
    tran0.writeAction("slorii X16 X16 12 2164")
    tran0.writeAction("slorii X16 X16 12 341")
    tran0.writeAction("slsubii X16 X17 0 794")
    tran0.writeAction("yieldt")
    return efa
