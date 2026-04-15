#!/opt/conda/bin/python3.10
#!/usr/bin/env python3.10
str_tab = "    "
efapath = "../testprogs/efas/"
progpath = "../tests/inst_unit_tests/"
import random, itertools
import enum
import os
max_int_64 = int('ffffffffffffffff', 16) -1
min_int_64 = -int('ffffffffffffffff', 16)
max_int_32 = int('ffffffff', 16) -1
min_int_32 = -int('ffffffff', 16)

max_int_16 = int('ffff', 16) -1
min_int_16 = -int('ffff', 16)

max_int_12 = int('fff', 16) -1
min_int_12 = -int('fff', 16)

max_int_4 = int('f', 16) -1
min_int_4 = -int('f', 16)

max_1_byte = int('ff', 16)
max_2_bytes = int('ffff', 16)
WAIT = False
local_bank_bound = 32*1024
class RetCase(enum.Enum):
    NORET = 0
    WRET = 1
    
class LaneCase(enum.Enum):
    SAMELANE = 0
    DIFFLANE = 1
    # INVALID_SINGLE_UD0 = 64
    # INVALID_SINGLE_UD1 = 100
    # INVALID_SINGLE_CL0 = 256

def genGSetUp(progs):
    setupTemplate = """

#include <gtest/gtest.h>
#include "basim.hh"
#include "types.hh"
#include "lanetypes.hh"
#include "udaccelerator.hh"
#include <iostream>
#include <cstdlib>

using namespace basim;

class {cinst} : public ::testing::Test {{
 protected:
    void SetUp() override {{
        m.NumLanes = numlanes;
        m.NumNodes = 1;
        m.NumUDs = 1;
        m.NumStacks = 1;
        m.LocalMemAddrMode = 1;
        sim = BASim(m);
    }}
    void testWait(BASim& sim,int nwid){{
        bool status;
        while(1){{
            status = true;

            uint64_t val;
            sim.ud2t_memcpy(&val, 8, NetworkID(nwid), 0);
            status = status && (val == 1);
            
            printf("{cinst} test is waiting...\\n");
            if(status) break;
        }}
        printf(".................Successfuly exit wait!.............\\n");
    }}
    BASim sim;
    machine_t m;
    int numlanes = 2;
    
}};

{gtests}
    """
    results = []
    for cinst in progs:
        prog = setupTemplate.format(cinst=cinst.capitalize(), numlanes=progs[cinst]["numlanes"], gtests=progs[cinst]['gtests'])
        results.append({"cinst": cinst, "prog": prog})
    return results

