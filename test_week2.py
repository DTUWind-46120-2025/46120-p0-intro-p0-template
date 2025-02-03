"""Test your functions from Week 2 assignment.
"""
import pytest

import preclass_assignment.functions as fxn


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect



def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # given
    size = 139  # what is the size of the bed?
    # when
    fxn.goldilocks(size)  # call the function
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Too small!\n'  # check that the function printed what we expect


def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    inp = 30  # test input to function
    exp_out = [1, 1, 2, 3, 5, 8, 13, 21]  # expected output
    # when
    out = fxn.fibonacci_stop(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    inp_x = [-1, 2, 6, 95]  # test input to function, x
    inp_status = [1, 0, 0, 0]  # test input to function, status
    exp_out = [-999, 2, 6, 95]  # expected output
    # when
    out = fxn.clean_pitch(inp_x, inp_status)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


@pytest.mark.parametrize("size,text", [(139, 'Too small!'), (140, 'Just right. :)'), (150, 'Just right. :)'), (151, 'Too large!')])
def test_goldilocks_param(capsys, size, text):
    """Check goldilocks returns expected output for all sizes"""
    # when
    fxn.goldilocks(size)  # call the function
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == (text + '\n')  # check that the function printed what we expect
