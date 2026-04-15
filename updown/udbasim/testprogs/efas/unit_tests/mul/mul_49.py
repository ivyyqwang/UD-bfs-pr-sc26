from EFA_v2 import *
def mul_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2188237296286875016, 1440903090181598494]
    tran0.writeAction("movir X16 7774")
    tran0.writeAction("slorii X16 X16 12 739")
    tran0.writeAction("slorii X16 X16 12 2601")
    tran0.writeAction("slorii X16 X16 12 1803")
    tran0.writeAction("slorii X16 X16 12 3464")
    tran0.writeAction("movir X17 5119")
    tran0.writeAction("slorii X17 X17 12 475")
    tran0.writeAction("slorii X17 X17 12 2542")
    tran0.writeAction("slorii X17 X17 12 150")
    tran0.writeAction("slorii X17 X17 12 3358")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
