from EFA_v2 import *
def fsub_64_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12741197463760077858, 4882985600088313793]
    tran0.writeAction("movir X16 45265")
    tran0.writeAction("slorii X16 X16 12 3385")
    tran0.writeAction("slorii X16 X16 12 1640")
    tran0.writeAction("slorii X16 X16 12 2160")
    tran0.writeAction("slorii X16 X16 12 1058")
    tran0.writeAction("movir X17 17347")
    tran0.writeAction("slorii X17 X17 12 3480")
    tran0.writeAction("slorii X17 X17 12 2104")
    tran0.writeAction("slorii X17 X17 12 2504")
    tran0.writeAction("slorii X17 X17 12 4033")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
