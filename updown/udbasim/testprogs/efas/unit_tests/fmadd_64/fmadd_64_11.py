from EFA_v2 import *
def fmadd_64_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17049557400629035310, 426927597342409675, 9872789976704493098]
    tran0.writeAction("movir X16 60572")
    tran0.writeAction("slorii X16 X16 12 801")
    tran0.writeAction("slorii X16 X16 12 3994")
    tran0.writeAction("slorii X16 X16 12 516")
    tran0.writeAction("slorii X16 X16 12 302")
    tran0.writeAction("movir X17 1516")
    tran0.writeAction("slorii X17 X17 12 3078")
    tran0.writeAction("slorii X17 X17 12 840")
    tran0.writeAction("slorii X17 X17 12 1660")
    tran0.writeAction("slorii X17 X17 12 971")
    tran0.writeAction("movir X18 35075")
    tran0.writeAction("slorii X18 X18 12 802")
    tran0.writeAction("slorii X18 X18 12 3311")
    tran0.writeAction("slorii X18 X18 12 2082")
    tran0.writeAction("slorii X18 X18 12 1578")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
