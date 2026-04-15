from EFA_v2 import *
def ori_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -583")
    tran0.writeAction("slorii X16 X16 12 571")
    tran0.writeAction("slorii X16 X16 12 3051")
    tran0.writeAction("slorii X16 X16 12 2911")
    tran0.writeAction("slorii X16 X16 12 3768")
    tran0.writeAction("movir X17 19123")
    tran0.writeAction("slorii X17 X17 12 3225")
    tran0.writeAction("slorii X17 X17 12 4042")
    tran0.writeAction("slorii X17 X17 12 3795")
    tran0.writeAction("slorii X17 X17 12 814")
    tran0.writeAction("ori X16 X17 -17447")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
