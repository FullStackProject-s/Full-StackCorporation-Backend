from general.tests.model_factory.base_factory import create_model_factory

make_user = create_model_factory(
    'user.CustomUser',
    is_active=True
)
make_profile = create_model_factory('user.Profile')
