

def test_temp_level_one(template_character):
    assert isinstance(template_character.level, int)
    assert template_character.level == 1


def test_mage_health_and_resource(mage_character):
    assert hasattr(mage_character, 'health')
    assert hasattr(mage_character, 'mana')


def test_mage_greater_stats(template_character, mage_character):
    assert template_character.intel < mage_character.intel
    assert template_character.stam < mage_character.stam


def test_level_up(template_character, mage_character):
    assert template_character.level < template_character.level_up().level
    assert mage_character.level < mage_character.level_up().level
