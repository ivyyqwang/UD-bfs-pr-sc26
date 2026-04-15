from EFA_v2 import *
def mul_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3315262456133938324, 3052104055984063988]
    tran0.writeAction("movir X16 53757")
    tran0.writeAction("slorii X16 X16 12 3365")
    tran0.writeAction("slorii X16 X16 12 3188")
    tran0.writeAction("slorii X16 X16 12 3881")
    tran0.writeAction("slorii X16 X16 12 876")
    tran0.writeAction("movir X17 10843")
    tran0.writeAction("slorii X17 X17 12 1031")
    tran0.writeAction("slorii X17 X17 12 2010")
    tran0.writeAction("slorii X17 X17 12 1880")
    tran0.writeAction("slorii X17 X17 12 1524")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
