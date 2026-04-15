#include "simupdown.h"
#include "updown.h"

int main(int argc, char *argv[]){
	UpDown::ud_machine_t machine;
	machine.NumLanes = 64;
	machine.NumUDs = 1;
	machine.NumStacks = 1;
	machine.NumNodes = 1;
	machine.LocalMemAddrMode = 0;
	printf("Before creating runtime\n");

#ifdef GEM5_MODE
	UpDown::UDRuntime_t *rt = new UpDown::UDRuntime_t(machine);
#else
	char dir[100] = "efas/";
	strcat(dir, argv[1]);
	printf("%s\n", dir);
	UpDown::SimUDRuntime_t *rt = new UpDown::SimUDRuntime_t(machine,
		argv[1],
		"main", 
		"./", 
		UpDown::EmulatorLogLevel::FULL_TRACE);
#endif
	printf("After creating runtime\n");
	UpDown::networkid_t nwid(0, 0);
	UpDown::word_t ops_data[5];
	UpDown::operands_t ops(5, ops_data);
    // should be random values, 5 values
    // Xc, Xptr, X1, X2, X3
	ops.set_operand(0, 0);
	ops.set_operand(1, 0);
	ops.set_operand(2, 8);
	ops.set_operand(3, 16);
	ops.set_operand(4, 24);

	UpDown::word_t data = 0;
	rt->t2ud_memcpy(&data, 8, nwid,0);

	UpDown::event_t evnt_ops = UpDown::event_t(0,nwid,UpDown::CREATE_THREAD,&ops);
	rt->send_event(evnt_ops);
	rt->start_exec(nwid);

	return 0;
}

bool startsWith(const char *pre, const char *str)
{
    size_t lenpre = strlen(pre),
           lenstr = strlen(str);
    return lenstr < lenpre ? false : memcmp(pre, str, lenpre) == 0;
}
