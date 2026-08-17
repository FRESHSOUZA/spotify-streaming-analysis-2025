import pandas as pd

data = pd.read_csv("most_streamed_spotify_2025.csv")

print(data.head())
print(data.shape)
print(data.columns)
print(data.info())
print(data["rank"].head(10))
print(data.head(10)[["rank", "track", "artist", "spotify_streams_total"]])
print(data["artist"].value_counts().head(10))
print(data.groupby("artist")["spotify_streams_total"].sum().sort_values(ascending=False).head(10))
print(data.groupby("artist")["spotify_streams_total"].sum().sort_values(ascending=False).head(10))
data.groupby("artist")["spotify_streams_total"].sum().sort_values(ascending=False).head(10)
print(data.groupby("artist")["spotify_streams_total"].mean().sort_values(ascending=False).head(10))
print(data.groupby("artist")["spotify_streams_total"].agg(["count", "mean"]).sort_values("mean", ascending=False).head(10))
print(data.isnull().sum())
data = data.drop(columns=["wrapped_global_top10_rank"])
print(data.isnull().sum())
import matplotlib.pyplot as plt

top_artists = data.groupby("artist")["spotify_streams_total"].sum().sort_values(ascending=False).head(10)

plt.bar(top_artists.index, top_artists.values)
plt.xticks(rotation=45, ha="right")
plt.xlabel("Artist")
plt.ylabel("Total Streams")
plt.title("Top 10 Artists by Total Spotify Streams")
plt.tight_layout()
plt.show()





