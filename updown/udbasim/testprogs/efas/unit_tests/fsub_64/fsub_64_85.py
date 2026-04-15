from EFA_v2 import *
def fsub_64_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4116862049578662811, 17766692110356671973]
    tran0.writeAction("movir X16 14626")
    tran0.writeAction("slorii X16 X16 12 131")
    tran0.writeAction("slorii X16 X16 12 2262")
    tran0.writeAction("slorii X16 X16 12 1731")
    tran0.writeAction("slorii X16 X16 12 2971")
    tran0.writeAction("movir X17 63119")
    tran0.writeAction("slorii X17 X17 12 3973")
    tran0.writeAction("slorii X17 X17 12 1959")
    tran0.writeAction("slorii X17 X17 12 2230")
    tran0.writeAction("slorii X17 X17 12 3557")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