def genSendProg(gefas, progs={}):
    if not gefas:
        return gefas, progs

    testWait = "testWait(sim, {nwid});"
    
    gtestTemplate = """
TEST_F({cinst}, {fname}){{
    numlanes = {numlanes};
    m.NumLanes = {numlanes};
    sim = BASim(m);
    printf("numlanes: %d\\n", numlanes);
    sim.initMachine("testprogs/binaries/{binfname}", 0);
    sim.initMemoryArrays();
    word_t** memdata = new word_t*[numlanes];
    for(int i = 0; i < numlanes; i++){{
        memdata[i] = new word_t[32];
        for(int j = 0; j < 32; j++){{
            memdata[i][j] = (word_t) rand() % 100;
        }}
    }}
    int numops = 8;
    eventword_t ev(0);
    ev.setNumOperands(numops);
    ev.setThreadID(0xFF);
    ev.setNWIDbits(0);
    operands_t ops(numops);
    word_t* data = new word_t[numops];
    // set data based on the instruction
    {operands}
    ops.setData(data);
    for(int j = 0; j < numops; j++){{
        printf("data[%d] = %ld\\n", j, (long)data[j]);
        }}
    eventoperands_t evops(&ev, &ops);
    networkid_t nwid = NetworkID(0);
    sim.pushEventOperands(nwid, evops);
    sim.simulate();
    printf("\\n After simulation.................\\n");
    {testWait}
    word_t val;
    {expects} 
    printf("numlanes: %d\\n", numlanes);
    printf("memdata[0] = %lu\\n", (uint64_t)memdata[0]);
    for(int i = 0; i < numlanes; i++){{
        for(int j = 0; j < 8; j++){{
            word_t val;
            sim.ud2t_memcpy(&val, 8, NetworkID(i), 8 * (j+1));
            printf("nwid: %d, j = %d, val:  %lu\\n", i,j, val);
        }}
        for(int j = 0; j < 32; j++){{
            printf("memdata[%d][%d] = %lu, @ %lu\\n", i, j, memdata[i][j], (uint64_t)&memdata[i][j]);
            }}
        }}
    
}}
    """
    gtests = ""
    ii = 0
    # here we need a thorough boundray check tests
    for gefa in gefas:
        cinst = gefa["fname"].split("_")[0]
        numlanes = int(gefa["fname"].split("_")[3].split("lane")[1])
        wret = gefa["fname"].split("_")[2].split("ret")[1]
        nops = int(gefa["fname"].split("_")[4].split("nops")[1])
        if cinst not in progs:
            progs[cinst] = {"numlanes": numlanes, "gtests": ""}
        expected = gefa["expected"]
        nwid = expected["nwid"]
        fname = gefa["fname"]
        binfname = gefa["fname"] + ".bin"
        memdata = ""
        operands = ""
        expects = ""
        # TODO: maybe from here, we can iterate over boundary values
        # case 0: invalid nwid - add one case in genSend
        # case 1: invalid dram address - add one case here
        # case 2: invalid sp address
        # case 3: invalid event label
        gargs = {'memdata': []}
        for i in range(16):
            d = random.randint(0, max_int_64)
            gargs['memdata'].append(d)
            memdata += f"memdata[{i}] = {d};\n" + str_tab
        gXoffset = random.randint(0, local_bank_bound-128) >> 3 << 3 # TODO: can extend to generate illegal values
        

      
        # if cinst == "sendops" or cinst == "send" or cinst == "sendr":
        gargs['Xoffset'] = gXoffset
        gargs['OB0'] = gXoffset
        # OB_1 = Xd, this can only be verified in c
        gargs['OB2'] = gXoffset + 128
        # OB_0 = Xoffset
        operands += f"data[0] = {gargs['OB0']};\n" + str_tab
        # OB_1 = Xd, this cann only be verified in c
        operands += f"data[1] = reinterpret_cast<uint64_t>(&memdata[{expected['nwid']}][0]);\n" + str_tab 
        operands += f"data[2] = {gargs['OB2']};\n" + str_tab 
        # FIXME: OB_2 - OB_8 = rand, 0B_8 is actually X3??
        # else: # sendm*
        #     gargs['Xoffset'] = gXoffset
        #     gargs['OB1'] = gXoffset
        #     gargs['OB2'] = gXoffset + 128
        #     operands += f"data[0] = reinterpret_cast<uint64_t>(&memdata[{expected['nwid']}][0]);\n" + str_tab
        #     operands += f"data[1] = {gargs['OB1']};\n" + str_tab
        #     operands += f"data[2] = {gargs['OB2']};\n" + str_tab
            
        for i in range(5):
            OB = random.randint(0, max_int_64)
            gargs[f'OB{i+3}'] = OB
            operands += f"data[{i+3}] ={OB}u;\n" + str_tab
        
        str_offset = "offset"
        if cinst == "sendops" or cinst == "send" or cinst == "sendr" or cinst == "sendr3":
                # if lane==0 (same), ret==0 (noret), expect values in SP, starting from Xoffset
                # destionation nops could be from 3 to 8, it is a $imm so from efa
            # expected["dnops"] = 3  # FIXME: temporary for testing only
            for i in range(expected["dnops"]):
                if i == 1:
                    # now OB_1 is the address of the memdata
                    expects += f"sim.ud2t_memcpy(&val, 8, NetworkID({expected['nwid']}), {gXoffset + 16});\n" + str_tab
                    expects += f"EXPECT_EQ(val, (word_t) memdata[{expected['nwid']}]);\n" + str_tab
                    continue
                # first word is reserved for potential flag, may not used it anyways
                expects += f"sim.ud2t_memcpy(&val, 8, NetworkID({expected['nwid']}), {gXoffset + 8 * (i+1)});\n" + str_tab
                expects += f"EXPECT_EQ(val, {gargs[f'OB{i}']}u);\n" + str_tab

    
        if cinst == "sendmops"  or cinst == "sendm":
            if expected["mode0"] == 0:
                # load, data is loaded from memdata and store to starting from flag, len=nops
                for i in range(expected["dnops"]):
                    
                    expects += f"sim.ud2t_memcpy(&val, 8, NetworkID({nwid}), {8 * (i+1)});\n" + str_tab
                    expects += f"EXPECT_EQ(val, memdata[{nwid}][{i}]);\n" + str_tab
            else:
                # store, data is read from OBs and store to memdata, len=nops
                for i in range(expected["dnops"]):
                    
                    # expects += f"sim.ud2t_memcpy(&val, 8, NetworkID({expected['nwid']}), {8 * (i+1)});\n" + str_tab
                    expects += f"EXPECT_EQ(memdata[{nwid}][{i}], data[{i}]);\n" + str_tab
        
        if cinst == "sendmr" or cinst == "sendmr2":
            expects += f"sim.ud2t_memcpy(&val, 8, NetworkID({expected['nwid']}), 8);\n" + str_tab
            expects += f"EXPECT_EQ(memdata[{nwid}][0], {gargs[f'OB0']}u);\n" + str_tab
            if cinst == "sendmr2":
                expects += f"sim.ud2t_memcpy(&val, 8, NetworkID({expected['nwid']}), 16);\n" + str_tab
                expects += f"EXPECT_EQ(memdata[{nwid}][1], (word_t) memdata[{nwid}]);\n" + str_tab
            
        testWait = testWait.format(nwid=nwid)
        # FIXME: this is testonly
        # if cinst.startswith("sendm"):
        testWait = ""
        # if WAIT == False:
        #     testWait = ""
        # print(nwid, testWait)
        # FIXME: this is testonly   
        # expects = ""
        progs[cinst]['gtests'] += gtestTemplate.format(numlanes=numlanes,cinst=cinst.capitalize(), fname=fname+str(ii), binfname=binfname, memdata=memdata, operands=operands,testWait=testWait, expects=expects)
        ii +=1
    return gefas, progs
    
