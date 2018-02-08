import unittest
from app.models import Comment

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment = Comment(body = 'Wow, thats great')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)