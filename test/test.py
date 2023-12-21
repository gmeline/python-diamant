import unittest
from diamond import diamond

class TestDiamond (unittest.TestCase):
  def test_valeur_minim(self):
    result = diamond('A')
    self.assertEqual(result,'A')

  def test_valeur_minim(self):
    result = diamond('Z')
    self.assertEqual(result,'                         A
                        B B
                       C   C
                      D     D
                     E       E
                    F         F
                   G           G
                  H             H
                 I               I
                J                 J
               K                   K
              L                     L
             M                       M
            N                         N
           O                           O
          P                             P
         Q                               Q
        R                                 R
       S                                   S
      T                                     T
     U                                       U
    V                                         V
   W                                           W
  X                                             X
 Y                                               Y
Z                                                 Z
 Y                                               Y
  X                                             X
   W                                           W
    V                                         V
     U                                       U
      T                                     T
       S                                   S
        R                                 R
         Q                               Q
          P                             P
           O                           O
            N                         N
             M                       M
              L                     L
               K                   K
                J                 J
                 I               I
                  H             H
                   G           G
                    F         F
                     E       E
                      D     D
                       C   C
                        B B
                         A')
    def test_valeur_exemple(self):
    result = diamond('C')
    self.assertEqual(result,'  A
 B B
C   C
 B B
  A')
    def test_valeur_minuscule(self):
    result = diamond('a')
    self.assertEqual(result,'A')
