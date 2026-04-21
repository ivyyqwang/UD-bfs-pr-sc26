# -*- Makefile -*-
# Copyright 2010-2011,  Georgia Institute of Technology, USA.
# See COPYING for license.
BUILD_OPENMP = Yes
BUILD_XMT = No
CC = gcc
CFLAGS = -O2 -fopenmp -g

SRCS_COMMON = xalloc.c timer.c splittable_mrg.c utils.c
OBJS_COMMON = $(SRCS_COMMON:.c=.o)

.PHONY: all clean

all: preprocess

preprocess: preprocess.o $(OBJS_COMMON)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -MMD -c $< -o $@

-include $(SRCS_COMMON:.c=.d) preprocess.d

clean:
	rm -f *.o *.d preprocess


