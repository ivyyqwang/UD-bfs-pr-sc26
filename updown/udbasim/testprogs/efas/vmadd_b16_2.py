from EFA_v2 import *
def vmadd_b16_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3991, 39451, 25694, 21609, 25212, 52730, 26119, 59826, 26102, 54528, 35450, 53963, 8]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1350")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 1605")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 2465")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 249")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3739")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 1632")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 3295")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("slorii X17 X17 12 1575")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3372")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 2215")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 3408")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 1631")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("vmadd.b16 X19 X17 X18 8 ")
    tran0.writeAction("yieldt")
    return efa
