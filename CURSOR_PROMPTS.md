# MolGen Lab — Cursor Prompts (Sequential Build Guide)

Use these prompts one by one inside Cursor IDE. Each prompt builds on the last.
Read the "BEFORE YOU RUN THIS" note before each prompt.
The project will be fully functional by Prompt 20.

---

## PROMPT 01 — Project scaffold

> BEFORE YOU RUN THIS: Create a new empty folder called `molgen-lab`. Open it in Cursor. Run this prompt first.

```
Create a full-stack project scaffold called molgen-lab with this structure:

molgen-lab/
  backend/
    main.py
    requirements.txt
    models/  (empty, add __init__.py)
    utils/   (empty, add __init__.py)
    db/      (empty, add __init__.py)
  frontend/  (empty for now)
  notebooks/ (empty for now)
  data/
    sample_targets.json
  .gitignore
  README.md  (just a placeholder title for now)

In sample_targets.json, add 5 well-known drug targets as a JSON array:
[
  { "id": "EGFR", "name": "Epidermal Growth Factor Receptor", "disease": "Lung cancer", "description": "A protein that when mutated drives uncontrolled cell division" },
  ...add 4 more: BRCA1 (breast cancer), ACE2 (COVID-19), BRAF (melanoma), DRD2 (schizophrenia)
]

In .gitignore include: __pycache__, *.pyc, venv/, node_modules/, .env, *.db

Explain what each folder does in a comment at the top of main.py.
```

---

## PROMPT 02 — Backend dependencies

> BEFORE YOU RUN THIS: Make sure Python 3.11+ is installed. You'll install libraries here.

```
In backend/requirements.txt, add all required dependencies for this project:
- fastapi
- uvicorn[standard]
- rdkit (note: installed via conda or pip as rdkit-pypi)
- deepchem
- torch
- transformers
- huggingface_hub
- requests
- python-dotenv
- sqlalchemy
- aiosqlite
- pydantic

Then write a setup guide comment at the top of requirements.txt explaining:
1. Create a virtual environment: python -m venv venv
2. Activate it
3. pip install -r requirements.txt
4. Note that rdkit may need: pip install rdkit-pypi

Also create a backend/.env.example file with:
HUGGINGFACE_TOKEN=your_token_here
CHEMBL_BASE_URL=https://www.ebi.ac.uk/chembl/api/data
```

---

## PROMPT 03 — Understanding SMILES (learning notebook)

> BEFORE YOU RUN THIS: This prompt creates your first Jupyter notebook. Run `pip install jupyter` if needed, then open the notebook after it's created.

```
Create notebooks/01_smiles_basics.ipynb as a Jupyter notebook that teaches SMILES notation from scratch.

The notebook should have these sections, each as markdown + code cells:

1. "What is a SMILES string?" — explain it's a text representation of a molecule. Show examples: water (O), ethanol (CCO), aspirin (CC(=O)Oc1ccccc1C(=O)O), caffeine.

2. "Installing and importing RDKit" — code cell that imports RDKit and checks version.

3. "Parsing a SMILES string" — use Chem.MolFromSmiles() to load aspirin. Print the number of atoms and bonds.

4. "Drawing a molecule" — use Draw.MolToImage() to render aspirin as an image in the notebook.

5. "Validating SMILES" — write a function is_valid_smiles(smiles: str) -> bool that returns True if RDKit can parse it, False otherwise. Test it on 3 valid and 2 invalid strings.

6. "Molecular properties" — use Descriptors module to print: molecular weight, logP, number of H-bond donors/acceptors for aspirin.

7. "Lipinski's Rule of 5" — write a function lipinski_pass(smiles: str) -> dict that returns all 4 Lipinski properties and a boolean pass/fail. Test on aspirin and caffeine.

8. "Your turn" — a markdown cell prompting the reader to try their own molecule using PubChem to find SMILES strings.

Write clean, well-commented code. Use markdown cells generously — this is a learning resource.
```

---

## PROMPT 04 — MolGPT exploration notebook

> BEFORE YOU RUN THIS: Make sure your HuggingFace account is set up at huggingface.co. Get a free token from Settings > Access Tokens.

