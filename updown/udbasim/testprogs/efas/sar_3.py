from EFA_v2 import *
def sar_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -24947")
    tran0.writeAction("slorii X16 X16 12 1164")
    tran0.writeAction("slorii X16 X16 12 804")
    tran0.writeAction("slorii X16 X16 12 1796")
    tran0.writeAction("slorii X16 X16 12 246")
    tran0.writeAction("movir X17 23254")
    tran0.writeAction("slorii X17 X17 12 2535")
    tran0.writeAction("slorii X17 X17 12 2402")
    tran0.writeAction("slorii X17 X17 12 601")
    tran0.writeAction("slorii X17 X17 12 1501")
    tran0.writeAction("movir X18 -8210")
    tran0.writeAction("slorii X18 X18 12 1864")
    tran0.writeAction("slorii X18 X18 12 888")
    tran0.writeAction("slorii X18 X18 12 3544")
    tran0.writeAction("slorii X18 X18 12 2130")
    tran0.writeAction("sar X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
