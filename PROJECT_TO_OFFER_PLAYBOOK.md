# From MolGen Lab → High-Paying Job or Client
### The complete playbook for converting a portfolio project into crore-level opportunities

---

## The core idea

Most engineers applying to drug discovery AI roles have ML theory but zero deployed product.  
You will have both. That asymmetry is what this playbook is built around.

The three phases:

```
Phase 1 — Make the project undeniable
Phase 2 — Package the signal for each audience  
Phase 3 — Distribute deliberately, not broadly
```

Run Phase 1 fully before touching Phase 2. Run Phase 2 before Phase 3.  
The job path and client path run **in parallel** — don't choose one.

---

## Phase 1 — Make the project undeniable

> Goal: someone opens your project in 60 seconds and immediately understands what it does and that you know what you're talking about.

### The 60-second test checklist

- [ ] HuggingFace Space is live and loads without errors
- [ ] React UI renders, accepts a target, and returns molecules
- [ ] README has a screenshot or GIF at the very top (above the fold)
- [ ] All 4 Jupyter notebooks run top-to-bottom without errors
- [ ] GitHub repo has a clean commit history (not one giant "initial commit")
- [ ] `/docs` on the FastAPI backend shows all routes correctly

### The Loom video — your single most valuable asset

Record a **3-minute screen recording** of yourself using the app. Not a polished tutorial. Just you, the screen, and your voice.

Script outline:
1. "I built MolGen Lab — a generative AI tool for drug discovery. Let me show you what it does."
2. Type `EGFR` in the target input. Explain: "EGFR is a receptor that's mutated in about 15% of lung cancers."
3. Hit Generate. While it loads: "The model is generating SMILES strings — text representations of molecules — and scoring them."
4. Results appear. Walk through one card: "This candidate has a drug-likeness score of 0.87, passes Lipinski's Rule of 5, and low predicted toxicity."
5. "The full source is on GitHub, the notebooks walk through every step from scratch."

**This video goes everywhere:** README top section, LinkedIn post, every cold outreach message, every job application. It does more work than anything else you'll create.

### What "production-ready" means here

You don't need perfection. You need:
- No 500 errors on the happy path
- A loading state that doesn't look broken
- A result that a non-engineer could understand

If a pharma CTO opens your Loom link and watches 90 seconds, they should think: "this person actually built something."

---

## Phase 2 — Package the signal

### The LinkedIn post (post this the week the project goes live)

Structured exactly like this — do not deviate from the structure:

```
[HOOK — one striking sentence]
I built a tool that uses generative AI to design potential drug molecules from scratch.

[THE PROBLEM — 2 sentences, concrete numbers]
Drug discovery takes 12–15 years and costs $2 billion per approved drug. 
Most of that time is spent in the early search for viable molecule candidates.

[WHAT YOU BUILT — 3 tight bullet points]
→ Input a disease target (e.g. EGFR for lung cancer)
→ A pre-trained generative model proposes novel SMILES candidates  
→ Each one is scored for drug-likeness, toxicity, and binding potential

[ONE SURPRISING RESULT — make it specific]
Generated 20 EGFR candidates in ~40 seconds. 
14 passed Lipinski's Rule of 5. Top candidate: drug score 0.87, toxicity 0.09.

[THE LINKS]
GitHub: [link]
Live demo: [HuggingFace Space link]  
3-min walkthrough: [Loom link]

[CLOSE — what you're looking for]
I'm looking for roles or collaborations at the intersection of AI and drug discovery.
If you're building in this space, I'd love to connect.

#DrugDiscovery #GenerativeAI #Cheminformatics #MachineLearning #Healthcare
```

**Post timing:** Tuesday or Wednesday, 8–10am IST.  
**Tag:** Aganitha AI, Elucidata, and 2–3 researchers you've been following.  
**Do not** ask for likes or shares. The content does the work.

### The case study write-up (for your portfolio site or Notion)

A 1,000-word write-up structured as:

