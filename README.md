# Most Streamed Spotify Songs 2025 — Data Analysis

A beginner data analysis project exploring the **Most Streamed Spotify Songs 2025** dataset from Kaggle, focused on identifying which artists and songs dominated the dataset based on total Spotify streams, and understanding what "dominance" actually means depending on how you measure it.

> **Note on scope:** `spotify_streams_total` appears to be a cumulative stream count. Unless Kaggle's dataset documentation confirms these streams were all accumulated strictly during 2025, this analysis treats them as total accumulated streams reflected in the dataset — not as "streams that happened in 2025."

## Dataset

- **Source:** Kaggle — "Most Streamed Spotify Songs 2025"
- **File:** `most_streamed_spotify_2025.csv`
- **Size:** 730 rows × 10 columns

**Columns:**
| Column | Description |
|---|---|
| `rank` | Overall ranking of the song |
| `track` | Song title |
| `artist` | Artist name |
| `billed_artist_count` | Number of credited artists |
| `is_collaboration` | Whether the song is a collaboration |
| `spotify_streams_total` | Total Spotify streams |
| `daily_streams` | Daily streams |
| `daily_streams_rank` | Ranking based on daily streams |
| `daily_stream_share_pct` | Percentage of daily streams |
| `wrapped_global_top10_rank` | Global Top 10 ranking (Spotify Wrapped) — mostly missing, see Data Cleaning |

## Tools Used

- Python 3.14
- pandas — data loading, exploration, cleaning, aggregation
- matplotlib — visualization

## Process

### 1. Loading & Understanding the Data
Loaded the CSV with `pd.read_csv()` and explored its structure using `.shape`, `.columns`, and `.info()` to understand row/column counts and data types before doing any analysis.

### 2. Data Cleaning
Found that `wrapped_global_top10_rank` had only 3 non-null values out of 730 (727 missing). Because the column contains only 3 non-null values and is not required for the main analysis, it was excluded rather than imputed or used to remove the majority of observations — filling it with a placeholder would have been misleading, and dropping the affected rows would have destroyed 99% of the dataset:

```python
data = data.drop(columns=["wrapped_global_top10_rank"])
```

### 3. Analysis

**Top 10 songs by total streams:**
The dataset's existing `rank` column was verified to already be ordered 1–10 ascending, so `head(10)` reliably returns the top 10 by total streams:
```python
data.head(10)[["rank", "track", "artist", "spotify_streams_total"]]
```

**Most frequent artists in the dataset:**
Note: appearance count measures representation in the dataset, not necessarily popularity — an artist with 15 songs isn't automatically "more popular" than one with 5.
```python
data["artist"].value_counts().head(10)
```

**Top artists by total streams:**
```python
data.groupby("artist")["spotify_streams_total"].sum().sort_values(ascending=False).head(10)
```

**Top artists by average streams per song (with song count for context):**
```python
data.groupby("artist")["spotify_streams_total"].agg(["count", "mean"]).sort_values("mean", ascending=False).head(10)
```

### 4. Visualization
A bar chart of the top 10 artists by total streams, to make the scale of the leading artist's dominance immediately visible rather than reading it off a table.

## Key Findings

**1. Bad Bunny leads the dataset in total streams — largely driven by volume.**
Bad Bunny tops the dataset with 11.2 billion total streams — more than double Taylor Swift, the runner-up at 4.7 billion. This indicates strong representation across multiple highly streamed songs rather than dominance being driven by a single track. Part of this lead is volume-driven: Bad Bunny has 15 songs in the dataset versus Taylor Swift's 12, so some of the gap comes from having more entries, not purely stronger individual songs.

**2. A high "average" is only informative with enough songs behind it.**
Artists like W Sound, Dream Supplier, and Jin top the average-streams-per-song ranking — but each has only one song in the dataset, so their "average" is really just that one song's number, not a genuine average. This scales with sample size: one song is a weak basis for generalization, four songs (like HUNTR/X, averaging ~900M) is more informative but still limited, and fifteen songs (like Bad Bunny) is a stronger representation of an artist's performance across the dataset.

**3. Total streams and average streams per song measure different things.**
More songs increases an artist's total streams (this is a big part of why Bad Bunny leads overall), but it doesn't guarantee a higher average per song — HUNTR/X's 4 songs average more per song (~900M) than Bad Bunny's 15 (~750M). Total streams reward volume/output, while average streams per song indicate how strongly an artist's songs perform on average within this dataset — streams reflect popularity, exposure, fanbase, playlist placement, and timing, not "quality," which this dataset has no way to measure. An artist can lead on one metric and lose on the other. With only 4 songs, HUNTR/X's average is also a smaller sample than Bad Bunny's 15, so it's less stable as a long-term signal.

## What I'd Explore Next

- Whether collaborations (`is_collaboration`) stream better on average than solo songs
- Whether `billed_artist_count` correlates with stream performance
- Daily stream trends (`daily_streams`, `daily_streams_rank`) versus total streams

## About

Built as a hands-on beginner Data Science project — first time working with pandas, groupby aggregations, data cleaning decisions, and matplotlib visualization.
