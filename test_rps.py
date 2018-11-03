import rps
import pytest
import subprocess
import sys

def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True # miesto is je možné použiť == (v tomto prípade, inak to nie je to isté)

def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True

def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True

def test_lizard_is_invalid_play():
    assert rps.is_valid_play('lizard') is False

def test_spongebob_is_invalid_play():
    assert rps.is_valid_play('spongebob') is False

def test_computer_play_is_valid():
    for _ in range(5000):
        play = rps.generate_computer_play()
        assert rps.is_valid_play(play)

def test_computer_plays_randomly():
    plays = [rps.generate_computer_play() for _ in range(5000)]
    rocks = plays.count('rock')
    papers = plays.count('paper')
    scissors = plays.count('scissors')
    print(rocks, papers, scissors) # ak testy prechadzaju, nic nevyprintuje, ak failnu, tak to vypise
    assert rocks > 200
    assert papers > 200
    assert scissors > 200

def test_paper_beats_rock():
    result = rps.evaluate_game('paper', 'rock')
    assert result == 'human'

def test_paper_beats_rock2():
    result = rps.evaluate_game('rock', 'paper')
    assert result == 'computer'

def test_rock_beats_scissors():
    result = rps.evaluate_game('scissors', 'rock')
    assert result == 'computer'

def test_rock_beats_scissors2():
    result = rps.evaluate_game('rock', 'scissors')
    assert result == 'human'

def test_scissors_beats_paper():
    result = rps.evaluate_game('scissors', 'paper')
    assert result == 'human'

def test_scissors_beats_paper2():
    result = rps.evaluate_game('paper', 'scissors')
    assert result == 'computer'

def test_paper_and_paper_is_a_tie():
    result = rps.evaluate_game('paper', 'paper')
    assert result == 'tie'

def test_rock_and_rock_is_a_tie():
    result = rps.evaluate_game('rock', 'rock')
    assert result == 'tie'

def test_scissors_and_scissors_is_a_tie():
    result = rps.evaluate_game('scissors', 'scissors')
    assert result == 'tie'


def input_faked_rock(prompt):
    print(prompt)
    return 'rock'

def test_full_game(capsys):
    rps.main(input=input_faked_rock)
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out

def input_faked_paper(prompt):
    print(prompt)
    return 'paper'

def test_full_game_paper(capsys):
    rps.main(input = input_faked_paper)
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out

def input_faked_scissors(prompt):
    print(prompt)
    return 'scissors'

def test_full_game_scissors(capsys):
    rps.main(input = input_faked_scissors)
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out
"""
def test_full_game(capsys, monkeypatch):        # monkeypatch platí iba v rámci jedného testu
    monkeypatch.setattr('builtins.input', input_faked_rock)
    rps.main()
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out

def input_faked_paper(prompt):
    print(prompt)
    return 'paper'

def test_full_game_paper(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', input_faked_paper)
    rps.main()
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out

def input_faked_scissors(prompt):
    print(prompt)
    return('scissors')

def test_full_game_scissors(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', input_faked_scissors)
    rps.main()
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out

@pytest.fixture
def fake_input_rock(monkeypatch):
    monkeypatch.setattr('builtins.input', input_faked_rock)

def test_full_game(capsys, fake_input_rock):
    rps.main()
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out
"""


def test_wrong_play_results_in_repeated_question():
    cp = subprocess.run(['python', 'rps.py'], encoding='cp1250', stdout=subprocess.PIPE)
    assert cp.stdout.count('rock, paper, or scissors?') == 1

def test_wrong_play_results_in_repeated_question():
    cp = subprocess.run([sys.executable, 'rps.py'], encoding='cp1250', stdout=subprocess.PIPE, input='dragon\nrock\n', check=True)
    assert cp.stdout.count('rock, paper, or scissors?') == 2
# teraz som si istá, že sa spúšťa ten python, ktorý chcem
