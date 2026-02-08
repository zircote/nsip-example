# Requesting a Flock Analysis

Use this guide when you want the system to crunch numbers for you — comparing animals, ranking your flock, checking inbreeding, or getting mating recommendations.

This is one of the most powerful features of the system, and the good news is: **you just fill out a form and the computer does the rest.**

---

## What Kinds of Analysis Can You Request?

| Analysis | What It Does | When to Use It |
|---|---|---|
| **Mating Recommendations** | Finds the best rams to breed with a specific ewe | Before breeding season, to plan pairings |
| **Evaluate Flock** | Gives you an overview of your whole flock's genetics | Annually, to see how your flock is improving |
| **Compare Animals** | Puts 2-5 animals side by side so you can see differences | When deciding between animals to keep or sell |
| **Rank Animals** | Scores and sorts your animals based on traits you choose | When selecting replacements or sale animals |
| **Inbreeding Matrix** | Checks all possible pairings in a group for inbreeding risk | Before breeding season, to avoid risky pairings |
| **Flock Profile** | A summary of your whole flock's strengths and weaknesses | When talking to a breeding advisor or buyer |

---

## Steps

### Step 1 — Go to the Issues Tab

At the top of the project page, click on **"Issues"**.

### Step 2 — Start a New Request

Click the green **"New issue"** button.

### Step 3 — Choose the Flock Action Form

Find **"Flock Action"** in the list and click **"Get started"**.

### Step 4 — Pick Your Analysis Type

The form will ask you to choose one of the six options listed above. Click the one you want.

### Step 5 — Enter the Animal IDs

In the **"Animals"** field, type the ID numbers of the animals you want analyzed. Put each one on its own line:

```
12345
67890
11111
22222
```

- For **Mating Recommendations**: Enter the ewe(s) you want recommendations for
- For **Compare**: Enter 2 to 5 animals
- For **Rank**: Enter all the animals you want ranked
- For **Inbreeding Matrix**: Enter all the animals in the breeding group
- For **Evaluate Flock** or **Flock Profile**: Enter your whole flock (or a representative group)

### Step 6 — (For Ranking Only) Enter Trait Weights

If you chose **"Rank Animals,"** the form will also ask what traits matter most to you. Enter them like this:

```
WWT:3
NLB:2
FAT:-1
```

This tells the system: "I care a lot about weaning weight (3), somewhat about litter size (2), and I want less fat (-1)."

**Don't know what to put?** Here are some common setups:

- **For a meat flock**: `WWT:3, PWWT:2, FAT:-1, EMD:2`
- **For a maternal flock**: `NLB:3, NLW:3, WWT:1`
- **For balanced improvement**: `WWT:2, NLB:2, PWWT:1, EMD:1`

If this feels confusing, just skip it and ask your breeding advisor to help. You can also leave it blank and the system will use a balanced default.

### Step 7 — Submit

Click the green **"Submit new issue"** button.

### Step 8 — Wait for Results

The system will work on your request. Depending on how many animals you entered, this might take a few minutes. When it's done, you'll find:

1. A **comment** on your request with a summary of findings
2. A **report** (a separate document the system creates) with detailed tables and recommendations

Your farm manager can help you find the report if you can't locate it.

---

## Understanding the Results

The reports use some abbreviations for genetic traits. Here's a quick decoder:

| Abbreviation | What It Means | Why It Matters |
|---|---|---|
| **BWT** | Birth Weight | Heavier at birth (watch for lambing difficulty) |
| **WWT** | Weaning Weight | How fast lambs grow to weaning |
| **PWWT** | Post-Weaning Weight | Growth after weaning |
| **FAT** | Fat Depth | Carcass fat (lower is usually leaner) |
| **EMD** | Eye Muscle Depth | Meatiness (higher = more meat) |
| **NLB** | Number of Lambs Born | Litter size tendency |
| **NLW** | Number of Lambs Weaned | How many lambs a ewe successfully raises |

**Higher numbers are usually better** for growth and maternal traits. For fat, **lower (or negative)** is usually preferred if you want leaner animals.

Don't worry about memorizing all of this. The reports include explanations, and your breeding advisor can walk you through the numbers.

---

## Tips

- The best time to run analyses is **before breeding season** so you can plan pairings
- You can run the same analysis multiple times with different animals — each one creates its own separate record
- **Inbreeding Matrix** is especially valuable if you've been using the same rams for several years. It shows you which pairings to avoid
- If you just want a quick sanity check on one pairing, it might be easier to just create a Mating Record (see [Recording a Mating](recording-a-mating.md)) — it automatically checks inbreeding for you
