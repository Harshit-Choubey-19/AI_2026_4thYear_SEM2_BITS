import random

class PartPickingAgent:
    def actuate(self, percept):
        """
        Rational policy:
        Map 'Gear' → 'Bin Gear'
        Map 'Bolt' → 'Bin Bolt'
        """
        if percept == "Gear":
            return "Bin Gear"
        elif percept == "Bolt":
            return "Bin Bolt"
        else:
            raise ValueError("Unknown percept")

# Simulation Parameters
TRIALS = 100
SUCCESS_PROBABILITY = 0.9  # Bernoulli(0.9)

# Initialize agent
agent = PartPickingAgent()

score = 0

for _ in range(TRIALS):
    # Generate random part
    actual_part = random.choice(["Gear", "Bolt"])
    
    # Agent decision
    action = agent.actuate(actual_part)
    
    # Stochastic actuator failure (Bernoulli)
    success = random.random() < SUCCESS_PROBABILITY
    
    if success:
        final_bin = action
    else:
        # Failure → wrong bin
        final_bin = "Bin Bolt" if action == "Bin Gear" else "Bin Gear"
    
    # Performance evaluation
    if (actual_part == "Gear" and final_bin == "Bin Gear") or \
       (actual_part == "Bolt" and final_bin == "Bin Bolt"):
        score += 1
    else:
        score -= 1

print("Final Score after 100 trials:", score)
