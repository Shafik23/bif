#!/bin/python

import sys


TAPE_SIZE = 10   # Alas, the turing machine tape is not infinite in size
tape = [0] * TAPE_SIZE
data_pointer = 0
instruction_pointer = 0


def interpret(program):
    global tape
    global data_pointer
    global instruction_pointer

    # Remove all whitespace, since it's meaningless in Brainfuck
    program = "".join(program.split())

    while instruction_pointer < len(program):
        c = program[instruction_pointer]
        # print(tape, c, data_pointer)

        if c == '<':
            data_pointer = data_pointer - 1
        elif c == '>':
            data_pointer = data_pointer + 1
        elif c == '+':
            tape[data_pointer] = tape[data_pointer] + 1
        elif c == '-':
            tape[data_pointer] = tape[data_pointer] - 1
        elif c == '.':
            print(tape[data_pointer]),
        elif c == ',':
            tape[data_pointer] = sys.stdin.read(1)
        elif c == '[':
            if tape[data_pointer] == 0:
                jump_to_matching_bracket(']')
                continue
        elif c == ']':
            if tape[data_pointer] != 0:
                jump_to_matching_bracket('[')
                continue
        else:
            raise SyntaxError("Unrecognized BrainFuck Token: %s" % c)

        instruction_pointer = instruction_pointer + 1


def jump_to_matching_bracket(bracket):
    pass


print(interpret(",>, >, <<.>    .>."))
