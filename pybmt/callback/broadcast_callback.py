from pybmt.callback.base import PyBMTCallback
from collections import deque

from pybmt.fictrac.state import FicTracState


class BroadcastCallback(PyBMTCallback):
    """
    This class implements control logic for triggering a stimulus when tracking velocity reaches a certain
    threshold. It is just an example of how things can work in a closed loop experiment where tracking state triggers
    stimuli response.
    """

    def __init__(self, comms):
        """
        Setup a closed loop experiment that keeps track of a running average of the ball speed and generates a stimulus
        when the speed crosses a threshold.

        Args:
            comms: pipe/queue-like (needs send method)
        """

        # Call the base class constructor
        super().__init__()

        self.comms = comms

    def setup_callback(self):
        pass


    def process_callback(self, track_state: FicTracState):
        """
        This function is called with each update of fictrac's tracking state.
        A closed loop experiment that keeps track of a running average of the ball speed and generates a stimulus
        when the speed crosses a threshold.

        :param track_state:
        :return:
        """
        self.comms.send(track_state)
        return True

    def shutdown_callback(self):
        pass