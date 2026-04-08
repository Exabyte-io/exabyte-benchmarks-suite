import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")

df["total_procs"] = df["nproc"] * df["nodes"]
gnu = df[df["Build"] == "GNU"]
plt.plot(gnu["total_procs"], gnu["Time (s)"], "o-", label="GNU")
intel = df[df["Build"] == "Intel"]
plt.plot(intel["total_procs"], intel["Time (s)"], "o-", label="Intel")
plt.legend(frameon=False)
plt.xlabel("Number of processors")
plt.ylabel("Time (s)")
plt.title("Time (s) vs number of processors")
plt.savefig("plot.png", dpi=150, bbox_inches="tight")
