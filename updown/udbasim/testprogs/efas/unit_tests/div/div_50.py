from EFA_v2 import *
def div_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5767703966642273956, -8886404525569513529]
    tran0.writeAction("movir X16 20491")
    tran0.writeAction("slorii X16 X16 12 3")
    tran0.writeAction("slorii X16 X16 12 757")
    tran0.writeAction("slorii X16 X16 12 1327")
    tran0.writeAction("slorii X16 X16 12 3748")
    tran0.writeAction("movir X17 33965")
    tran0.writeAction("slorii X17 X17 12 610")
    tran0.writeAction("slorii X17 X17 12 2699")
    tran0.writeAction("slorii X17 X17 12 22")
    tran0.writeAction("slorii X17 X17 12 1991")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
