def update_projects(instance, validated_data):
    if projects := validated_data.get('projects', None):
        for project in instance.projects.all():
            if project not in projects:
                project.delete()
