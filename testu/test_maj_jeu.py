from noyau import *
import pytest

def test_maj_jeu():
    grille = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
    ]
    niveau = [5, 5, 5, 5, 5, 5, 5]
    joueur = 0

# Test avec un coup valide
    case = "C3"
    result = maj_jeu(case, grille, niveau, joueur)
    assert result == (5, 3)  # La dernière case remplie devrait être (5, 3)

    