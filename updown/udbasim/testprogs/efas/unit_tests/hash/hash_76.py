from EFA_v2 import *
def hash_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6534013545547152453, 2494777521428493679]
    tran0.writeAction("movir X16 23213")
    tran0.writeAction("slorii X16 X16 12 1963")
    tran0.writeAction("slorii X16 X16 12 883")
    tran0.writeAction("slorii X16 X16 12 3803")
    tran0.writeAction("slorii X16 X16 12 3141")
    tran0.writeAction("movir X17 8863")
    tran0.writeAction("slorii X17 X17 12 943")
    tran0.writeAction("slorii X17 X17 12 22")
    tran0.writeAction("slorii X17 X17 12 1535")
    tran0.writeAction("slorii X17 X17 12 1391")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
