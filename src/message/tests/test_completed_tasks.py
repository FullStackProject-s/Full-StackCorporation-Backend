from django.urls import reverse

from general.tests.generic import BaseTestCaseGeneric

from message.serializers import (
    CompletedTasksSerializer,
    TaskSerializer,
)
from message.models import CompletedTasks

from general.tests.model_factory import (
    make_completed_tasks,
    make_task,
    make_user,
    make_organization
)


class CompletedTasksTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`message.CompletedTasks`.
    """
    all_objects_url = reverse('all-completed-tasks')
    create_object_url = reverse('create-completed-tasks')

    retrieve_object_url = 'completed-tasks'
    delete_object_url = 'delete-completed-tasks'
    update_object_url = 'update-completed-tasks'

    make_method = make_completed_tasks
    serializer_class = CompletedTasksSerializer
    model_class = CompletedTasks

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def test_get_all_completed_tasks(self):
        self._test_get_all_objects()

    def test_completed_tasks_retrieve(self):
        reassignment = self.obj_1
        response_json = self._test_retrieve_object().json()

        self.assertEqual(
            response_json['checked'],
            False
        )
        self.assertEqual(
            response_json['text'],
            reassignment.text
        )

    def test_completed_tasks_create(self):
        creator = make_user(1)
        task_1, task_2 = make_task(2)
        org = make_organization(1)
        json = {
            "creator": creator.pk,
            'organization': org.pk,
            "text": 'test_completed_tasks_create',
            "tasks": [
                task_1.pk,
                task_2.pk
            ]
        }
        response_json = self._test_create_object(json).json()

        self.assertEqual(
            TaskSerializer(task_1).data,
            response_json['tasks'][0]
        )

        self.assertEqual(
            TaskSerializer(task_2).data,
            response_json['tasks'][1]
        )
        self.assertEqual(
            json['text'],
            response_json['text']
        )

    def test_delete_completed_tasks(self):
        self._test_delete_object()

    def test_put_completed_tasks(self):
        task_1, task_2 = make_task(2)
        json = {
            "text": 'test_put_completed_tasks',
            "tasks": [
                task_1.pk,
                task_2.pk
            ],
            'checked': True
        }
        response_json = self._test_put_object(json).json()
        pk = response_json['pk']
        self.assertEqual(
            response_json['checked'],
            True
        )
        self.assertEqual(
            CompletedTasks.objects.get(pk=pk).checked,
            True
        )

    def test_patch_completed_tasks(self):
        pk = self.obj_2.pk
        self.default_object_number = 2

        json = {
            'text': 'test_patch_reassignment',
            'checked': True

        }
        response_json = self._test_patch_object(json).json()

        self.assertEqual(
            CompletedTasks.objects.get(pk=pk).text,
            response_json['text']
        )
        self.assertEqual(
            CompletedTasks.objects.get(pk=pk).checked,
            response_json['checked']
        )
