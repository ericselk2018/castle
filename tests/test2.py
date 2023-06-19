from tests.test_case import TestCase

class Test1(TestCase):

    def test2(self):
        # starts in attract mode as expected
        self.assert_mode_running('attract')

        # advances to base mode as expected, when game starts
        # game mode (as system mode) also running
        self.start_single_player_game()
        self.assert_mode_running('game')
        self.assert_mode_running('base')
        self.add_player()
        self.assert_player_number(1)

        # base is running here
        self.assert_mode_running('base')

        self.drain_ball()

        # this will fail, base stops automatically when all balls drained
        # self.assert_mode_running('base')

        # moved to 2nd player as expected
        self.assert_player_number(2)

        # maybe need to press start for next player? doesn't help
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run()

        # shows only one active game mode named "game"
        # self.log.info('active modes')
        # for mode in self.machine.mode_controller.active_modes:
        #     self.log.info(mode.name)

        self.assert_mode_running('game')

        # self.machine.playfields['playfield'].available_balls = 0
        # self.advance_time_and_run()

        # this fails - how do I get base running again? start next turn?
        self.assert_mode_running('base')
