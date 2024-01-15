from noyau import changer_joueur
import pytest

def test_changer_joueur():
    assert(changer_joueur(0)) == (1)
    assert(changer_joueur(1)) == (0)
    