# Brioche Factory TDD

## Unit test
Tests singular and unitary pieces of code.

## Integrates test
Tests code from end to end.

## TDD - Test Driven Development
Is is what it says it is.
you first write a test.
Then you code.
Code the minimum amount to pass the test.

## Basics of a test

Known inputs, and known outputs.
All you do is assertion.

Then you have testing frameworks that help you do this.

## Our factory know inputs and outputs

### make_bread
make a function that takes in two arguments.
It should make 'dough' when given water and flour and eggs.
inputs:
- water
- flour
- eggs

outputs:
- dough


### bake
inputs:
- Dough

Outputs:
- brioche

:)

### run_factory
As a user, i want to be able to run a factory function, give it flour, water and eggs and recieve brioche.

