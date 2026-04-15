from EFA_v2 import *
def subi_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7688309884236521815, -10307]
    tran0.writeAction("movir X16 27314")
    tran0.writeAction("slorii X16 X16 12 1489")
    tran0.writeAction("slorii X16 X16 12 2805")
    tran0.writeAction("slorii X16 X16 12 174")
    tran0.writeAction("slorii X16 X16 12 343")
    tran0.writeAction("subi X16 X17 -10307")
    tran0.writeAction("yieldt")
    return efa
