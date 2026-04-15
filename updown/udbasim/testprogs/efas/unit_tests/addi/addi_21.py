from EFA_v2 import *
def addi_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8341859422671771514, 14474]
    tran0.writeAction("movir X16 29636")
    tran0.writeAction("slorii X16 X16 12 975")
    tran0.writeAction("slorii X16 X16 12 678")
    tran0.writeAction("slorii X16 X16 12 2441")
    tran0.writeAction("slorii X16 X16 12 1914")
    tran0.writeAction("addi X16 X17 14474")
    tran0.writeAction("yieldt")
    return efa
