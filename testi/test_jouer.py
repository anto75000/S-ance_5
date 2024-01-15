from noyau import jouer
import pytest

def test_coup_gagnant_false(self, changer_joueur_mock, coup_gagnant_mock):
        # Configurer les mocks
        coup_gagnant_mock.return_value = False
        changer_joueur_mock.return_value = 1  # Supposons que changer_joueur renvoie 1 dans ce cas

        # Définir les variables globales
        global joueur
        global rang
        global grille
        global niveau
        global etat

        joueur = self.joueur_stub
        rang = self.rang_stub
        grille = self.grille_stub
        niveau = self.niveau_stub
        etat = self.etat_stub

        # Appeler la fonction jouer
        jouer("B4", self.gbouton_stub, self.message_stub)

        # Vérifier que le message et l'état ont été mis à jour correctement
        changer_joueur_mock.assert_called_once_with(self.rang_stub)
        self.message_stub.config.assert_called_once_with(text="A toi " + str(self.joueur_stub[1]))