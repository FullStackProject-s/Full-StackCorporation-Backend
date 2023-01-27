from general.tests.model_factory.base_factory import create_model_factory

make_reassignment = create_model_factory('message.Reassignment')
make_task = create_model_factory('message.Task')
make_completed_tasks = create_model_factory('message.CompletedTasks')
make_invite_to_organization = create_model_factory(
    'message.InviteToOrganization'
)
