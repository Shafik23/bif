#!/bin/python
import sys


class Bif:
    def __init__(self):
        self.tape = [0] * 10000     # pre-allocate a finite-size tape (sorry Alan Turing)
        self.data_pointer = 0
        self.instruction_pointer = 0

    def interpret(self, program):
        '''Interprets a Brainfuck program. This function does not return anything.'''

        # print("Program is %s" % program)
        # print

        # Remove all whitespace, since it's meaningless in Brainfuck
        program = "".join(program.split())

        while self.instruction_pointer < len(program):
            c = program[self.instruction_pointer]

            if c == '<':
                self.data_pointer = self.data_pointer - 1
            elif c == '>':
                self.data_pointer = self.data_pointer + 1
            elif c == '+':
                self.tape[self.data_pointer] = self.tape[self.data_pointer] + 1
            elif c == '-':
                self.tape[self.data_pointer] = self.tape[self.data_pointer] - 1
            elif c == '.':
                sys.stdout.write(chr(self.tape[self.data_pointer]))
                sys.stdout.flush()
            elif c == ',':
                self.tape[self.data_pointer] = sys.stdin.read(1)
                sys.stdin.flush()
            elif c == '[':
                if self.tape[self.data_pointer] == 0:
                    self.jump_to_matching_bracket(program, ']')
            elif c == ']':
                if self.tape[self.data_pointer] != 0:
                    self.jump_to_matching_bracket(program, '[')
            else:
                raise SyntaxError("Unrecognized BrainFuck Token: %s" % c)

            self.instruction_pointer = self.instruction_pointer + 1

    def jump_to_matching_bracket(self, program, bracket):
        '''Given a program, advances the instruction pointer to the next given bracket,
           going either forwards or backwards depending on bracket orientation (left vs. right).'''

        if bracket == ']':
            inc = 1
            opposite = '['
        else:
            inc = -1
            opposite = ']'

        stack = []
        self.instruction_pointer = self.instruction_pointer + inc

        while (self.instruction_pointer >= 0 and
               self.instruction_pointer < len(program)):
            if program[self.instruction_pointer] == opposite:
                stack.append(program[self.instruction_pointer])
            if program[self.instruction_pointer] == bracket:
                if len(stack) == 0:
                    return  # success - found the bracket
                else:
                    stack.pop()

            self.instruction_pointer = self.instruction_pointer + inc

        # Outside the loop - could not find bracket
        raise SyntaxError("Could not match %s" % opposite)


if __name__ == "__main__":
    # Bif().interpret(",>, >, <<.>    .>.")
    # Bif().interpret("++++[[[[.-]]]]")

    # Hello World!
    Bif().interpret("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
