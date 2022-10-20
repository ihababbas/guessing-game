
import pytest

from guessing_game.game import GuessingGame



def test_player_name():
    player = GuessingGame('ibrahim')
    actual = player.player
    expected = "ibrahim"
    assert actual == expected


def test_random_num():
    player=GuessingGame('ehab')
    actual=player.number
    excepted=actual > 0 and actual <21
    assert excepted

def test_game_score():

    player=GuessingGame('ehab')
    actual=player.score
    excepted=0
    assert excepted == actual


def test_guessed_num():

    player=GuessingGame('ehab')
    player.guessed_number=10
    actual=player.guessed_number
    excepted=10
    assert excepted == actual

def test_input_1():
    player =GuessingGame('salem')
    player.guessed_number=10
    player.number=10
    actual=player.guess_number()
    
    excepted =print('congrats ! , You win the number is 10 and your score is : 10 ')

    assert excepted == actual

def test_input_2():
    player =GuessingGame('hani')
    player.guessed_number=10
    player.number=11
    actual=player.guess_number()
    excepted =  print(f'your guess too low , 4 rounds left')  

    assert excepted == actual


def test_score():
    player =GuessingGame('ibarhim')
    player.guessed_number=10
    player.number=10
    player.guess_number()
    actual=player.display_score()
    print(actual)
    excepted =  print(f' Name : {player.player} | Score : 10')  

    assert excepted == actual


