from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, Module, Subject  # 添加 Subject 导入
from .forms import ModuleFormSet


class CourseModelTest(TestCase):
    """测试课程模型"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_teacher',
            password='testpass123'
        )
        # 创建一个必需的 Subject 对象
        self.subject = Subject.objects.create(
            title='测试学科',
            slug='test-subject'
        )
        self.course = Course.objects.create(
            title='测试课程',
            slug='test-course',
            owner=self.user,
            subject=self.subject  # 添加 subject 字段
        )

    def test_course_creation(self):
        """测试课程是否能被成功创建"""
        self.assertEqual(self.course.title, '测试课程')
        self.assertEqual(self.course.slug, 'test-course')
        self.assertEqual(self.course.owner.username, 'test_teacher')
        self.assertEqual(self.course.subject.title, '测试学科')  # 新增断言

    def test_course_str_method(self):
        """测试课程的字符串表示"""
        self.assertEqual(str(self.course), '测试课程')