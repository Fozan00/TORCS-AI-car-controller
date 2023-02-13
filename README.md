# TORCS-AI-car-controller

Generated dataset of car races on different tracks using manual controls.
I have used feed forward neural network for creating the AI controller.

For basic understanding of the TORCS framework and guidelines for installation please refer to
http://cs.adelaide.edu.au/~optlog/SCR2015/index.html
https://www.youtube.com/watch?v=nKIQvc-UdRo
Introduction:
TORCS architecture has three respects. First, TORCS works as a client-server applications: the
bots are run as external processes connected to the race server through UDP connections. Second,
it adds real-time: every game tic (roughly corresponding to 20ms of simulated time), the server
sends the current sensory inputs to each bot and then it waits for 10ms (of real time) to receive
an action from the bot. If no action arrives, the simulation continues and the last performed action
is used. Finally, the competition software creates a physical separation between the driver code
and the race server building an abstraction layer, a sensors and actuators model, which (i) gives
complete freedom of choice regarding the programming language used for bots and (ii) restricts
the access only to the information defined by the designer. The server file is known as src_server
and it to be configured. The client can be in multiple languages as for testing purposes sample
java , c++, python and c# clients are available. You should use the python client in this project.
Objective:
Aim of the project is to design a controller for car racing that can race with other cars on different
tracks and wins the race. The usual performance metrics like speed, obstacle avoidance and track
following should be kept in mind while designing this controller. The controllers perceive the
racing environment through telemetry. Telemetry uses a number of sensors that describe the
relevant features of the car surroundings (e.g., the track limits, the position of near-by obstacles),
of the car state (the fuel level, the engine RPMs, the current gear, etc.), and the current game state
(lap time, number of lap, etc.). We will keep this problem simple by disabling noisy sensor and
car damage, and by supplying unlimited amount of fuel. Rule based controller isn’t acceptable.
A simple and basic car is designed and downloadable at the above-mentioned site. Please
download and have a look at the interfaces (methods) their sample implementation. You have to
use the same interfaces in your controller.
