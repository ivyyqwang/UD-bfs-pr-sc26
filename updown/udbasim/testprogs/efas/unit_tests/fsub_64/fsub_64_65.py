from EFA_v2 import *
def fsub_64_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5065484618860688586, 1824830259548332988]
    tran0.writeAction("movir X16 17996")
    tran0.writeAction("slorii X16 X16 12 886")
    tran0.writeAction("slorii X16 X16 12 3130")
    tran0.writeAction("slorii X16 X16 12 1623")
    tran0.writeAction("slorii X16 X16 12 1226")
    tran0.writeAction("movir X17 6483")
    tran0.writeAction("slorii X17 X17 12 407")
    tran0.writeAction("slorii X17 X17 12 995")
    tran0.writeAction("slorii X17 X17 12 3122")
    tran0.writeAction("slorii X17 X17 12 956")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
