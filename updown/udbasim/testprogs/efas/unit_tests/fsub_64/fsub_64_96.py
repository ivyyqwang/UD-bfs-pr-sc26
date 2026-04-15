from EFA_v2 import *
def fsub_64_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4072635937290680842, 177134180089174117]
    tran0.writeAction("movir X16 14468")
    tran0.writeAction("slorii X16 X16 12 3724")
    tran0.writeAction("slorii X16 X16 12 3749")
    tran0.writeAction("slorii X16 X16 12 2871")
    tran0.writeAction("slorii X16 X16 12 2570")
    tran0.writeAction("movir X17 629")
    tran0.writeAction("slorii X17 X17 12 1257")
    tran0.writeAction("slorii X17 X17 12 2345")
    tran0.writeAction("slorii X17 X17 12 3257")
    tran0.writeAction("slorii X17 X17 12 2149")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
