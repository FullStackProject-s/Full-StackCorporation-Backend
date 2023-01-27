from general.tests.model_factory.base_factory import create_model_factory

make_specialty = create_model_factory(
    'employee.DeveloperOrganizationSpecialty'
)
make_developer = create_model_factory('employee.Developer')
make_project_manager = create_model_factory('employee.ProjectManager')
make_technologies = create_model_factory('employee.Technologies')
make_administrator = create_model_factory('employee.Administrator')
