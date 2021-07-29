import pytest


APPLICATION_VERSION = 0.1

CAT_BOT_FEATURE_ENABLED = True


@pytest.mark.cat
def test_fluffy_cat():
    pass


@pytest.mark.dog
def test_scruffy_dog():
    pass


@pytest.mark.skipif(APPLICATION_VERSION == 0.1, reason='testing application version')
def test_skip_with_condition():
    pass


@pytest.mark.skipif(CAT_BOT_FEATURE_ENABLED is False, reason='feature enabled')
def test_skip_with_condition2():
    pass


# @pytest.mark.skipif(PAYPAL_FEATURE is False, reason="Feature is disabled")
# def test_skip_with_condition2():
#     pass


@pytest.mark.skip()
def test_puffy_hamster():
    pass
