from django.urls import reverse

from general.tests.generic import BaseTestCaseGeneric

from message.serializers import TaskSerializer
from message.models import Task

from general.tests.model_factory import (
    make_user,
    make_task
)


class TaskTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`message.Task`.
    """
    all_objects_url = reverse('all-tasks')
    create_object_url = reverse('create-task')

    retrieve_object_url = 'task'
    delete_object_url = 'delete-task'
    update_object_url = 'update-task'

    make_method = make_task
    serializer_class = TaskSerializer
    model_class = Task

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def test_get_all_tasks(self):
        self._test_get_all_objects()

    def test_task_retrieve(self):
        reassignment = self.obj_1
        response_json = self._test_retrieve_object().json()

        self.assertEqual(
            response_json['text'],
            reassignment.text
        )

    def test_task_create(self):
        user = make_user(1)

        json = {
            "creator": user.pk,
            "text": 'test_task_create',
        }
        response_json = self._test_create_object(json).json()

        pk = response_json['pk']

        self.assertEqual(
            response_json['text'],
            Task.objects.get(pk=pk).text
        )

    def test_delete_task(self):
        self._test_delete_object()

    def test_put_task(self):
        self.default_object_number = 2

        json = {
            "text": 'test_put_task',
        }
        response_json = self._test_put_object(json).json()

        self.assertEqual(
            response_json['text'],
            json['text']
        )

    def test_patch_task(self):
        self.default_object_number = 3

        json = {
            "text": 'test_patch_task',
        }
        response_json = self._test_patch_object(json).json()

        self.assertEqual(
            response_json['text'],
            json['text']
        )
