from drf_spectacular.utils import extend_schema_serializer, OpenApiExample


def developer_change_team(serializer_name):
    return extend_schema_serializer(
        exclude_fields=('single',),  # schema ignore these fields
        examples=[
            OpenApiExample(
                'Valid example 1',
                value={
                    'team': 'blabla1',
                },
            ),
        ]
    )(serializer_name)