1. **The problem** — why drug discovery takes so long
2. **The approach** — how generative AI addresses the molecule search problem
3. **Technical decisions** — why MolGPT, why RDKit, why FastAPI + React
4. **What I learned** — one genuine insight (e.g. "SMILES validity rates from unconditional generation were ~65% — I had to implement a retry loop with a max_attempts cap to reliably get N valid candidates")
5. **What's next** — GNN-based generation, binding affinity prediction, quantum simulation module

This write-up signals domain depth, not just execution. Link to it from your LinkedIn and GitHub.

### Resume line

In your experience section, add under a "Projects" heading:

```
MolGen Lab  —  Generative AI Drug Discovery Platform  (2026)
Full-stack AI application for novel drug candidate generation. Pre-trained MolGPT model 
for SMILES generation, RDKit + DeepChem scoring pipeline (Lipinski, QED, toxicity), 
React/TypeScript dashboard, FastAPI backend, deployed on HuggingFace Spaces.
Stack: Python · PyTorch · HuggingFace · RDKit · React · TypeScript · FastAPI · AWS
```

---

## Phase 3 — Distribute deliberately

### Path A — Tier 1 company jobs

#### Target companies (pick 8–10 max, research each one)

| Company | Location | What they do | Why you fit |
|---|---|---|---|
| Aganitha.ai | Hyderabad / remote | AI for drug discovery pipelines | Direct match to MolGen Lab |
| Elucidata | Delhi / remote | ML on biomedical data | Strong data engineering angle |
| Insilico Medicine | Remote (HK-based) | Generative AI for pharma | Generative model focus |
| Recursion Pharmaceuticals | Remote-friendly | High-throughput drug discovery | Scale + AI infrastructure |
| Strand Life Sciences | Bengaluru | Bioinformatics + genomics | Indian HQ, strong domain |
| Pfizer / AstraZeneca India | Hyderabad / Mumbai | Big pharma AI teams | Stability + high salary |
| Any US healthtech (remote) | Remote | AI-driven clinical / discovery tools | ₹1Cr+ via geographic arbitrage |

#### Where to apply

- **LinkedIn Jobs** — set alerts for "computational biology engineer", "AI drug discovery", "ML scientist pharma"
- **Wellfound (AngelList)** — best for funded biotech startups, filter by "remote" + "AI"
- **Company careers pages directly** — set a monthly reminder to check each of your 8–10 targets
- **Naukri** — less useful for this niche but worth checking for domestic roles

#### What gets you past screening

Most screening is done by recruiters who don't understand the domain. They scan for:
- Specific keywords: `RDKit`, `cheminformatics`, `SMILES`, `DeepChem`, `molecular generation`
- A GitHub link that actually works
- Evidence of domain interest beyond the job description

Your resume, LinkedIn, and cover note should all include the keywords above naturally.

#### Cover note template

```
Hi [Name],

I'm a full-stack AI engineer with a background in healthcare AI 
(currently at Fitwell.ai) and a recent deep-dive into computational drug discovery.

I recently built MolGen Lab — a generative AI platform for novel drug candidate 
design using MolGPT, RDKit, and a React/TypeScript frontend. [Loom link / GitHub link]

I'm particularly interested in [Company] because of [1 specific thing about their work].  
I think my combination of production AI engineering and drug discovery domain knowledge 
could be useful to your team.

Happy to chat — I can do any timezone.

Ashraf
```

Keep it under 150 words. Specificity > length.

#### Salary negotiation anchors

| Role type | Domestic India | Remote US/EU |
|---|---|---|
| ML Engineer — Drug Discovery | ₹35–60 LPA | ₹70L–1Cr+ |
| Computational Biology Engineer | ₹30–55 LPA | ₹60–90L |
| Senior AI Scientist (3+ yrs) | ₹55–90 LPA | ₹1–1.5Cr |
| Staff / Lead Engineer | ₹80L–1.2Cr | ₹1.5–2Cr+ |

Always negotiate. The first offer is rarely the best offer. Ask for 15–20% above your target — you can always come down.

---

### Path B — High-paying clients

#### Target client types

- **Biotech founders** building drug discovery platforms who need an AI engineer but can't afford a full-time hire
- **CROs (Contract Research Organisations)** that want to add AI tooling to their workflows
- **Pharma startups** (Series A–C) that have scientists but no ML engineers
- **Academic labs** with grants looking to build bioinformatics pipelines

