import unittest
from Diamond.diamond import diamond

class TestDiamond(unittest.TestCase):
    def test_valeur_minim(self):
        result = diamond('A')
        self.assertEqual(result.strip(), 'A')

    def test_valeur_maxim(self):
        result = diamond('Z')
        expected_result = '''
                         A
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
                         A
        '''
        self.assertEqual(result.strip(), expected_result.strip())

    def test_valeur_exemple(self):
        result = diamond('C')
        expected_result = '''
  A
 B B
C   C
 B B
  A
        '''
        self.assertEqual(result.strip(), expected_result.strip())

    def test_valeur_minuscule(self):
        result = diamond('a')
        self.assertEqual(result.strip(), 'A')

if __name__ == '__main__':
    unittest.main()
