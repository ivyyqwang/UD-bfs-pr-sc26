from EFA_v2 import *

def multi_efa():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)

    state0 = State()
    state0.alphabet = [0-255]
    efa.add_state(state0)

    state1 = State()
    state1.alphabet = [0-255]
    efa.add_state(state1)

    state2 = State()
    state2.alphabet = [0-255]
    efa.add_state(state2)

    state3 = State()
    state3.alphabet = [0-255]
    efa.add_state(state3)

    #state4 = State()
    #state4.alphabet = [0-255]
    #efa.add_state(state4)

    event_map = {
        'init_lm':              0,
        'data_recieved':        1,
        'TFORM_procedure0':        2,
        'TFORM_procedure1':        3,
        'TFORM_return':        4
    }
    tran0 = state.writeTransition("eventCarry", state, state, 0)
    tran0.writeAction("movir X16 10")
    tran0.writeAction("yieldt")

    tran0 = state.writeTransition("commonCarry_with_action", state, state0, 1)
    tran0.writeAction("or X29 X27 X29")

    tran0 = state0.writeTransition("commonCarry_with_action", state0, state0, 0)
    tran0.writeAction("add X6 X7 UDPR_14")
    tran0.writeAction("beq X16 X30 test")

    tran = state.writeTransition("commonCarry_with_action", state, state1, 2)
    tran.writeAction("add X6 X7 UDPR_14")

    tran0 = state1.writeTransition("commonCarry_with_action", state1, state2, 0)
    tran0.writeAction("add X6 X7 UDPR_14")

    tran0 = state2.writeTransition("commonCarry_with_action", state2, state3, 0)
    tran0.writeAction("sub X6 X7 UDPR_14")

    tran0 = state3.writeTransition("commonCarry_with_action", state3, state3, 0)
    tran0.writeAction("add X6 X7 UDPR_14")

    efa.appendBlockAction("test","sub X31 X10 X31")
    efa.appendBlockAction("test","yieldt")

    efa.appendBlockAction("end_of_input_terminate_efa1","sub X31 X10 X31")
    efa.appendBlockAction("end_of_input_terminate_efa1","yieldt")

    efa.linkBlocktoState("end_of_input_terminate_efa1",state2)
    efa.linkBlocktoState("end_of_input_terminate_efa1",state0)
    return efa
