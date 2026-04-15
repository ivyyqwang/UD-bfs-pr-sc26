from EFA_v2 import *
def mul_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2457536434184588371, 2192905337107633147]
    tran0.writeAction("movir X16 56805")
    tran0.writeAction("slorii X16 X16 12 314")
    tran0.writeAction("slorii X16 X16 12 569")
    tran0.writeAction("slorii X16 X16 12 3471")
    tran0.writeAction("slorii X16 X16 12 941")
    tran0.writeAction("movir X17 7790")
    tran0.writeAction("slorii X17 X17 12 3132")
    tran0.writeAction("slorii X17 X17 12 2332")
    tran0.writeAction("slorii X17 X17 12 1469")
    tran0.writeAction("slorii X17 X17 12 1019")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
