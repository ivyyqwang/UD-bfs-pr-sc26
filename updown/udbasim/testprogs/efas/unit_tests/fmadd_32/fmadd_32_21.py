from EFA_v2 import *
def fmadd_32_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1851697899, 2929111215, 1269332500]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 110")
    tran0.writeAction("slorii X16 X16 12 1514")
    tran0.writeAction("slorii X16 X16 12 2795")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 174")
    tran0.writeAction("slorii X17 X17 12 2411")
    tran0.writeAction("slorii X17 X17 12 175")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 75")
    tran0.writeAction("slorii X18 X18 12 2695")
    tran0.writeAction("slorii X18 X18 12 2580")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
