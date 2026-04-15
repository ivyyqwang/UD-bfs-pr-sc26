from EFA_v2 import *
def mod_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8768655594825295041, 1913997136907589611]
    tran0.writeAction("movir X16 31152")
    tran0.writeAction("slorii X16 X16 12 2140")
    tran0.writeAction("slorii X16 X16 12 3615")
    tran0.writeAction("slorii X16 X16 12 1242")
    tran0.writeAction("slorii X16 X16 12 1217")
    tran0.writeAction("movir X17 6799")
    tran0.writeAction("slorii X17 X17 12 3620")
    tran0.writeAction("slorii X17 X17 12 342")
    tran0.writeAction("slorii X17 X17 12 2013")
    tran0.writeAction("slorii X17 X17 12 2027")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
