from EFA_v2 import *
def fmadd_32_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [97445100, 1702003623, 3842531394]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 5")
    tran0.writeAction("slorii X16 X16 12 3310")
    tran0.writeAction("slorii X16 X16 12 1260")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 101")
    tran0.writeAction("slorii X17 X17 12 1832")
    tran0.writeAction("slorii X17 X17 12 935")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 229")
    tran0.writeAction("slorii X18 X18 12 134")
    tran0.writeAction("slorii X18 X18 12 66")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
