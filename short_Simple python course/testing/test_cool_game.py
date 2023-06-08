# TDD - Test Driven Development

import unittest

import cool_game

class CoolgameFunctionsTest(unittest.TestCase):
  def test_greet(self):
    """greet() have to return 'how are you' if isEnemy == False"""
    self.assertEqual(cool_game.greet('Jack', False), 'Hello Jack, How are you?')
    
  def test_greet_enemy(self):
    """greet() have to return 'I wil l kill you, bastard!' if isEnemy == True"""
    self.assertEqual(cool_game.greet('Ivan', True),'Hello Ivan! I wil l kill you, bastard!')

  def test_eat_burgers(self):
    """eat_burgers() have to return 'Mmm, that was exellent!' if count <=3"""
    self.assertEqual(cool_game.eat_burgers(3), 'Mmm, that was excellent!')

  def test_eat_too_much_burgers(self):
    """eat_burgers() have return 'Oh, I overate!' if count >3"""
    self.assertEqual(cool_game.eat_burgers(4), 'Oh, I overate!')


  def test_can_batman_fly(self):
    """Batman fly test"""
    self.assertTrue(cool_game.can_fly('Batman'), 'Batman Have to be able to fly')

  def test_can_anyone_fly(self):
    self.assertEqual(cool_game.can_fly('Bob'), False)
    self.assertEqual(cool_game.can_fly('Stive'), False)
if __name__ == '__main__':
    unittest.main()
