import pytest

from ..review import BaseCharacter, Mage


@pytest.fixture
def template_character():
    return BaseCharacter('Template')


@pytest.fixture
def mage_character():
    return Mage('Mage')
