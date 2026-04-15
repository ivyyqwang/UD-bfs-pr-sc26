from EFA_v2 import *
def fmadd_64_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [579400735425314601, 1716883316150067216, 539844460073097990]
    tran0.writeAction("movir X16 2058")
    tran0.writeAction("slorii X16 X16 12 1822")
    tran0.writeAction("slorii X16 X16 12 1577")
    tran0.writeAction("slorii X16 X16 12 2563")
    tran0.writeAction("slorii X16 X16 12 3881")
    tran0.writeAction("movir X17 6099")
    tran0.writeAction("slorii X17 X17 12 2436")
    tran0.writeAction("slorii X17 X17 12 1939")
    tran0.writeAction("slorii X17 X17 12 3766")
    tran0.writeAction("slorii X17 X17 12 16")
    tran0.writeAction("movir X18 1917")
    tran0.writeAction("slorii X18 X18 12 3738")
    tran0.writeAction("slorii X18 X18 12 3356")
    tran0.writeAction("slorii X18 X18 12 2537")
    tran0.writeAction("slorii X18 X18 12 2822")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
