from EFA_v2 import *
def fmadd_32_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [311609528, 382169211, 575734673]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 18")
    tran0.writeAction("slorii X16 X16 12 2348")
    tran0.writeAction("slorii X16 X16 12 2232")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 22")
    tran0.writeAction("slorii X17 X17 12 3191")
    tran0.writeAction("slorii X17 X17 12 123")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 34")
    tran0.writeAction("slorii X18 X18 12 1296")
    tran0.writeAction("slorii X18 X18 12 913")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
