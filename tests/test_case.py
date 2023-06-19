from mpf.tests.MpfMachineTestCase import MpfMachineTestCase
import logging

class TestCase(MpfMachineTestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

        # see MpfTestCase.unittest_verbosity - looks like probably a command line option to enable verbose test logs
        # This enables logging for game events, not just tests.
        console_log = logging.StreamHandler()
        console_log.setLevel(logging.DEBUG)
        logging.basicConfig(level=logging.DEBUG,
                           handlers=[console_log])

        # internal logger just for our test needs
        self.log = logging.getLogger("Test Case")
        self.log.setLevel(logging.INFO)

    def unittest_verbosity(self):
        return 2

    def start_single_player_game(self):
        self.set_num_balls_known(6)
        self.machine.playfield.ball_search.disable()
        self.advance_time_and_run()
        self.hit_and_release_switch('s_start')
        self.assertIsNotNone(self.machine.game)
        self.advance_time_and_run()

        # ball moves from trough 1 to plunger lane
        self.release_switch_and_run('s_trough1', 1)
        self.hit_switch_and_run('s_plunger_lane', 1)

        # ball moves from trough 2 to trough 1
        self.release_switch_and_run('s_trough2', 1)
        self.hit_switch_and_run('s_trough1', 1)

        # ball moves from trough 3 to trough 2
        self.release_switch_and_run('s_trough3', 1)
        self.hit_switch_and_run('s_trough2', 1)

        # ball moves from trough 4 to trough 3
        self.release_switch_and_run('s_trough4', 1)
        self.hit_switch_and_run('s_trough3', 1)

        # ball moves from trough 5 to trough 4
        self.release_switch_and_run('s_trough5', 1)
        self.hit_switch_and_run('s_trough4', 1)

        # ball moves from trough 6 to trough 5
        self.release_switch_and_run('s_trough6', 1)
        self.hit_switch_and_run('s_trough5', 1)

    def add_player(self):
        prev_players = self.machine.game.num_players
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run()
        self.assertEqual(prev_players + 1, self.machine.game.num_players)

    def drain_ball(self):
        self.release_switch_and_run('s_plunger_lane', 1)
        self.hit_switch_and_run('s_trough6', 1)
        # drain = self.machine.ball_devices.items_tagged("drain")[0]
        # for _ in range(self.machine.game.balls_in_play):
        #     self.log.info('draining ball')
        #     self.machine.default_platform.add_ball_to_device(drain)
        # self.advance_time_and_run()
        # self.log.info('balls in play after drain')
        # self.log.info(self.machine.game.balls_in_play)

    def assert_player_number(self, number):
        self.assertEqual(number, self.machine.game.player.index + 1)

    def assert_mode_running(self, mode_name):
        self.assertModeRunning(mode_name)