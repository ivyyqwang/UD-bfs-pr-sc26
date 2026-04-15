from EFA_v2 import *
def srsubii_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [785359378152359247, 15, 7]
    tran0.writeAction("movir X16 2790")
    tran0.writeAction("slorii X16 X16 12 643")
    tran0.writeAction("slorii X16 X16 12 387")
    tran0.writeAction("slorii X16 X16 12 3248")
    tran0.writeAction("slorii X16 X16 12 1359")
    tran0.writeAction("srsubii X16 X17 15 7")
    tran0.writeAction("yieldt")
    return efa
