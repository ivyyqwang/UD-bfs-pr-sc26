from EFA_v2 import *
def fsub_64_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14417907485893527132, 4964522846850058565]
    tran0.writeAction("movir X16 51222")
    tran0.writeAction("slorii X16 X16 12 2855")
    tran0.writeAction("slorii X16 X16 12 2069")
    tran0.writeAction("slorii X16 X16 12 528")
    tran0.writeAction("slorii X16 X16 12 1628")
    tran0.writeAction("movir X17 17637")
    tran0.writeAction("slorii X17 X17 12 2163")
    tran0.writeAction("slorii X17 X17 12 2525")
    tran0.writeAction("slorii X17 X17 12 3312")
    tran0.writeAction("slorii X17 X17 12 2373")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
