from EFA_v2 import *
def fmul_64_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13818124466710341177, 5738804765205826454]
    tran0.writeAction("movir X16 49091")
    tran0.writeAction("slorii X16 X16 12 3439")
    tran0.writeAction("slorii X16 X16 12 3500")
    tran0.writeAction("slorii X16 X16 12 1654")
    tran0.writeAction("slorii X16 X16 12 1593")
    tran0.writeAction("movir X17 20388")
    tran0.writeAction("slorii X17 X17 12 1352")
    tran0.writeAction("slorii X17 X17 12 1865")
    tran0.writeAction("slorii X17 X17 12 1688")
    tran0.writeAction("slorii X17 X17 12 2966")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
