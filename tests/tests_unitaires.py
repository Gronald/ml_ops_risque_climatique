from app.main import predict
import pytest


def tests_unitaires():
    
    """rentrer une valeur et voir sa vaeur attendue"""
    assert(predict([100, 100, 2008])) == 1

    """on rentre une année > 2000, il doit y avoir une erreur"""
    test_annee = predict([100, 100, 2023])
    assert response.status_code == 400

    """on rentre latitude hors France, il doit y avoir une erreur"""
    test_annee = predict([100, 100, 2008])
    assert response.status_code == 400

    """on rentre longitude hors France, il doit y avoir une erreur"""
    test_annee = predict([100, 100, 2008])
    assert response.status_code == 400