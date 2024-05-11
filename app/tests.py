import datetime
from django.test import TestCase
from .models import Project

class ProjectCreationTestCase(TestCase):
    def test_project_creation(self):
        # Create a new project
        project = Project.objects.create(project_name="Test Project", deadline="2024-05-01", status="Not completed")
        
        # Retrieve the project from the database
        saved_project = Project.objects.get(pk=project.pk)
        
        # Assert that the project is saved correctly
        self.assertEqual(saved_project.project_name, "Test Project")
        self.assertEqual(saved_project.deadline, datetime.date(2024, 5, 1))
        self.assertEqual(saved_project.status, "Not completed")

class ProjectEditingTestCase(TestCase):
    def test_project_editing(self):
        # Create a new project
        project = Project.objects.create(project_name="Test Project", deadline="2024-05-01", status="Not completed")
        
        # Retrieve the project from the database
        saved_project = Project.objects.get(pk=project.pk)
        
        # Modify project attributes
        saved_project.project_name = "Edited Project"
        saved_project.deadline = "2024-06-01"
        saved_project.status = "Completed"
        saved_project.save()
        
        # Retrieve the edited project from the database
        edited_project = Project.objects.get(pk=project.pk)
        
        # Assert that the project is edited correctly
        self.assertEqual(edited_project.project_name, "Edited Project")
        self.assertEqual(edited_project.deadline, datetime.date(2024, 6, 1))
        self.assertEqual(edited_project.status, "Completed")
