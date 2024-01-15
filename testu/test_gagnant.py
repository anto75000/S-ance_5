from noyau import *
import pytest

def test_gagnant():
    # Stub
    def jeton_stub(joueur, posx, posy, depx, depy, grille):
        
        return 0

    
    # Test 1: gagnant à la verticale
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
    assert coup_gagnant(joueur2, i2, j2, grille2)

    
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
    assert coup_gagnant(joueur3, i3, j3, grille3)