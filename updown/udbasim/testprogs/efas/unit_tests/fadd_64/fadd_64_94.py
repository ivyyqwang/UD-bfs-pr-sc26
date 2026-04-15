from EFA_v2 import *
def fadd_64_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [260555717306450299, 12406613477741469608]
    tran0.writeAction("movir X16 925")
    tran0.writeAction("slorii X16 X16 12 2784")
    tran0.writeAction("slorii X16 X16 12 2910")
    tran0.writeAction("slorii X16 X16 12 1016")
    tran0.writeAction("slorii X16 X16 12 379")
    tran0.writeAction("movir X17 44077")
    tran0.writeAction("slorii X17 X17 12 595")
    tran0.writeAction("slorii X17 X17 12 2454")
    tran0.writeAction("slorii X17 X17 12 1449")
    tran0.writeAction("slorii X17 X17 12 4008")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