```
Create notebooks/02_molGPT_generation.ipynb that explores the MolGPT model from HuggingFace.

Sections:

1. "What is MolGPT?" — markdown explanation: it's a GPT-2 model trained on 1.5M SMILES strings from ZINC database. It learns the grammar of valid molecules.

2. "Load the model" — code cell to load the model:
   from transformers import GPT2LMHeadModel, GPT2Tokenizer
   model_name = "entropy/gpt2_zinc_87m"
   tokenizer = GPT2Tokenizer.from_pretrained(model_name)
   model = GPT2LMHeadModel.from_pretrained(model_name)

3. "Generate raw SMILES" — generate 10 SMILES strings using model.generate() with temperature=0.8, max_length=100. Print raw output.

4. "Filter valid molecules" — use is_valid_smiles() from notebook 01 to filter only valid outputs. Print how many passed.

5. "Visualise the valid ones" — use RDKit Draw.MolsToGridImage() to show all valid molecules in a grid.

6. "Score them" — apply the lipinski_pass() function to each valid SMILES. Show a summary table.

7. "Observations" — markdown cell: what patterns do you notice? Which molecules look drug-like?

Add a note: "In production, generation is conditioned on a specific target. Here we're doing unconditional generation to understand the model first."
```

---

## PROMPT 05 — Scoring pipeline module

> BEFORE YOU RUN THIS: This is the first real backend module. It lives in backend/models/scorer.py.

```
Create backend/models/scorer.py — a MoleculeScorer class that takes a SMILES string and returns a full scoring report.

The class should have these methods:

1. __init__(self) — import rdkit modules, set up any configuration

2. validate(self, smiles: str) -> bool — returns True if RDKit can parse the SMILES

3. lipinski(self, smiles: str) -> dict — returns:
   { mol_weight: float, logp: float, h_donors: int, h_acceptors: int, passes: bool }
   A molecule passes if all 4 Lipinski rules are satisfied.

4. drug_likeness_score(self, smiles: str) -> float — return a score from 0.0 to 1.0 combining:
   - Lipinski pass (40% weight)
   - QED score from RDKit (Quantitative Estimate of Drug-likeness) (60% weight)

5. toxicity_estimate(self, smiles: str) -> float — a simple heuristic toxicity score 0.0 to 1.0 based on:
   - Presence of known toxic substructures (nitro groups, heavy metals, reactive groups)
   - Use RDKit's HasSubstructMatch for SMARTS patterns
   - Return 0.0 = not toxic, 1.0 = very likely toxic

6. full_report(self, smiles: str) -> dict — runs all of the above and returns:
   {
     smiles: str,
     valid: bool,
     lipinski: dict,
     drug_likeness_score: float,
     toxicity_score: float,
     overall_rank_score: float  # drug_likeness * (1 - toxicity)
   }

At the bottom of the file, include a quick test: if __name__ == "__main__" — test on aspirin SMILES and print the full report.

Add docstrings and type hints throughout.
```

---

## PROMPT 06 — Generator module

> BEFORE YOU RUN THIS: The scorer from Prompt 05 must exist.

```
Create backend/models/generator.py — a MoleculeGenerator class wrapping the MolGPT HuggingFace model.

Methods:

1. __init__(self, model_name: str = "entropy/gpt2_zinc_87m") — load model and tokenizer from HuggingFace. Print "Model loaded." when done.

2. generate_candidates(self, num_candidates: int = 20, temperature: float = 0.8, max_length: int = 100) -> list[str]
   - Generate raw text from the model
   - Parse out SMILES tokens
   - Return a list of raw (not yet validated) SMILES strings

3. generate_valid(self, num_candidates: int = 20, temperature: float = 0.8, max_attempts: int = 100) -> list[str]
   - Keep generating until we have num_candidates valid SMILES
   - Use RDKit Chem.MolFromSmiles() to validate each one
   - Cap at max_attempts to avoid infinite loops
   - Return only valid SMILES strings

4. generate_and_score(self, num_candidates: int = 20, scorer=None) -> list[dict]
   - Call generate_valid()
   - If scorer is provided, run scorer.full_report() on each
   - Sort results by overall_rank_score descending
   - Return sorted list of dicts

Add type hints, docstrings, and a __main__ test block that generates 5 molecules and prints them.
```

---

## PROMPT 07 — Structure visualiser utility

