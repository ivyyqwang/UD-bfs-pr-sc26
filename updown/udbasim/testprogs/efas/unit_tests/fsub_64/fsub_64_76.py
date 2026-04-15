from EFA_v2 import *
def fsub_64_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9191519724279089154, 15714525460791938622]
    tran0.writeAction("movir X16 32654")
    tran0.writeAction("slorii X16 X16 12 3431")
    tran0.writeAction("slorii X16 X16 12 3471")
    tran0.writeAction("slorii X16 X16 12 2668")
    tran0.writeAction("slorii X16 X16 12 2050")
    tran0.writeAction("movir X17 55829")
    tran0.writeAction("slorii X17 X17 12 858")
    tran0.writeAction("slorii X17 X17 12 1472")
    tran0.writeAction("slorii X17 X17 12 1372")
    tran0.writeAction("slorii X17 X17 12 3646")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
