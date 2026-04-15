from EFA_v2 import *
def fsub_64_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4204730435692542769, 14619472572046103977]
    tran0.writeAction("movir X16 14938")
    tran0.writeAction("slorii X16 X16 12 832")
    tran0.writeAction("slorii X16 X16 12 3515")
    tran0.writeAction("slorii X16 X16 12 2979")
    tran0.writeAction("slorii X16 X16 12 2865")
    tran0.writeAction("movir X17 51938")
    tran0.writeAction("slorii X17 X17 12 3277")
    tran0.writeAction("slorii X17 X17 12 2260")
    tran0.writeAction("slorii X17 X17 12 1533")
    tran0.writeAction("slorii X17 X17 12 1449")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