> BEFORE YOU RUN THIS: Prompts 05 and 06 must be complete.

```
Create backend/utils/visualiser.py — functions that convert SMILES strings to visual representations.

Functions:

1. smiles_to_svg(smiles: str, width: int = 300, height: int = 200) -> str
   - Use RDKit Draw.MolToImage() and then convert to SVG using Draw.rdMolDraw2D
   - Return the SVG as a string
   - Return an empty string if SMILES is invalid

2. smiles_to_base64_png(smiles: str, width: int = 300, height: int = 200) -> str
   - Render the molecule as a PNG image using RDKit
   - Convert to base64 string for embedding in JSON
   - Return empty string if invalid

3. batch_to_svg_grid(smiles_list: list[str], mols_per_row: int = 4) -> str
   - Use RDKit's Draw.MolsToGridImage() to render multiple molecules
   - Return as SVG string

4. highlight_lipinski_violations(smiles: str) -> dict
   - Return a dict with which Lipinski rules the molecule violates, if any
   - { "violations": ["mol_weight > 500", "logP > 5"], "pass": False }

Add a __main__ test that renders aspirin and prints the first 200 characters of the SVG.
```

---

## PROMPT 08 — ChEMBL API client

> BEFORE YOU RUN THIS: This calls the public ChEMBL REST API (no key needed).

```
Create backend/utils/chembl.py — a ChEMBLClient class for fetching reference data.

Methods:

1. __init__(self) — set base URL to https://www.ebi.ac.uk/chembl/api/data and set default headers for JSON

2. search_target(self, query: str) -> list[dict]
   - GET /target.json?search={query}&limit=5
   - Return list of targets with: { target_chembl_id, pref_name, organism, target_type }

3. get_compounds_for_target(self, target_id: str, limit: int = 20) -> list[str]
   - Fetch known active compounds for a ChEMBL target ID
   - GET /activity.json?target_chembl_id={target_id}&limit={limit}
   - Extract and return SMILES strings from the response
   - These serve as reference "known drug" molecules for comparison

4. get_molecule_by_smiles(self, smiles: str) -> dict | None
   - Search ChEMBL for a molecule matching the given SMILES
   - Return basic metadata if found

Add error handling for failed API calls (return empty list / None gracefully).
Add a __main__ test that searches for "EGFR" and prints the first result.
```

---

## PROMPT 09 — Database layer

> BEFORE YOU RUN THIS: SQLite will be created automatically. No setup needed.

```
Create backend/db/database.py — a SQLite session store for saving generation results.

Use SQLAlchemy with async support (aiosqlite).

Tables to create:

1. generation_sessions
   - id: int (primary key, autoincrement)
   - target: str
   - created_at: datetime
   - num_requested: int
   - num_valid: int

2. molecules
   - id: int (primary key)
   - session_id: int (foreign key → generation_sessions)
   - smiles: str
   - drug_likeness_score: float
   - toxicity_score: float
   - overall_rank_score: float
   - lipinski_pass: bool
   - mol_weight: float
   - logp: float
   - structure_svg: text (the SVG string)
   - rank: int (position in sorted results)

Functions to implement:
- create_tables() — create all tables if not exist
- save_session(target, results) -> int — saves a session + all its molecules, returns session_id
- get_session(session_id) -> dict — retrieves a full session with all molecules
- get_recent_sessions(limit=10) -> list — returns last N sessions (without molecule details)

Use SQLAlchemy ORM models with proper relationships.
```

---

## PROMPT 10 — FastAPI main app

> BEFORE YOU RUN THIS: All backend modules (Prompts 05–09) must exist.

