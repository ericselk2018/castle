from tests.test_case import TestCase

class Test1(TestCase):

    def test2(self):
        self.assert_mode_running('attract')
        self.start_single_player_game()
        self.assert_mode_running('base')
        self.add_player()
        self.assert_player_number(1)
        self.launch_ball()

        self.assert_mode_not_running('test')
        self.post_event('start_mode_test', 1)
        self.assert_mode_running('test')

        self.drain_ball()
        self.assert_player_number(2)
        self.assert_mode_running('base')
        self.assert_mode_not_running('test')

        self.launch_ball()
        self.drain_ball()
        self.assert_player_number(1)
        self.assert_mode_running('base')
        self.assert_mode_running('test')
