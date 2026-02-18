# Problem 1
**Rationality in Stochastic Environments**

### PEAS Framework

| Component               | Description                                                                     |
| ----------------------- | ------------------------------------------------------------------------------- |
| **Performance Measure** | +1 for correct sort, −1 for incorrect sort                                      |
| **Environment**         | Conveyor belt with random parts (Gear/Bolt), stochastic due to actuator failure |
| **Actuators**           | Robotic arm → `Bin Gear` or `Bin Bolt`                                          |
| **Sensors**             | Camera returning percept string: `"Gear"` or `"Bolt"`                           |

### Agent Implementation (Rational Agent)

A *rational agent* chooses the action that maximizes expected performance based on its percept.

Since:
- If percept = "Gear" → Best action = Bin Gear
- If percept = "Bolt" → Best action = Bin Bolt

The agent should always map correctly.

### Expected Performance (Mathematical Analysis)

Let:

- Success probability = 0.9
- Failure probability = 0.1
- Reward for correct = +1
- Penalty for incorrect = −1

Expected reward per trial:

                        E = (0.9)(+1)+(0.1)(−1)
                        E =  0.9 − 0.1 = 0.8

Expected total score over 100 trials: 100 × 0.8 = 80

So typical simulation result will be around ***75–85** *depending on randomness*.


