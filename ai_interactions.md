# AI Interactions Log

## Challenge 1: Advanced Song Features

### Prompts used

1. **Expand the dataset:** Add popularity (0–100), release decade, 2–3 pipe-separated mood tags, explicit (0/1), and instrumentalness (0.0–1.0) to every song, preserving the existing columns.
2. **Update the loader:** Parse popularity, release decade, and explicit as integers; instrumentalness as a float; and mood tags as a list split on `|`, without changing existing conversions.
3. **Update scoring and `UserProfile`:** Add up to 0.5 for popularity closeness, 0.5 for a decade match, up to 1.0 for overlapping mood tags, and up to 0.3 for instrumentalness closeness. Include a reason for each score contribution and preserve the existing score rules.
4. **Update profiles:** Supply the new preference fields in each CLI profile.
5. **Document and verify:** Record the workflow and manually check that a song's total matches its listed score reasons.

### Changes generated

- Added five columns and values for all 18 songs. The original columns and their values were preserved.
- Extended `load_songs` to convert the added numeric columns and split mood tags into lists.
- Added the new preferences to `UserProfile` and to each CLI profile.
- Added popularity, decade, mood-tag overlap, and instrumentalness contributions with readable score reasons.
- Left the existing genre, mood, and energy rules unchanged.

### Manual Verification Notes

- Ran `python3 -m src.main`; it loaded all 18 songs and returned recommendations for all five profiles.
- Checked the CSV headers, row count, popularity and explicit ranges, instrumentalness ranges, and that every mood tag field has two or three tags.
- For the High-Energy Pop profile, Sunrise City scored 6.00. Its displayed reasons add to 6.00: 1.00 genre + 1.00 mood + 1.74 energy + 0.48 popularity + 0.50 decade + 1.00 mood-tag overlap + 0.28 instrumentalness.
- The first run exposed a loader bug: instrumentalness was still a string, so scoring it against a float raised a `TypeError`. I added it to the existing float-field conversion set and reran the CLI successfully.
- I found no other issues during these checks.

---

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**Prompts used:**

<!-- Paste the key prompts you gave the agent -->

**What did the agent generate or change?**

<!-- List the files edited, code generated, or commands run -->

**What did you verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->
