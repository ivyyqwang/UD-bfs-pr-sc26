from EFA_v2 import *
def fmul_64_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3810230996460147548, 15098034876272113496]
    tran0.writeAction("movir X16 13536")
    tran0.writeAction("slorii X16 X16 12 2702")
    tran0.writeAction("slorii X16 X16 12 1888")
    tran0.writeAction("slorii X16 X16 12 777")
    tran0.writeAction("slorii X16 X16 12 860")
    tran0.writeAction("movir X17 53638")
    tran0.writeAction("slorii X17 X17 12 4075")
    tran0.writeAction("slorii X17 X17 12 2598")
    tran0.writeAction("slorii X17 X17 12 2695")
    tran0.writeAction("slorii X17 X17 12 1880")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
