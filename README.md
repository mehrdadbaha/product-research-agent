# 🔍 AI Product Research Agent

An autonomous AI agent that turns a one-line product idea into a structured **decision memo**:
“Should we build this, and why now?”

**Live app:** https://pro-duct-research-agent-mehrdad.streamlit.app/  
**Code:** https://github.com/mehrdadbaha/product-research-agent

---

## What It Does

Input:  
> `"Freelancer tax autopilot for Germany"`  

Output (in ~60–120 seconds):

- Market attractiveness (TAM / SAM / SOM, growth rate, timing)
- Customer & problem validation (ICP, pain intensity, current alternatives, behavior evidence)
- Competitive landscape (5–8 real competitors, pricing, weaknesses, funding)
- Business viability & GTM (monetization model, CAC/LTV intuition, first 100 customers plan)
- Final scorecard out of 50 with a Build / Don’t Build / Test recommendation

This is designed as a **PM decision tool**, not just a generic market research report.

---

## Tech Stack

| Layer | Tool |
|-------|------|
| LLM | OpenAI `gpt-4o-mini` |
| Agent framework | LangChain + LangGraph (`create_react_agent`) |
| Web search | Tavily Search API |
| UI | Streamlit |
| Language | Python 3.10+ |

---

## How It Works

1. **User prompt** — you provide a product idea (e.g., “AI exam coach for German university students”).
2. **Agent loop** — LangGraph’s `create_react_agent` runs a ReAct loop:
   - Calls Tavily search multiple times (market size, competitors, reviews, trends)
   - Reads each result and decides what to search next
3. **Synthesis** — GPT-4o-mini composes a structured **decision memo** with:
   - Market attractiveness
   - Customer & problem validation
   - Competitive landscape & wedge
   - Business viability & GTM
   - Scorecard with Build / Don’t Build / Test recommendation
4. **UI** — Streamlit renders the memo as clean Markdown in the browser.

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/mehrdadbaha/product-research-agent.git
cd product-research-agent

# Create & activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your API keys in a .env file
# .env
# OPENAI_API_KEY=sk-...
# TAVILY_API_KEY=tvly-...

# Run the Streamlit app
streamlit run streamlit_app.py
```

---

## Prompt & Agent Design

The agent is guided by a **decision-memo prompt** structured in 5 sections:

1. **Market Attractiveness**  
   - TAM / SAM / SOM  
   - Growth & timing (“Why now?”)  
   - Geography focus (Berlin / Germany / Europe)  

2. **Customer & Problem Validation**  
   - ICP (who exactly is the buyer/user?)  
   - Pain intensity & current alternatives  
   - Behavior evidence (Reddit, G2, job posts, reviews)  

3. **Competitive Landscape & Positioning**  
   - 5–8 competitors (direct, indirect, substitutes)  
   - Pricing, weaknesses, funding  
   - Positioning wedge (faster / cheaper / AI-native / vertical-specific / local)  

4. **Business Viability & Go-to-Market**  
   - Monetization model and rough unit economics intuition  
   - First 100 customers strategy  
   - Key risks (regulation, sales cycle, switching costs)  

5. **Scorecard & Verdict**  
   - 5 criteria scored /10 → total /50  
   - Build / Don’t Build / Test recommendation  

---

## Why I Built This

As a **Business & Engineering master’s student in Berlin** transitioning toward product roles, I wanted a project that:

- Shows I can go beyond “chatbot demos” to **decision-support tools**
- Combines **market research, strategy thinking, and AI tooling**
- Is directly relevant to **Berlin startup PM / strategy roles**


---

## Possible Next Steps

- Add caching to reduce API cost for repeated ideas  
- Support multiple personas (VC analyst, PM, founder) with different memo styles  
- Export the decision memo as PDF for pitch decks  
- Add a “Berlin-only” mode focusing on DACH market data
