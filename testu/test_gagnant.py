from noyau import *
import pytest

def test_coup_gagnant():
    # Stub
    def jeton_stub(joueur, posx, posy, depx, depy, grille):
        # Replace this stub with your logic or an actual implementation of the jeton function
        return 0

    # Test case 1: No winning move
    grille1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    joueur1 = 0
    i1, j1 = 2, 3
    assert not coup_gagnant(joueur1, i1, j1, grille1, jeton_stub)

    # Test case 2: Winning move in vertical direction
    grille2 = [
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    joueur2 = 1
    i2, j2 = 3, 0
    assert coup_gagnant(joueur2, i2, j2, grille2, jeton_stub)

    # Test case 3: Winning move in horizontal direction
    grille3 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    joueur3 = 1
    i3, j3 = 2, 2
    assert coup_gagnant(joueur3, i3, j3, grille3, jeton_stub)

# Run the tests
test_coup_gagnant()