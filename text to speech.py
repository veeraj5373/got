import matplotlib.pyplot as plt
import numpy as np

# List of OpenAI engines
engines = ['gpt-3.5-turbo', 'babbage-002', 'davinci-002', 'text-davinci-003', 'text-curie-001', 'text-babbage-001', 'text-ada-001']

# Assumed scores on a scale of 1 to 5 for each engine
performance = [4, 2, 4, 3, 2, 2, 2]  # Performance rating
use_case = [4, 1, 4, 3, 2, 2, 2]  # Use case suitability rating
cost = [3, 2, 4, 4, 2, 2, 2]  # Cost rating

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 9))


# Plot Performance
axs[0].bar(engines, performance, color='skyblue')
axs[0].set_title('Performance')
axs[0].set_ylabel('Scale')

# Plot Use Case Suitability
axs[1].bar(engines, use_case, color='lightgreen')
axs[1].set_title('Use Case Suitability')
axs[1].set_ylabel('Scale')

# Plot Cost
axs[2].bar(engines, cost, color='coral')
axs[2].set_title('Cost')
axs[2].set_ylabel('Scale')

# Adjust layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()



