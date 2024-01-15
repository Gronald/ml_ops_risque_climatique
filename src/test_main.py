from src.main import get_prediction


def tests_unitaires():
    
    """rentrer une valeur et voir sa vaeur attendue"""
    assert(get_prediction(46.15373399404384, 4.925852382365117, 1984).get('prediction')) == 0
    #Trouver un exemple avec un 1 ou refaire le modele avec k = 1
    
    #Test sur l'annee
    assert(get_prediction(46.15373399404384, 4.925852382365117, 2024)) == "Erreur dans la saisie"

    #Test sur la latitude
    assert(get_prediction(-100, 4.925852382365117, 1984)) == "Erreur dans la saisie"

     #Test sur la longitude
    assert(get_prediction(46.15373399404384, -100, 1984)) == "Erreur dans la saisie"

    # https://fastapi.tiangolo.com/tutorial/testing/