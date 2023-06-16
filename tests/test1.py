from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class Test1(MpfMachineTestCase):

    def _start_single_player_game(self, secs_since_plunge):
        self.set_num_balls_known(6)
        self.machine.playfield.ball_search.disable()
        self.advance_time_and_run(10)
        self.hit_and_release_switch('s_start')

        # game should be running
        self.assertIsNotNone(self.machine.game)

        # advance enough time for the balls to eject and stuff
        self.advance_time_and_run(2)

    def test2(self):
        self.mock_event('find_me_player_score_less_than_10000')
        self.mock_event('find_me_player_score_between_10000_and_20000')

        self._start_single_player_game(1)

        self.assertEventCalled('find_me_player_score_less_than_10000')

        # 1,000 points per flipper hit
        self.hit_and_release_switch('s_left_flipper')
        self.hit_and_release_switch('s_left_flipper')
        self.hit_and_release_switch('s_left_flipper')
        self.hit_and_release_switch('s_left_flipper')
        self.hit_and_release_switch('s_left_flipper')
        self.hit_and_release_switch('s_left_flipper')
        self.hit_and_release_switch('s_left_flipper')
        self.hit_and_release_switch('s_left_flipper')
        self.hit_and_release_switch('s_left_flipper')
        self.hit_and_release_switch('s_left_flipper')

        # only 10,000 points
        self.assertEventNotCalled('find_me_player_score_between_10000_and_20000')

        self.hit_and_release_switch('s_left_flipper')

        # 11,000 points
        self.assertEventCalled('find_me_player_score_between_10000_and_20000')
