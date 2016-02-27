# The E++ Compiler

A compiler that converts E++ source code into E100 assembly code! :D

#### The Hell is E100?

The E100 is part of the "Microprocessors and Toys" section of "Engineering 100," the first-year engineering course at the Universty of Michigan. In this section, students learn the basics of computer engineering and implement a simple microprocessor (called the E100) on the [Altera DE2 FPGA Development Board](http://wl.altera.com/education/univ/materials/boards/de2/unv-de2-board.html).

The E100 has a simple Instruction Set Architecture. Using it, the students write E100 assembly code (E100 asm) programs to make their toys functional.

#### Okay, but what is E++?

E++ is a simple programming language I invented that is loosely based on C++. I chose to base the language on C++ because the University of Michigan's Computer Science curriculum teaches C++. That way, other University of Michigan students could easily use it.

## Installation

This program requires that you have [Python](https://python.org) installed on your computer.

To install the E++ compiler, open up your Terminal and enter this command:

```
$ pip install e++
```

**Pro-Tip:** Don't be a noob. You don't actually type the `$`

## Usage

The E++ compiler works similarly to the g++ compiler:

```
$ e++ test_program.epp -o test_program_assembly.e
```

This command will compile the E++ source code from `test_program.epp` into the E100 assembly file `test_program_assembly.e`.
