from EFA_v2 import *
def fsub_64_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6003149606528602775, 8650793934793750015]
    tran0.writeAction("movir X16 21327")
    tran0.writeAction("slorii X16 X16 12 1932")
    tran0.writeAction("slorii X16 X16 12 726")
    tran0.writeAction("slorii X16 X16 12 2717")
    tran0.writeAction("slorii X16 X16 12 663")
    tran0.writeAction("movir X17 30733")
    tran0.writeAction("slorii X17 X17 12 3251")
    tran0.writeAction("slorii X17 X17 12 4084")
    tran0.writeAction("slorii X17 X17 12 1987")
    tran0.writeAction("slorii X17 X17 12 1535")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
