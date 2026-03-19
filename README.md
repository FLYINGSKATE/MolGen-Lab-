# 🧬 MolGen Lab

> **Generative AI for Drug Discovery** — A full-stack platform that designs novel drug candidate molecules for a given disease target using pre-trained generative models, scores them for drug-likeness, and visualises results in a React dashboard.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-orange?style=flat-square&logo=pytorch)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=flat-square)
![React](https://img.shields.io/badge/React-TypeScript-61DAFB?style=flat-square&logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green?style=flat-square&logo=fastapi)
![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)

---

## What this project does

Drug discovery traditionally takes 12–15 years and costs $2 billion per approved drug. Most of that time is spent in the early stages — identifying *which molecules* are even worth testing.

MolGen Lab compresses that search using generative AI:

1. You provide a **target protein** (e.g. EGFR, a driver of lung cancer)
2. A **pre-trained generative model** proposes novel molecule candidates as SMILES strings
3. Each candidate is **scored** for drug-likeness (Lipinski's Rule of 5), predicted toxicity, and estimated binding affinity
4. A **React dashboard** displays ranked candidates with 2D structure visualisations and property cards

This is the same paradigm used by companies like Recursion Pharmaceuticals, Insilico Medicine, and Aganitha.ai — just open-source and learnable.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend (React/TS)                   │
│   Target input → Generation trigger → Molecule result cards  │
└──────────────────────────┬──────────────────────────────────┘
                           │ REST API
┌──────────────────────────▼──────────────────────────────────┐
│                      Backend (FastAPI)                        │
│  /generate  →  MolGPT / REINVENT model (HuggingFace)         │
│  /score     →  RDKit scoring pipeline                         │
│  /visualise →  RDKit 2D structure renderer (SVG)              │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│              Data Layer                                       │
│  ChEMBL database (reference molecules)                        │
│  Local SQLite cache (generated candidates)                    │
└─────────────────────────────────────────────────────────────┘
```

---

## Tech stack

| Layer | Technology | Why |
|---|---|---|
| Molecule generation | MolGPT (HuggingFace) | Pre-trained GPT-2 style model fine-tuned on SMILES |
| Molecule manipulation | RDKit | Industry-standard cheminformatics library |
| Property prediction | DeepChem + RDKit | Lipinski, toxicity, logP scoring |
| Backend API | FastAPI + Python 3.11 | Fast, typed, async |
| Frontend | React 18 + TypeScript + Tailwind | Interactive dashboard |
| Structure visualisation | RDKit SVG renderer | 2D molecular diagrams |
| Data source | ChEMBL REST API | 2.4M bioactive molecules reference set |
| Deployment | HuggingFace Spaces (backend) + Vercel (frontend) | Free tier, shareable |
| Cloud (optional) | AWS Lambda + S3 | Production-grade deployment |

---

## Project structure

```
molgen-lab/
├── backend/
│   ├── main.py                  # FastAPI app entry point
│   ├── models/
│   │   ├── generator.py         # MolGPT wrapper
│   │   └── scorer.py            # RDKit + DeepChem scoring
│   ├── utils/
│   │   ├── smiles.py            # SMILES validation & parsing
│   │   ├── visualiser.py        # RDKit SVG renderer
│   │   └── chembl.py            # ChEMBL API client
│   ├── db/
│   │   └── database.py          # SQLite session store
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── TargetInput.tsx       # Disease target search
│   │   │   ├── MoleculeCard.tsx      # Single candidate card
│   │   │   ├── MoleculeGrid.tsx      # Results grid
│   │   │   ├── PropertyBadge.tsx     # Drug-likeness badges
│   │   │   └── StructureViewer.tsx   # SVG molecule renderer
│   │   ├── hooks/
│   │   │   └── useGenerate.ts        # API call hook
│   │   ├── types/
│   │   │   └── molecule.ts           # TypeScript interfaces
│   │   └── App.tsx
│   ├── package.json
│   └── tsconfig.json
├── notebooks/
│   ├── 01_smiles_basics.ipynb        # Learn SMILES & RDKit
│   ├── 02_molecule_properties.ipynb  # Lipinski, logP, toxicity
│   ├── 03_molGPT_generation.ipynb    # Run the generative model
│   └── 04_full_pipeline.ipynb        # End-to-end walkthrough
├── data/
│   └── sample_targets.json           # 10 example disease targets
└── README.md
```

---

## Getting started

### Prerequisites

- Python 3.11+
- Node.js 20+
- Git

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/molgen-lab.git
cd molgen-lab
```

### 2. Set up the backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at `http://localhost:8000`. Visit `/docs` for the auto-generated Swagger UI.

### 3. Set up the frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`.

### 4. Run a generation

Open the app, type `EGFR` in the target input, set the number of candidates to 20, and click **Generate**. Watch molecules appear.

---

## Key concepts (read this if you're learning)

### What is a SMILES string?

SMILES (Simplified Molecular Input Line Entry System) is how molecules are represented as text. For example, aspirin is:

```
CC(=O)Oc1ccccc1C(=O)O
```

Every atom, bond, ring, and branch is encoded in that string. Generative models learn to produce valid SMILES strings the same way LLMs learn to produce valid sentences.

### What is Lipinski's Rule of 5?

A heuristic filter that predicts whether a molecule is likely to be orally bioavailable (i.e., a pill you can swallow, not just an injection). A drug candidate passes if:

- Molecular weight ≤ 500 Da
- LogP (lipophilicity) ≤ 5
- Hydrogen bond donors ≤ 5
- Hydrogen bond acceptors ≤ 10

RDKit calculates all of these for us from the SMILES string.

### What is MolGPT?

MolGPT is a GPT-2 style transformer trained on ~1.5 million SMILES strings from the ZINC and ChEMBL databases. It learns the "grammar" of valid molecules. Given a prompt (or a target condition), it generates novel SMILES strings that are chemically valid and drug-like — molecules that may never have existed before.

### Why Graph Neural Networks matter here

Molecules are naturally graphs — atoms are nodes, bonds are edges. GNNs can encode this structure directly. More advanced versions of this project replace the MolGPT approach with GNN-based models like JTVAE or GraphAF, which generate molecules by constructing the graph atom-by-atom.

---

## API reference

### `POST /generate`

Generate novel molecule candidates for a given target.

```json
{
  "target": "EGFR",
  "num_candidates": 20,
  "temperature": 0.8
}
```

Response:

```json
{
  "candidates": [
    {
      "smiles": "CC1=CC=C(C=C1)NC2=NC=CC(=N2)NC3=CC=CC=C3",
      "valid": true,
      "drug_likeness_score": 0.84,
      "lipinski_pass": true,
      "logp": 3.2,
      "molecular_weight": 341.4,
      "toxicity_score": 0.12,
      "structure_svg": "<svg>...</svg>"
    }
  ]
}
```

### `POST /score`

Score an existing SMILES string.

```json
{ "smiles": "CC(=O)Oc1ccccc1C(=O)O" }
```

### `GET /targets`

Returns a list of well-known drug target proteins with descriptions.

---

## Roadmap

- [x] Core SMILES generation pipeline
- [x] RDKit scoring (Lipinski, logP, molecular weight)
- [x] FastAPI backend with Swagger docs
- [x] React dashboard with molecule cards
- [ ] Binding affinity prediction using AutoDock-GPU
- [ ] GNN-based generation with GraphAF
- [ ] Fine-tuning MolGPT on a specific disease target dataset
- [ ] Quantum molecular simulation module (Qiskit + VQE)
- [ ] Multi-parameter optimisation (REINVENT 4 integration)
- [ ] User accounts + generation history

---

## Learning resources

| Resource | What you'll learn |
|---|---|
| [RDKit Getting Started](https://www.rdkit.org/docs/GettingStartedInPython.html) | Manipulating molecules in Python |
| [DeepChem Tutorials](https://deepchem.io/tutorials/) | ML on molecular data |
| [MolGPT on HuggingFace](https://huggingface.co/entropy/gpt2_zinc_87m) | The generative model we use |
| [ChEMBL Database](https://www.ebi.ac.uk/chembl/) | Reference bioactive molecules |
| [Practical Cheminformatics (Pat Walters)](https://practicalcheminformatics.blogspot.com) | Best blog in the space |
| [Papers With Code — Molecule Generation](https://paperswithcode.com/task/molecule-generation) | State of the art models |

---

## Why I built this

I'm a full-stack software engineer transitioning into computational drug discovery. This project was my entry point into the field — learning how molecules are represented, how generative AI can explore chemical space, and how to build a usable tool on top of research-grade models.

The goal is to bridge the gap between ML research and wet-lab scientists who need usable software — not just Jupyter notebooks.

---

## Contributing

PRs welcome. If you're a cheminformatics researcher who wants a better frontend, or a frontend engineer who wants to learn the biology, this is a good place to meet in the middle.

---

## License

MIT — use it, learn from it, build on it.

---

*Built by Ashraf — Software Engineer at the intersection of AI and healthcare.*
*Mumbai, India 🇮🇳*