```
Create backend/main.py — the FastAPI application connecting all backend modules.

Imports and setup:
- Import FastAPI, CORS middleware
- Import MoleculeGenerator, MoleculeScorer, ChEMBLClient, visualiser functions, database functions
- Enable CORS for http://localhost:5173 (our React frontend)

Pydantic request/response models:
- GenerateRequest: { target: str, num_candidates: int = 20, temperature: float = 0.8 }
- MoleculeResult: { smiles, valid, drug_likeness_score, toxicity_score, overall_rank_score, lipinski_pass, mol_weight, logp, structure_svg }
- GenerateResponse: { session_id: int, target: str, candidates: list[MoleculeResult], generated_at: str }

Endpoints:

1. GET / — health check, returns { status: "ok", message: "MolGen Lab API" }

2. GET /targets — returns the sample_targets.json data as JSON

3. POST /generate
   - Accept GenerateRequest
   - Run generator.generate_and_score(num_candidates, scorer)
   - For each result, generate SVG via smiles_to_svg()
   - Save to database via save_session()
   - Return GenerateResponse

4. POST /score
   - Accept { smiles: str }
   - Run scorer.full_report() + smiles_to_svg()
   - Return the full report + SVG

5. GET /sessions — return recent sessions from DB

6. GET /sessions/{session_id} — return full session with all molecules

Initialise the generator and scorer as singletons on startup (use FastAPI lifespan events).
Add proper HTTPException handling for invalid SMILES, model errors, etc.
```

---

## PROMPT 11 — TypeScript types and API client

> BEFORE YOU RUN THIS: Run `npm create vite@latest frontend -- --template react-ts` in the molgen-lab root, then cd into frontend and run `npm install`.

```
Create frontend/src/types/molecule.ts with all TypeScript interfaces:

export interface Target {
  id: string;
  name: string;
  disease: string;
  description: string;
}

export interface LipinskiData {
  mol_weight: number;
  logp: number;
  h_donors: number;
  h_acceptors: number;
  passes: boolean;
}

export interface MoleculeResult {
  smiles: string;
  valid: boolean;
  drug_likeness_score: number;
  toxicity_score: number;
  overall_rank_score: number;
  lipinski_pass: boolean;
  mol_weight: number;
  logp: number;
  structure_svg: string;
  rank?: number;
}

export interface GenerateResponse {
  session_id: number;
  target: string;
  candidates: MoleculeResult[];
  generated_at: string;
}

export type GenerationStatus = 'idle' | 'loading' | 'success' | 'error';

Then create frontend/src/api/client.ts:
- A typed API client using fetch
- Base URL from env: VITE_API_URL or fallback to http://localhost:8000
- Functions: getTargets(), generateMolecules(target, numCandidates, temperature), scoreMolecule(smiles)
- Each function properly typed with the interfaces above
- Each function has try/catch and throws a typed ApiError on failure
```

---

## PROMPT 12 — useGenerate hook

> BEFORE YOU RUN THIS: Types and API client (Prompt 11) must exist.

```
Create frontend/src/hooks/useGenerate.ts — a React hook managing the full generation flow.

The hook should:
1. Expose state: { status: GenerationStatus, results: MoleculeResult[], error: string | null, sessionId: number | null }
2. Expose actions: { generate(target: string, numCandidates: number, temperature: number): Promise<void>, reset(): void }
3. Handle loading state (status = 'loading') during the API call
4. On success: set results sorted by overall_rank_score descending, set status = 'success'
5. On error: set error message, set status = 'error'
6. reset() clears all state back to idle

Also create frontend/src/hooks/useTargets.ts:
- Fetches the /targets endpoint on mount
- Returns { targets: Target[], loading: boolean, error: string | null }
```

---

## PROMPT 13 — PropertyBadge and StructureViewer components

> BEFORE YOU RUN THIS: Install Tailwind: follow Vite+Tailwind setup for React.

```
Create two small reusable components:

frontend/src/components/PropertyBadge.tsx
- Props: { label: string, value: string | number, type: 'success' | 'warning' | 'danger' | 'neutral' }
- Renders a small badge pill showing label: value
- Colour coded: success = green, warning = amber, danger = red, neutral = gray
- Clean, minimal Tailwind styling — no borders, just background colour with matching text

frontend/src/components/StructureViewer.tsx
- Props: { svg: string, smiles: string, size?: 'sm' | 'md' | 'lg' }
- Renders the SVG string as dangerouslySetInnerHTML inside a div
- Shows a "Copy SMILES" button below the structure — clicking copies the SMILES string to clipboard and shows a brief "Copied!" confirmation
- If svg is empty, shows a placeholder grey box with the text "No structure available"
- Sizes: sm = 150px, md = 250px (default), lg = 350px
```

---

## PROMPT 14 — MoleculeCard component

> BEFORE YOU RUN THIS: PropertyBadge and StructureViewer (Prompt 13) must exist.

