from agent import run_research_agent

def test_memo_has_required_sections():
    result = run_research_agent("AI flashcard tool for German medical students")
    
    required = [
        "Decision Memo",
        "Verdict",
        "Market Attractiveness",
        "Customer & Problem Validation",
        "Competitive Landscape",
        "Business Viability",
        "Final Scorecard",
    ]
    
    for section in required:
        assert section in result, f"Missing section: {section}"

if __name__ == "__main__":
    test_memo_has_required_sections()
    print("✅ All smoke tests passed")