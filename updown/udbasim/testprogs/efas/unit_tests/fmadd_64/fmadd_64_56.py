from EFA_v2 import *
def fmadd_64_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13526607340532074632, 15302464295930836889, 17151479814171409213]
    tran0.writeAction("movir X16 48056")
    tran0.writeAction("slorii X16 X16 12 667")
    tran0.writeAction("slorii X16 X16 12 1420")
    tran0.writeAction("slorii X16 X16 12 2480")
    tran0.writeAction("slorii X16 X16 12 2184")
    tran0.writeAction("movir X17 54365")
    tran0.writeAction("slorii X17 X17 12 1123")
    tran0.writeAction("slorii X17 X17 12 899")
    tran0.writeAction("slorii X17 X17 12 227")
    tran0.writeAction("slorii X17 X17 12 1945")
    tran0.writeAction("movir X18 60934")
    tran0.writeAction("slorii X18 X18 12 1216")
    tran0.writeAction("slorii X18 X18 12 1215")
    tran0.writeAction("slorii X18 X18 12 3971")
    tran0.writeAction("slorii X18 X18 12 2877")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