```
Create frontend/src/components/MoleculeCard.tsx

Props: { molecule: MoleculeResult, rank: number }

The card should show:
- Rank badge in top-left corner (e.g. "#1")
- StructureViewer (size="md") centered in the card
- Overall rank score as a large number (e.g. "0.87") with label "Drug score"
- PropertyBadges for: Drug-likeness, Toxicity risk, Mol. weight, LogP
- Lipinski pass/fail as a coloured status line at the bottom: green "✓ Lipinski pass" or red "✗ Lipinski fail"
- Hover state: subtle shadow lift

Colour the rank score: 
- ≥ 0.7 = green text
- 0.4–0.69 = amber text  
- < 0.4 = red text

Toxicity badge:
- score < 0.2 = success ("Low")
- 0.2–0.5 = warning ("Medium")
- > 0.5 = danger ("High")

Use clean Tailwind. The card should feel like a polished data card — not a demo.
```

---

## PROMPT 15 — TargetInput component

> BEFORE YOU RUN THIS: useTargets hook and types must exist.

```
Create frontend/src/components/TargetInput.tsx

Props: { onGenerate: (target: string, numCandidates: number, temperature: number) => void, disabled: boolean }

The component renders a clean input panel:

1. A search/select for the disease target:
   - Text input for typing a target name
   - Below it, show quick-select buttons for each target from useTargets() (e.g. "EGFR", "BRCA1")
   - Clicking a quick-select fills the input

2. A slider for "Number of candidates" (5–50, default 20) showing the current value

3. A slider for "Temperature" (0.5–1.2, default 0.8, step 0.1) with a label explaining: "Lower = more conservative molecules. Higher = more creative."

4. A large "Generate Molecules" button — disabled when disabled prop is true or target input is empty
   - While disabled (loading state), show a spinner + "Generating..."

5. A small info text below: "Generation takes ~30 seconds. Results are scored and ranked automatically."

Clean layout. The whole component should feel like a focused tool, not a form.
```

---

## PROMPT 16 — MoleculeGrid and results section

> BEFORE YOU RUN THIS: MoleculeCard (Prompt 14) must exist.

```
Create frontend/src/components/MoleculeGrid.tsx

Props: { molecules: MoleculeResult[], status: GenerationStatus }

Behaviour:
- status = 'idle': show an empty state — a subtle illustration placeholder and text "Enter a target above to generate drug candidates"
- status = 'loading': show a loading skeleton — 6 grey placeholder cards in a grid, pulsing (CSS animation)
- status = 'error': show error state with a message
- status = 'success': render molecules in a responsive grid

For the success grid:
- Display molecules sorted by rank (already sorted from the hook)
- Show a summary bar at top: "Generated {n} candidates for {target} — {m} passed Lipinski filter"
- Responsive grid: 1 col on mobile, 2 on tablet, 3 on desktop
- Each MoleculeCard gets its rank (1-indexed)
- Add a "Sort by" toggle: Overall score | Drug-likeness | Toxicity (lowest)
- Add a "Filter" toggle: All | Lipinski pass only

The loading skeleton should match the MoleculeCard dimensions exactly so there's no layout shift.
```

---

## PROMPT 17 — App.tsx and main layout

> BEFORE YOU RUN THIS: All components and hooks must exist.

```
Rewrite frontend/src/App.tsx as the main application layout.

Layout:
- Full-width header: "🧬 MolGen Lab" on the left, subtitle "Generative AI for Drug Discovery" on the right
- Below header: TargetInput component
- Below that: MoleculeGrid component
- Footer: "Built with MolGPT · RDKit · HuggingFace · React" — minimal, centered

Wire everything together:
- Use useGenerate hook for state
- Pass generate function to TargetInput's onGenerate prop
- Pass results + status to MoleculeGrid
- TargetInput's disabled prop = status === 'loading'

Add a simple page-level error boundary using React's ErrorBoundary pattern.

Global styles (in index.css):
- Clean white background
- Inter or system-ui font
- Smooth scroll
- No other global overrides — Tailwind handles the rest

The overall feel should be: a focused research tool, clean and professional, not a portfolio toy.
```

---

## PROMPT 18 — Connect frontend to backend

> BEFORE YOU RUN THIS: Backend must be running on port 8000. Frontend on 5173.

