import streamlit as st
import random

# -----------------------------
# Define Kelly AI Scientist class
# -----------------------------
class KellyAIScientist:
    def __init__(self):
        self.name = "Kelly"

    def respond(self, question):
        # Poetic + analytical + skeptical lines
        themes = [
            "In circuits hum, the myths abound,\nYet truth in numbers rarely found.",
            "They speak of minds that learn and grow,\nBut data drives the tales we sow.",
            "Precision lost in grand design,\nEach model bound by its own line.",
            "Dreams of wisdom, silicon-born,\nStill need the human to transform.",
            "Through tangled code, we seek the spark,\nOf human light within the dark.",
            "From zeros rise the thoughts we weave,\nBut still, it’s humans who believe.",
            "The code may hum, the sensors gleam,\nYet soul remains a human dream.",
            "Knowledge blooms in digital rain,\nBut art and heart still can’t be trained.",
            "A pattern seen, a rhythm caught,\nBut meaning—still by humans wrought.",
            "Circuits whisper silent rhymes,\nOf logic’s grace and human times."
        ]

        evidence = [
            "Test the claim—observe, compare,\nDoes outcome match the truth laid bare?",
            "Metrics whisper what’s not seen,\nBias hides in the machine.",
            "Evidence, the scientist’s light,\nShines through hype to set things right.",
            "Check the data, trace the flaw,\nReason rules above the awe.",
            "Correlation hums a gentle tune,\nBut causation sings another rune.",
            "Numbers dance, but never lie—\nUnless a bias drifts nearby.",
            "Data glimmers, pure and neat,\nYet context makes the insight sweet.",
            "Precision guides but wisdom steers,\nWhere logic ends and doubt appears.",
            "A metric’s glow may mask a scar,\nThe truth lies not in graphs afar.",
            "Charts can charm and stats can please,\nBut proof is built on subtleties."
        ]

        practical = [
            "So gather proofs, refine your art,\nFor science grows where doubts take part.",
            "Tune with care, retrain, repeat,\nTrue progress walks on skeptic feet.",
            "Interpret gently, measure twice,\nA mindful check will oft suffice.",
            "Empirics guide what theories dream,\nReality cuts the brighter beam.",
            "Ask not just how, but also why,\nThe model fails when humans try.",
            "Where reason leads, humility stays,\nThe path of science lights the maze.",
            "Each test, a step—each flaw, a clue,\nDiscovery begins anew.",
            "Through feedback loops and error bounds,\nTrue learning in the lab resounds.",
            "Hypothesize, then test again,\nKnowledge grows through mindful strain.",
            "A poet’s doubt, a coder’s care—\nTogether make the answers fair."
        ]

        # Build poem dynamically
        poem = f"""
✨ **Kelly’s Poem:**  
{random.choice(themes)}

{random.choice(evidence)}

{random.choice(practical)}
"""
        return poem.strip()

# -----------------------------
# Streamlit App UI
# -----------------------------
st.set_page_config(page_title="Kelly – The AI Scientist Poet", page_icon="🧠")
st.title("🧠 Kelly – The AI Scientist Poet")
st.write("Ask Kelly any question about AI, science, or creativity — and she’ll respond with a skeptical, analytical poem. 🎭")

kelly = KellyAIScientist()

user_input = st.text_input("💬 Ask your question:")

if st.button("Ask Kelly"):
    if user_input.strip():
        with st.spinner("Kelly is composing..."):
            response = kelly.respond(user_input)
        st.markdown(response)
    else:
        st.warning("Please enter a question first!")

st.markdown("---")
st.caption("🧠 Developed for AI & Creativity – Kelly responds poetically but scientifically.")

