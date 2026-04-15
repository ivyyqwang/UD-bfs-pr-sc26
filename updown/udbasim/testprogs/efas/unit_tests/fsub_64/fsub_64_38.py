from EFA_v2 import *
def fsub_64_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13748184842247970144, 14466893458110248397]
    tran0.writeAction("movir X16 48843")
    tran0.writeAction("slorii X16 X16 12 1492")
    tran0.writeAction("slorii X16 X16 12 1508")
    tran0.writeAction("slorii X16 X16 12 2457")
    tran0.writeAction("slorii X16 X16 12 3424")
    tran0.writeAction("movir X17 51396")
    tran0.writeAction("slorii X17 X17 12 2991")
    tran0.writeAction("slorii X17 X17 12 902")
    tran0.writeAction("slorii X17 X17 12 343")
    tran0.writeAction("slorii X17 X17 12 1485")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