#### Where to find them

- **LinkedIn** — search "biotech founder", "computational biology", "drug discovery startup" and filter by 2nd-degree connections
- **X / Twitter** — the drug discovery AI community is very active here. Follow researchers at Recursion, Insilico, Isomorphic Labs
- **Toptal** — rigorous vetting but premium rates ($100–200/hr). Worth applying once your project is solid
- **Contra** — async-first freelance platform, good for project-based engagements
- **BioSpace** — job board that also surfaces consulting opportunities in life sciences

#### The warm-before-cold engagement strategy

Do not cold DM immediately. Spend 2 weeks first:

1. **Follow** 15–20 target people on LinkedIn and X
2. **Read** their recent posts and papers
3. **Comment** thoughtfully — not "great post!" but something that adds a perspective or asks a specific question
4. **After 3–5 interactions**, send the DM

Your DM after warming up:

```
Hi [Name],

I've been following your work on [specific project or paper] — 
the approach you took to [specific thing] was interesting.

I recently built MolGen Lab, a generative AI tool for drug candidate 
design ([30-second demo link]). Given what you're building, 
I thought it might be relevant.

I'm available for project-based collaboration. No pressure — 
just wanted to share the work.

Ashraf
```

**Conversion rate of warm DM vs cold DM: roughly 10×.**

#### Rate targets

| Engagement type | Rate |
|---|---|
| Short project (2–4 weeks) | $80–120/hr · ₹5–8L fixed |
| Medium project (1–3 months) | $70–100/hr · ₹10–20L fixed |
| Ongoing retainer | $5,000–10,000/month · ₹4–8L/month |
| Full consulting engagement | Negotiated, project-scoped |

Start at the higher end. Clients who push back hard on rate are often the hardest to work with.

---

## The interview ace card

When you get to interviews, MolGen Lab becomes your answer to almost every question.

| Interview question | Your answer |
|---|---|
| "Tell me about a technical challenge" | The SMILES validity filtering problem — unconditional generation had ~65% validity, had to implement a retry loop with max_attempts cap |
| "What do you know about drug discovery?" | Lipinski's Rule of 5, SMILES notation, ChEMBL, the role of generative models vs virtual screening |
| "Show us something you've built" | Open browser, demo live — type EGFR, show results |
| "Why do you want to work in this space?" | Genuine answer: the scale of impact. A better algorithm means a cure for a disease that's killed millions |
| "What's your ML background?" | Production ML on healthcare data at Fitwell.ai, built a generative molecule model from scratch for MolGen Lab |
| "Do you have bioinformatics experience?" | ChEMBL API integration, RDKit cheminformatics pipeline, SMILES parsing and validation |

**The preparation that matters most:** being able to explain Lipinski's Rule of 5, what a SMILES string is, and what MolGPT does — in plain English, not jargon. Domain fluency is what separates you from pure ML engineers applying to the same roles.

---

## Timeline

| Week | Action |
|---|---|
| Weeks 1–8 | Build MolGen Lab (20 Cursor prompts) |
| Week 9 | Polish, deploy, record Loom |
| Week 10 | LinkedIn post, resume update, case study |
| Week 10–11 | Begin warm engagement with 15–20 targets |
| Week 11–12 | Start applications (8–10 companies) + client outreach |
| Week 12–14 | Interviews + client conversations |
| Week 14–16 | Offers + negotiation |

---

## The mindset shift

Most people build a project, put it on GitHub, then wait.

The project is not the thing. **The signal you extract from the project is the thing.**

The Loom video, the LinkedIn post, the specific outreach, the case study — these are what convert the work into conversations, and conversations into offers. The code is proof. The story is what gets people to look at the proof.

You're 26 on March 31st. This project, done well and distributed deliberately, is a genuinely strong opening move into one of the most meaningful and well-paid intersections in tech.

---

*MolGen Lab Playbook — Ashraf, Mumbai 🇮🇳*  
*Built at the intersection of AI, healthcare, and the ambition to leave something lasting.*
