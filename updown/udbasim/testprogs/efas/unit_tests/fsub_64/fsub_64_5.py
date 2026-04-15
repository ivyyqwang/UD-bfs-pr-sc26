from EFA_v2 import *
def fsub_64_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4131890895019247957, 16878962871011136316]
    tran0.writeAction("movir X16 14679")
    tran0.writeAction("slorii X16 X16 12 1742")
    tran0.writeAction("slorii X16 X16 12 152")
    tran0.writeAction("slorii X16 X16 12 1200")
    tran0.writeAction("slorii X16 X16 12 2389")
    tran0.writeAction("movir X17 59966")
    tran0.writeAction("slorii X17 X17 12 500")
    tran0.writeAction("slorii X17 X17 12 3447")
    tran0.writeAction("slorii X17 X17 12 2565")
    tran0.writeAction("slorii X17 X17 12 828")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
