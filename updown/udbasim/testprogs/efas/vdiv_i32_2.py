from EFA_v2 import *
def vdiv_i32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-487183571, 172776407, -2010778401, -145020537, -194138048, -1717531998, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 164")
    tran0.writeAction("slorii X19 X19 12 3163")
    tran0.writeAction("slorii X19 X19 8 215")
    tran0.writeAction("slorii X19 X19 12 3631")
    tran0.writeAction("slorii X19 X19 12 1579")
    tran0.writeAction("slorii X19 X19 8 45")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3957")
    tran0.writeAction("slorii X17 X17 12 2857")
    tran0.writeAction("slorii X17 X17 8 135")
    tran0.writeAction("slorii X17 X17 12 2178")
    tran0.writeAction("slorii X17 X17 12 1524")
    tran0.writeAction("slorii X17 X17 8 223")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2458")
    tran0.writeAction("slorii X18 X18 12 138")
    tran0.writeAction("slorii X18 X18 8 162")
    tran0.writeAction("slorii X18 X18 12 3910")
    tran0.writeAction("slorii X18 X18 12 3504")
    tran0.writeAction("slorii X18 X18 8 64")
    tran0.writeAction("vdiv.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
