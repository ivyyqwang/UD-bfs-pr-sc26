from EFA_v2 import *
def fmul_64_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7967453191989631613, 7508687673746937348]
    tran0.writeAction("movir X16 28306")
    tran0.writeAction("slorii X16 X16 12 327")
    tran0.writeAction("slorii X16 X16 12 1785")
    tran0.writeAction("slorii X16 X16 12 385")
    tran0.writeAction("slorii X16 X16 12 2685")
    tran0.writeAction("movir X17 26676")
    tran0.writeAction("slorii X17 X17 12 890")
    tran0.writeAction("slorii X17 X17 12 2067")
    tran0.writeAction("slorii X17 X17 12 165")
    tran0.writeAction("slorii X17 X17 12 1540")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
