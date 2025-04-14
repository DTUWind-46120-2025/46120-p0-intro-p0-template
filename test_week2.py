"""Test your functions from Week 2 assignment.
"""
import preclass_assignment.functions as fxn

def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.printing_word(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world\n'  # check that the greeting was what we expect



def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # given
    test_cases = [(139, 'Too small!!'),
                  (140, 'Just right :)'),
                  (150, 'Just right :)'),
                  (151, 'Too big!!')]
    # when
    for length, message in test_cases:
        fxn.length_bed(length)  # actual output
        captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
        assert captured.out.strip() == message 


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
    inp = 30 # test input to function
    exp_out = [1, 1, 2, 3, 5, 8, 13, 21]  # expected output
    # when
    out = fxn.fibonacci_stop(inp)
    # then
    assert exp_out == out 


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    inp_angles = [-1, 2, 6, 95]  # test input to function
    inp_status = [1, 0, 0, 0]  # test input to function
    exp_out = [-999, 2, 6, 95]
    # when
    out = fxn.clean_pitch(inp_angles, inp_status)  # actual output
    # then
    assert  exp_out == out #Update the contents of this function so it correctly tests clean_pitch