def genSendEFA(inst, nops, nlanes, mode1, mode0=None):
    # TODO: boundray check
    if inst.startswith("sendm") and mode0 is None:
        print("sendm* needs mode0")
        return
    
    match inst:
        case "sendops":
            if mode0 is not None:
                print("sendops does not support mode0(load/store)")
                return
            if not 1 <= nops <= 8:
                print("sendops only supports 1-8 operands")
                return
        case "send":
            if mode0 is not None:
                print("send does not support mode0(load/store)")
                return
            if not 1 <= nops <= 8:
                print("send only supports 2-9 operands")
                return
        # new_sendr: sendr default with 2 operands
        case "sendr":
            if mode0 is not None:
                print("sendr does not support mode0(load/store)")
                return
            if mode1 == 1:
                print("sendr only supportes contword!")
                return
            if nops!=2:
                print("sendr only supports 2 operands")
                return
        # new_sendr: sendr3 has 3 operands
        case "sendr3":
            if mode0 is not None:
                print("sendr3 does not support mode0(load/store)")
                return
            if mode1 == 1:
                print("sendr3 only supportes contword!")
                return
            if nops!=3:
                print("sendr3 only supports 3 operands")
                return
        # new_sendr: sendmr default has one operands
        case "sendmr":
            if mode0 != 1:
                print("sendmr only supports store")
                return
            if mode1 == 1:
                print("sendmr only supportes contword!")
                return
            if nops!=1:
                print("sendmr only supports 1 operand")
                return
        # new_sendr: sendmr2 has two operands
        case "sendmr2":
            if mode0 != 1:
                print("sendmr2 only supports store")
                return
            if mode1 == 1:
                print("sendmr2 only supportes contword!")
                return
            if nops!=2:
                print("sendmr2 only supports 2 operands")
                return
        case "sendmops":
            if mode0 != 1:
                print("sendmops only supports store")
                return
            if not 1 <= nops <= 8:
                print("sendmops only supports 1-8 operands")
                return
        case "sendm":
            if mode0 is None:
                print("sendm needs mode0(load/store)")
                return
            if not 1 <= nops <= 8:
                print("sendmops only supports 1-8 operands")
                return
 
    if nlanes > 2:
        nlanes = 2
    # nops >= 3 so sendr can work
    # mode1 is for cont event
    # mode1 = 1, auto send_wret, Xc is event_label
    # mode1 = 0, send_wret, Xc is event_word
    # when mode0 is not None, it is for sendm
    # mode0 = 0, load
    # mode0 = 1, store
    
    Xe = "X31"
    
    Xoffset = "X16" #pointer offset
    Xd = "X17"  #dram address
    X1 = "X18"
    Xoffset2 = "X18" # second pointer for later use
    X2 = "X19"
    X3 = "X20"
    X4 = "X21"
    X5 = "X22"
    X6 = "X23"
    
    
    Xptr = "X24"
    Xc = "X25"
    Xflag = "X30"
    template = """
from EFA_v2 import *
def {fname}():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {{
        "start_event": 0,
        "send_event": 1,
        "cont_event": 2,
        "dram_return": 3,
    }}
    tran0 = state.writeTransition("eventCarry", state, state, event_map['start_event'])

    """
    # for e0, always 8 OBs, starting from X8
    for i in range(8):
        template += f"tran0.writeAction(\"addi X{i+8} X{i+16} 0\")\n" + str_tab
    template += """
    tran0.writeAction("add X7 {Xoffset} {Xptr}") # local SP pointer, to read data from
    # update to the send event
    tran0.writeAction("evi X2 {Xe} 1 1")    # update event_label
    tran0.writeAction("evi {Xe} {Xe} 255 4") # update tid, new thread
    # construct Xc based on outside mode1
    {e1cont}
    # may or maynot write to SP
    {e0_writeSP}
    
    # send events after write to SP
    {send2e1}
    
    
    # may or maynot terminate
    {e0term}
    
    # only send* will use tran1
    tran1 = state.writeTransition("eventCarry", state, state, event_map['send_event'])
    # for sendr, obs are Xd, Xoffset, X1
    tran1.writeAction("addi X8 {Xoffset} 8") # first 8 bytes are for flag
    tran1.writeAction("movir {Xptr} 0") # reset Xptr
    tran1.writeAction("add X7 {Xoffset} {Xptr}") # starting from base + Xoffset
    # write data in the SP, depending on how may operands received
    {e1_writeSP}  
    # tran1 now can decide send_reply, send several values back
    {send_reply2e0}
    {e1term}
    
    tran2= state.writeTransition("eventCarry", state, state, event_map['cont_event'])
    tran2.writeAction("addi X8 {Xoffset} 8") # 
    tran2.writeAction("movir {Xptr} 0") # reset Xptr
    tran2.writeAction("add X7 {Xoffset} {Xptr}") # starting from base + Xoffset
    # get some values back, store them in SP
    {e2_writeSP}
    # for sure is yieldt
    {e2term} 
    
    # only sendm* will use tran3
    tran3 = state.writeTransition("eventCarry", state, state, event_map['dram_return'])
    tran3.writeAction("movir {Xptr} 8") # reset Xptr, now always starts from the base + 8
    {dr_writeSP} # always write to SP after the flag
    {drterm} # only run once, don't bother yield
    return efa
    """
        # writing data to e1's SP
    e1nops = nops
    # always write all the OBs to SP, starting from X8
    write_temp = ""
    # for i in range(e1nops):
    for i in range(e1nops): #FIXME: when set to constant, it is only for testing
        write_temp += f"tran{{t}}.writeAction(\"movrl X{i+8} 0({Xptr}) 1 8\")\n" + str_tab
    
    write_term = """
    # terminate and write termination flag to SP, Xbase[0] = flag
    tran{t}.writeAction("movir {Xflag} 1") # set flag to 1
    tran{t}.writeAction("addi X7 {Xptr} 0") # starting from base
    tran{t}.writeAction("movrl {Xflag} 0({Xptr}) 0 8") # write flag the beginning of the SP
    tran{t}.writeAction("yieldt") # for sure e1 will term
    """

    iyield ="tran{t}.writeAction(\"yield\")\n"
    iyieldt ="tran{t}.writeAction(\"yieldt\")\n"
    e1cont =""
    if mode1:
        # auto send_wret
        e1cont = f"# mode1==1, auto send_wret, Xc is the cont_label\n" + str_tab
        if inst.startswith("sendm"):
            e1cont += f"tran0.writeAction(\"evlb {Xc} 3\")\n" # label 3, dram_return
        else:
            e1cont += f"tran0.writeAction(\"evlb {Xc} 2\")\n" # label 2
        
    else:
        # send_wret
        e1cont = f"# mode1==0, send_wret, Xc is the cont_word\n" + str_tab
        if inst.startswith("sendm"):
            e1cont += f"tran0.writeAction(\"evi X2 {Xc} 3 1\") #sendm with contword\n"
        else:    
            e1cont += f"tran0.writeAction(\"evi X2 {Xc} 2 1\")\n"
    
    
    send2e1 = ""
    e0_writeSP = ""
    e0term = ""
    e1_writeSP = ""
    send_reply2e0 = ""
    e1term = ""
    e2_writeSP = ""
    e2term = ""
    drterm = ""
    dr_writeSP = ""
    fname = ""
    generated = []
    for rc in RetCase:
        for lc in LaneCase:
            # if lc == LaneCase.SAMELANE:
            #     continue
            expected = {}
            # only when no ret, and have two lanes, we expect the values in lane1 SP
            # the starting address of the values stored is the Xbase + Xoffset,
            expected["nwid"] = int(rc == RetCase.NORET and lc == LaneCase.DIFFLANE)
            # destination nops could be from 3 to 8
            expected["dnops"] = nops
            expected["mode0"] = mode0
            
            if nops > 8:
                expected["dnops"] = 8

            # new_sendr updates
            if inst == "sendr3":
                expected["dnops"] = 3            
            if inst == "sendr":
                expected["dnops"] = 2
            if inst == "sendmr2":
                expected["dnops"] = 2
            if inst == "sendmr":
                expected["dnops"] = 1
        
            expected["offset"] = 1 if inst != "sendr" else 2 # first Xd is not used
            
      
            if mode0 is None and inst.startswith("sendm"):
                # ignore sendm when no mode0 provided
                continue
            if mode1 == 1 and inst.startswith("sendm") and lc == LaneCase.DIFFLANE:
                # ignore sendm when it is contlable for different labes, it will never happen
                # print("sendm with contlabel cannot be in different lanes")
                continue
            # if lc == LaneCase.DIFFLANE:
            #     continue
            if rc == RetCase.WRET:
                continue
            # print(rc, lc)
            if rc == RetCase.NORET:
                # if no ret, then e1t1 will write flag to SP and terminate anyways
                # e0term = iyieldt.format(t=0)
                if lc == LaneCase.DIFFLANE:
                    e0term = write_term.format(t=0, Xptr=Xptr, Xflag=Xflag)
                else:
                    e0term = iyieldt.format(t=0)
                e1_writeSP = write_temp.format(t=1)
                e1term = write_term.format(t=1, Xflag=Xflag, Xptr=Xptr)
                send_reply2e0 = "\n"
                e2term = iyield.format(t=2)
            else:
                # if ret, let e2 write values and flag to SP
                e0term = iyield.format(t=0)
                e1term = iyield.format(t=1)
                send_reply2e0 = f"tran1.writeAction(\"evi X2 {Xc} 2 {0b0001}\") # construct cont word\n" + str_tab 
                send_reply2e0 += f"tran1.writeAction(\"evi X1 {Xe} 0 {0b0010}\")\n" + str_tab
                # send_reply2e0 += f"tran1.writeAction(\"evi {Xc} {Xc} {0b111111111111} {0b0100}\")\n" + str_tab
                # send_reply2e0 += f"tran1.writeAction(\"evi {Xc} {Xc} {0b011111111111} {0b1000}\")\n" + str_tab
                
                # new_sendr: update from sendr to sendr3
                send_reply2e0 += f"tran1.writeAction(\"sendr3 {Xe} {Xc} X8 X9 X10\")\n"       
                e2_writeSP = write_temp.format(t=2)
                e2term = write_term.format(t=2, Xptr=Xptr, Xflag=Xflag)
            # if it is sendm, ev0 and ev1 simply terminate
            if inst.startswith("sendm"):
                if mode1 == 0: # Xc is a cont_word
                    send2e1 = f"tran0.writeAction(\"evi {Xc} {Xc} {lc.value} {0b1000}\") # new lid update lid with lc.value\n" + str_tab
                    send2e1 += f"tran0.writeAction(\"evi {Xc} {Xc} 255 {0b0100}\") # new thread, cont_label will handle sendm*_wret \n" + str_tab
                    # send2e1 += f"tran0.writeAction(\"evi {Xc} {Xc} 3 {0b0001}\") # update label is 3, dram_return\n" + str_tab
                    e0term = iyieldt.format(t=0)
                else:
                    send2e1 = f"tran0.writeAction(\"evlb {Xc} 3\") # cont_label in Xc, 3\n" + str_tab
                    e0term = iyield.format(t=0)
                
            else:
                send2e1 = f"tran0.writeAction(\"evi {Xe} {Xe} {lc.value} 8\")\n" + str_tab
                
            drterm = write_term.format(t=3, Xflag=Xflag, Xptr=Xptr)
            
            match inst:
                # new_sendr: sendr3 has 3 operands
                case "sendr3":
                    # here Xd Xptr X1 are simply X1 X2 X3
                    send2e1 += f"tran0.writeAction(\"sendr3 {Xe} {Xc} {Xoffset} {Xd} {X1}\")\n"
                # new_sendr: sendr is default with 2 operands
                case "sendr":
                    # here Xd Xptr are simply X1 X2
                    send2e1 += f"tran0.writeAction(\"sendr {Xe} {Xc} {Xoffset} {Xd}\")\n"
                case "sendops":
                    # if nops == 9:
                    #     send2e1 += f"tran0.writeAction(\"sendops {Xe} {Xc} X3 1 {mode1}\")\n"
                    # else:
                    send2e1 += f"tran0.writeAction(\"sendops {Xe} {Xc} X8 {nops} {mode1}\")\n"
                case "send":
                    e0_writeSP += f"tran0.writeAction(\"movir {Xptr} 0\") # reset Xptr\n" + str_tab
                    e0_writeSP += f"tran0.writeAction(\"add X7 {Xoffset2} {Xptr}\")\n" + str_tab
                    e0_writeSP += write_temp.format(t=0) + "\n" + str_tab
                    e0_writeSP += f"tran0.writeAction(\"movir {Xptr} 0\") # reset Xptr after send\n" + str_tab
                    e0_writeSP += f"tran0.writeAction(\"add X7 {Xoffset2} {Xptr}\")\n"+ str_tab 
                    # if nops == 9:
                    #     send2e1 += f"tran0.writeAction(\"send {Xe} {Xc} X3 1 {mode1}\")\n"                         
                    # else:
                    send2e1 += f"tran0.writeAction(\"send {Xe} {Xc} {Xptr} {nops} {mode1}\")\n"

                
                # for sendm, only Xd, Xc, (Xptr, Xop, X1), ($len, X2), $mode[1, 0]
                case "sendm":
                    # we don't care about whether it is RET or NORET, load, store always has RET.
                    if rc == RetCase.WRET:
                        # print("")
                        continue
                    # load, Xc is determinted (e2), no need to worry about
                    # when store, data is read from Xptr, len, then store to Xd, write ack does nothing, but a flag will be written to SP
                    send2e1 += f"tran0.writeAction(\"sendm {Xd} {Xc} {Xptr} {nops} {2 * mode1 + mode0}\")\n"
                    if mode0 == 1:
                        # when store, discard the ack, check the dram value, starting from Xd, nops
                        e0_writeSP += f"tran0.writeAction(\"movir {Xptr} 0\") # reset Xptr\n" + str_tab
                        e0_writeSP += f"tran0.writeAction(\"add X7 {Xoffset2} {Xptr}\")\n" + str_tab
                        e0_writeSP += write_temp.format(t=0) + "\n" + str_tab
                        e0_writeSP += f"tran0.writeAction(\"movir {Xptr} 0\") # reset Xptr after send\n" + str_tab
                        e0_writeSP += f"tran0.writeAction(\"add X7 {Xoffset2} {Xptr}\")\n"+ str_tab   
                        # e0term = iyieldt.format(t=0)
                        dr_writeSP = ""
                        # e1_writeSP = ""
                        # send_reply2e0 = ""
                        # e1term = write_term.format(t=1, Xflag=Xflag, Xptr=Xptr)
                    else:
                        # e0term = iyieldt.format(t=0)
                        # dr_writeSP = ""
                        dr_writeSP = f"# Xptr is reset to 8, for sendm write_return, static address starting from 8\n" + str_tab
                        dr_writeSP += f"tran3.writeAction(\"add X7 {Xptr} {Xptr}\")\n" + str_tab
                        dr_writeSP += write_temp.format(t=3)
                        
                        # e1_writeSP = write_temp.format(t=1)
                        # send_reply2e0 = ""
                        # e1term = write_term.format(t=1, Xflag=Xflag, Xptr=Xptr)
                        
                    # load, e2 will write nops to SP, starting from Xoffset
                case "sendmops":
                    # only store supported
                    if mode0 == 1:
                        # write ack, data in OBs written to Xd
                        send2e1 = f"tran0.writeAction(\"sendmops {Xd} {Xc} X8 {nops} {mode1}\")\n"
                        e0term = iyieldt.format(t=0)
                        dr_writeSP = ""
                        # e1_writeSP = ""
                        # send_reply2e0 = ""
                        # e1term = write_term.format(t=1, Xflag=Xflag, Xptr=Xptr)
                        # check the dram value
                    else:
                        continue
                # new_sendr: sendmr2 has two operands
                case "sendmr2":
                    # when mode0==0, load, data is loaded from Xd to OBs by ev1
                    if mode0 == 1:
                        # write ack, data in regs written to Xd
                        send2e1 = f"tran0.writeAction(\"sendmr2 {Xd} {Xc} {Xoffset} {Xd}\")\n"
                        e0term = iyieldt.format(t=0)
                        dr_writeSP = ""
                        # e1_writeSP = write_temp.format(t=1)
                        # send_reply2e0 = ""
                        # e1term = write_term.format(t=1, Xflag=Xflag, Xptr=Xptr)
                        # # check the dram value 
                    else:
                        continue
                # new_sendr: sendmr default has one operand
                case "sendmr":
                    # when mode0==0, load, data is loaded from Xd to OBs by ev1
                    if mode0 == 1:
                        # write ack, data in regs written to Xd
                        send2e1 = f"tran0.writeAction(\"sendmr {Xd} {Xc} {Xoffset}\")\n"
                        e0term = iyieldt.format(t=0)
                        dr_writeSP = ""
                        # e1_writeSP = write_temp.format(t=1)
                        # send_reply2e0 = ""
                        # e1term = write_term.format(t=1, Xflag=Xflag, Xptr=Xptr)
                        # # check the dram value 
                    else:
                        continue
            if mode1:
                m1 = "cl"
            else:
                m1 = "cw"
            fname = f"{inst}_{m1}_ret{rc.value}_lane{lc.value+1}_nops{nops}"
            if mode0 is not None and inst.startswith("sendm"):
                if mode0 == 0:
                    fname += f"_load"
                else:
                    fname += f"_store"
            r = template.format(fname=fname, Xoffset=Xoffset, Xptr=Xptr, Xe=Xe,
                                e1cont=e1cont, send2e1=send2e1, e0_writeSP=e0_writeSP, e0term=e0term,
                                e1_writeSP=e1_writeSP, send_reply2e0=send_reply2e0, e1term=e1term,
                                e2_writeSP=e2_writeSP, e2term=e2term,
                                dr_writeSP=dr_writeSP, drterm=drterm
                                    )
            generated.append({"fname": fname, "efa": r, "expected": expected})
                                             
    return generated



