from EFA_v2 import *
def div_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2798492556600127399, -1295097264473493232]
    tran0.writeAction("movir X16 55593")
    tran0.writeAction("slorii X16 X16 12 3101")
    tran0.writeAction("slorii X16 X16 12 2249")
    tran0.writeAction("slorii X16 X16 12 1125")
    tran0.writeAction("slorii X16 X16 12 89")
    tran0.writeAction("movir X17 60934")
    tran0.writeAction("slorii X17 X17 12 3646")
    tran0.writeAction("slorii X17 X17 12 1617")
    tran0.writeAction("slorii X17 X17 12 1955")
    tran0.writeAction("slorii X17 X17 12 272")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
