from django.test import TestCase
from django.urls import resolve
from django.urls import reverse_lazy

from boards.models import Board
from boards.views import BoardListView


class IndexTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse_lazy('index')
        self.response = self.client.get(url)

    def test_index_view_status_code(self):
        url = reverse_lazy('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_index_resolves_index_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, BoardListView)

    def test_index_view_contains_link_to_topics_page(self):
        board_topics_url = reverse_lazy('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))