def dumpToFile(gefas, results,  efapath, progpath):
    efa_dir = os.path.join(os.getcwd(), efapath)
    prog_dir = os.path.join(os.getcwd(), progpath)
    for gefa in gefas:
        fname = gefa["fname"] + ".py"
        with open(os.path.join(efa_dir, fname), "w") as f:
            f.write(gefa["efa"])
    for result in results:
        print(result["cinst"])
        cinst = result["cinst"]
        fname = cinst + "_test.cpp"
        with open(os.path.join(prog_dir, fname), "w") as f:
            f.write(result["prog"])
    print(efa_dir, prog_dir)


sends = ["sendr", "sendops", "send", "sendm", "sendmops", "sendmr", "sendmr2", "sendr3"]
# sends = ["sendr", "sendr3", "sendmr", "sendmr2"]
# sends = ["sendm"]
# sends = ["sendr", "sendops", "send", "sendmr"]
# sends = ["sendops", "send"]
# sends=["sendm"]
# sends = ["send"]
# sends=["sendmops", "sendops"]
# sends = ["sendmr"]
# sends = ["sendr"]
# sends = ["sendr", "sendops", "send"]
# sends = ["sendmops", "sendmr"]
# numops = [1,2,3, 4,5,6,7, 8]
numops = [1, 2, 3, 4, 5, 6, 7, 8] # for sendr and sendmr
mode1s= [0, 1]
mode0s = [0, 1, None]
# numops = [4, 8]

# numops=[2]
# mode1s = [1] # 1 for contlabel, 0 for contword
# mode0s = [1] # 1 for store, 0 for load
progs = {}
gefass = []
results = []
already_sent = False
already_sentm = False
for c in itertools.product(sends, numops, mode1s, mode0s):
    print(c)
    gefas, _ = genSendProg(genSendEFA(c[0], c[1], 2, c[2], c[3]), progs)
    if gefas:
        # print(c)
        gefass.extend(gefas)
results = genGSetUp(progs)


dumpToFile(gefass, results, efapath, progpath)

# print(progs)
   
    # dumpToFile(gefas, progs, efapath, progpath)
# gefas, progs = genSendProg(genSendEFA("sendr", 8, 0, 1))
# dumpToFile(gefas, progs, efapath, progpath)