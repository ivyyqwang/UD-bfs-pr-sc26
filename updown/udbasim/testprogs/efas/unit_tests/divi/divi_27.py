from EFA_v2 import *
def divi_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9140953738321634628, -31352]
    tran0.writeAction("movir X16 33060")
    tran0.writeAction("slorii X16 X16 12 3312")
    tran0.writeAction("slorii X16 X16 12 383")
    tran0.writeAction("slorii X16 X16 12 245")
    tran0.writeAction("slorii X16 X16 12 2748")
    tran0.writeAction("divi X16 X17 -31352")
    tran0.writeAction("yieldt")
    return efa
