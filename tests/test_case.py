from mpf.tests.MpfMachineTestCase import MpfMachineTestCase
import logging

class TestCase(MpfMachineTestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

        # this controls logging outside of tests, for times we want to see logs from game code we are testing
        # level 99 = no logging
        # logging.basicConfig(level=logging.DEBUG)
        logging.basicConfig(level=99)

        # internal logger just for our test needs
        self.log = logging.getLogger("Test Case")
        self.log.setLevel(logging.INFO)

    def unittest_verbosity(self):
        return 2

    def start_single_player_game(self):
        # make test bugs easier to find, ensure a game isn't already started
        self.assertIsNone(self.machine.game)

        # start game by pressing start switch and ensure it started
        self.hit_and_release_switch('s_start')
        self.assertIsNotNone(self.machine.game)

        self.eject_ball_from_trough()

        # should be one player game
        self.assertEqual(1, self.machine.game.num_players)

    def eject_ball_from_trough(self):
        # ball moves from trough 1 to plunger lane
        self.release_switch_and_run('s_trough1', 1)
        self.hit_switch_and_run('s_plunger_lane', 1)

        # remaining balls settle in trough (roll down one switch at a time)
        for i in [1, 2, 3, 4, 5]:
            self.release_switch_and_run('s_trough' + str(i + 1), 1)
            self.hit_switch_and_run('s_trough' + str(i), 1)

    def launch_ball(self):
        # should be a ball to launch
        self.assert_switch_state('s_plunger_lane', True)

        self.release_switch_and_run('s_plunger_lane', 1)

    def add_player(self):
        prev_players = self.machine.game.num_players
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run()
        self.assertEqual(prev_players + 1, self.machine.game.num_players)

    def assert_switch_state(self, name, state):
        self.assertSwitchState(name, state)

    def drain_ball(self):
        # must launch ball first
        self.assert_switch_state('s_plunger_lane', False)

        # trough cannot be full
        self.assert_switch_state('s_trough6', False)

        # put ball in trough
        self.hit_switch_and_run('s_trough6', 1)

        # eject ball because this happens automatically
        self.eject_ball_from_trough()

    def assert_player_number(self, number):
        self.assertEqual(number, self.machine.game.player.index + 1)

    def assert_mode_running(self, mode_name):
        self.assertModeRunning(mode_name)

    def assert_mode_not_running(self, mode_name):
        self.assertModeNotRunning(mode_name)