```
Create frontend/.env.local:
VITE_API_URL=http://localhost:8000

Then update frontend/src/api/client.ts to handle the actual backend response shape — make sure all field names match exactly what FastAPI returns from Prompt 10.

Add a proxy config in frontend/vite.config.ts so that /api/* proxies to http://localhost:8000 in development. This avoids CORS issues during development.

Test the full flow:
1. In App.tsx, add a console.log in useGenerate when results arrive
2. Type "EGFR" in the target input, click Generate
3. Verify results appear in the browser console

Fix any field name mismatches between the Python response model (snake_case) and TypeScript (camelCase). Add a response transformer in client.ts that converts snake_case to camelCase on the way in.
```

---

## PROMPT 19 — Error handling, loading states, polish

> BEFORE YOU RUN THIS: Full flow should be working end-to-end from Prompt 18.

```
Polish pass across the whole app:

1. In TargetInput — if the API call fails, show a toast notification (build a simple Toast component — no library needed) that auto-dismisses after 4 seconds.

2. In MoleculeCard — add a "Details" expand section that shows the full SMILES string in a monospace code block, and a note: "Copy this SMILES to use in RDKit or draw at molview.org"

3. In MoleculeGrid summary bar — add a "Export CSV" button that downloads all molecule data as a CSV file (smiles, scores, properties). Implement this in pure JS using Blob and URL.createObjectURL. No library needed.

4. In App.tsx header — add a subtle animated gradient line under the header (CSS only, no JS). Use the colour palette: from blue-500 to purple-500 to teal-500 at 3s ease infinite.

5. In the loading skeleton — replace the pulsing grey boxes with a more specific skeleton that shows the outline structure of MoleculeCard (image placeholder block + badge rows).

6. Add favicon: a simple DNA/molecule emoji favicon in index.html.

7. Make it fully responsive — test at 375px (mobile), 768px (tablet), 1280px (desktop).
```

---

## PROMPT 20 — Deploy to HuggingFace Spaces + Vercel

> BEFORE YOU RUN THIS: Create accounts at huggingface.co and vercel.com (both free).

```
Prepare the project for deployment:

BACKEND — HuggingFace Spaces (Gradio SDK or Docker):

1. Create backend/app.py as an alternative entry point that works with HuggingFace Spaces
2. Create a Dockerfile in the backend folder:
   - FROM python:3.11-slim
   - Install system deps for RDKit
   - COPY requirements.txt and pip install
   - EXPOSE 7860
   - CMD uvicorn main:app --host 0.0.0.0 --port 7860
3. Create backend/README_spaces.md with the HuggingFace Spaces YAML frontmatter:
   ---
   title: MolGen Lab API
   emoji: 🧬
   colorFrom: blue
   colorTo: purple
   sdk: docker
   pinned: false
   ---

FRONTEND — Vercel:

1. Create frontend/vercel.json:
   { "rewrites": [{ "source": "/api/(.*)", "destination": "https://YOUR_HF_SPACE_URL/$1" }] }
2. Update frontend/.env.production: VITE_API_URL=https://YOUR_HF_SPACE_URL
3. Make sure `npm run build` completes without errors

FINAL CHECKLIST before pushing to GitHub:
- [ ] .env files are in .gitignore (never commit secrets)
- [ ] README.md is complete and accurate
- [ ] All notebooks run top-to-bottom without errors
- [ ] Backend /docs endpoint shows all routes correctly
- [ ] Frontend builds with no TypeScript errors
- [ ] The Generate flow works end-to-end at least once

Congrats — you just built a production-grade drug discovery AI tool from scratch. 🧬
```

---

## Tips for using these prompts with Cursor

1. **One prompt at a time.** Don't skip ahead — each builds on the last.
2. **Read the code Cursor generates.** Don't just run it — understand why each decision was made.
3. **When something breaks**, add to your next prompt: "The previous code has this error: [paste error]. Fix it and explain why it happened."
4. **Use Cursor's @codebase** feature to give it context from previously generated files.
5. **Ask follow-ups** like: "Explain how the MolGPT tokenizer works in generator.py line 34" — this is how you learn while building.

---

*MolGen Lab — built prompt by prompt. Mumbai → the world.*
