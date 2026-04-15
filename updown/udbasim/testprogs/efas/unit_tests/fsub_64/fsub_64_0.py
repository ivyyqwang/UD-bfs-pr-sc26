from EFA_v2 import *
def fsub_64_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2399463447449569013, 6563030102412072803]
    tran0.writeAction("movir X16 8524")
    tran0.writeAction("slorii X16 X16 12 2484")
    tran0.writeAction("slorii X16 X16 12 2788")
    tran0.writeAction("slorii X16 X16 12 3136")
    tran0.writeAction("slorii X16 X16 12 1781")
    tran0.writeAction("movir X17 23316")
    tran0.writeAction("slorii X17 X17 12 2321")
    tran0.writeAction("slorii X17 X17 12 2832")
    tran0.writeAction("slorii X17 X17 12 1913")
    tran0.writeAction("slorii X17 X17 12 1891")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
