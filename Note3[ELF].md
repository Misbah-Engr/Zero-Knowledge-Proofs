## Background
I started grounding my learning with the study of Succint Project as you could see. I will quote them on what Succint is.

> SP1 is a performant, open-source zero-knowledge virtual machine (zkVM) that verifies the execution of arbitrary Rust (or any LLVM-compiled language) programs.
> SP1 has undergone multiple audits from leading ZK security firms and is currently used in production by many top blockchain teams.

Do not hold me liable to what I quote.

I read all through their whitepaper and the project is interesting.

## Today

Today I started reading the code line by line. The goal is, going forward, I will read all of the project code.

Today, I was in `sp1/crates/core/executor/src/disassembler/elf.rs`

This file introduced me to an alien thing.
ELF (Executable and Linkable Format) file. 
The Elf.rs. It is designed to be the interface between the ZKVM and the users. You supply an ELF file, and the elf.rs instructions decode it and the provers and verifiers do their job.

## So, what is ELF (Executable and Linkable Format) file?

Gemini from Google Search: It is a standard file format used for storing executable programs, object files, and shared libraries on Linux and other Unix-like operating systems. 

Wikipedia: In computing, the Executable and Linkable Format (ELF, formerly named Extensible Linking Format) is a common standard file format for executable files, object code, shared libraries, and core dumps.

## In Summary
you compile high-level Rust → LLVM → RISC-V → ELF binary.

This ELF struct loads the binary, extracts the program, and sets up memory + PC state so the zkVM can simulate execution and generate a ZK proof of correct computation.
