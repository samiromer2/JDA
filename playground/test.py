# import pandas as pd
# import matplotlib.pyplot as plt

# print("Setup works!")

import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    "product": ["A", "B", "C"],
    "revenue": [100, 200, 150]
}

df = pd.DataFrame(data)

# Print data
print(df)

# Plot
df.plot(kind="bar", x="product", y="revenue")

plt.title("Test Chart")
plt.show()