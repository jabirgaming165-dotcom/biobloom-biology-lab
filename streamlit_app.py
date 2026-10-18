
import streamlit as st

st.set_page_config(
    page_title="BioBloom Biology Lab",
    page_icon="🧬",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #07111f;
    color: #eef6ff;
}
[data-testid="stHeader"] {
    background: rgba(7,17,31,0.8);
}
h1, h2, h3 {
    color: #45f3dc !important;
}
.stTabs [data-baseweb="tab"] {
    color: #eef6ff;
}
div.stButton > button {
    background: #45f3dc;
    color: #07111f;
    border: 0;
    border-radius: 10px;
    font-weight: bold;
}
div.stButton > button:hover {
    background: #a78bfa;
    color: #07111f;
}
.lab-card {
    background: #101e30;
    padding: 20px;
    border: 1px solid #24364c;
    border-radius: 15px;
    margin: 10px 0;
}
.small-text {
    color: #9aacc2;
}
</style>
""", unsafe_allow_html=True)

LESSONS = {
    "Cells and Organelles": [
        "Cells are the basic structural and functional units of life.",
        "**Nucleus:** stores most of a eukaryotic cell's DNA.",
        "**Mitochondria:** carry out important stages of cellular respiration.",
        "**Ribosomes:** build proteins from amino acids.",
        "**Cell membrane:** controls what enters and leaves the cell.",
        "**Plant cells:** typically have a cell wall, chloroplasts, and a large central vacuole."
    ],
    "DNA and Genetics": [
        "DNA stores hereditary information in living organisms.",
        "**Base pairs:** adenine pairs with thymine; cytosine pairs with guanine.",
        "**Genes:** DNA sequences containing functional information.",
        "**Chromosomes:** structures made of DNA and associated proteins.",
        "**Mutations:** changes in genetic material that may have harmful, beneficial, or neutral effects."
    ],
    "Energy in Living Things": [
        "**Photosynthesis:** uses light energy to make sugars from carbon dioxide and water.",
        "**Chloroplasts:** the main sites of photosynthesis in plants and algae.",
        "**Cellular respiration:** releases usable energy from energy-rich molecules.",
        "**ATP:** a molecule cells use to transfer energy.",
        "**Enzymes:** biological catalysts that speed up chemical reactions."
    ],
    "Chemistry of Life": [
        "**Atoms:** units of chemical elements.",
        "**Molecules:** groups of atoms joined by chemical bonds.",
        "**Carbohydrates:** provide energy and can have structural roles.",
        "**Lipids:** include fats and oils; phospholipids are important in membranes.",
        "**Proteins:** have roles in structure, transport, signaling, and catalysis.",
        "**Nucleic acids:** DNA and RNA are involved in genetic information."
    ],
    "Cell Transport": [
        "**Diffusion:** net movement of particles from higher to lower concentration.",
        "**Osmosis:** net movement of water across a selectively permeable membrane.",
        "**Active transport:** uses energy to move substances against a concentration gradient.",
        "**Passive transport:** does not directly require cellular energy.",
        "**Homeostasis:** regulation of internal conditions within suitable ranges."
    ],
    "Ecology and Ecosystems": [
        "**Ecosystem:** living organisms interacting with their nonliving environment.",
        "**Producers:** organisms that make organic molecules using an energy source.",
        "**Consumers:** obtain energy by eating other organisms or organic material.",
        "**Decomposers:** break down dead material and help recycle nutrients.",
        "**Food webs:** connect feeding relationships in an ecosystem.",
        "**Biodiversity:** variety of life at genetic, species, and ecosystem levels."
    ]
}

QUESTIONS = [
    ("What is the basic unit of life?", ["Organ", "Cell", "Tissue", "Atom"], 1, "Cells are the basic units of life."),
    ("Which organelle stores most eukaryotic DNA?", ["Ribosome", "Nucleus", "Vacuole", "Golgi apparatus"], 1, "The nucleus stores most of a eukaryotic cell's DNA."),
    ("Which organelle produces much ATP during aerobic respiration?", ["Mitochondrion", "Cell wall", "Vacuole", "Ribosome"], 0, "Mitochondria carry out important stages of aerobic respiration."),
    ("What is the main function of ribosomes?", ["Store water", "Build proteins", "Capture sunlight", "Store chromosomes"], 1, "Ribosomes synthesize proteins."),
    ("What controls what enters and leaves a cell?", ["Chromosome", "Cell membrane", "Nucleolus", "Ribosome"], 1, "The cell membrane regulates movement into and out of cells."),
    ("Which structures are typical of plant cells?", ["Cell wall and chloroplasts", "Only ribosomes", "Only a nucleus", "No cell membrane"], 0, "Plant cells typically have cell walls and chloroplasts."),
    ("What does DNA stand for?", ["Dynamic Nuclear Atom", "Deoxyribonucleic acid", "Double Nitrogen Arrangement", "Deoxygenated RNA"], 1, "DNA stands for deoxyribonucleic acid."),
    ("Which DNA bases pair together?", ["A-C and G-T", "A-G and C-T", "A-T and C-G", "A-U and C-G"], 2, "A pairs with T, and C pairs with G in DNA."),
    ("What is a gene?", ["A type of organ", "A DNA sequence with functional information", "A cell membrane", "A sugar"], 1, "Genes are DNA sequences with functional information."),
    ("What do enzymes do?", ["Destroy all cells", "Store all DNA", "Speed up chemical reactions", "Create sunlight"], 2, "Enzymes are biological catalysts."),
    ("Where does photosynthesis occur in plants?", ["Mitochondria", "Chloroplasts", "Ribosomes", "Nucleus"], 1, "Chloroplasts are the main sites of photosynthesis in plants."),
    ("Which gas is released during photosynthesis?", ["Oxygen", "Nitrogen", "Helium", "Methane"], 0, "Photosynthesis releases oxygen when water is split."),
    ("Movement from high to low concentration is called:", ["Active transport", "Diffusion", "Translation", "Replication"], 1, "Diffusion moves particles down their concentration gradient."),
    ("What is osmosis?", ["Water movement across a selectively permeable membrane", "DNA production", "Cell division", "Protein synthesis"], 0, "Osmosis is the net movement of water across a selectively permeable membrane."),
    ("Which process can move substances against a concentration gradient?", ["Simple diffusion", "Osmosis", "Active transport", "Passive diffusion"], 2, "Active transport uses energy to move substances against a gradient."),
    ("What is the approximate pH of a neutral solution at room temperature?", ["1", "7", "10", "14"], 1, "A neutral solution has a pH of about 7 at room temperature."),
    ("Which macromolecule is made from amino acids?", ["Protein", "Carbohydrate", "Nucleic acid", "Mineral"], 0, "Amino acids are the building blocks of proteins."),
    ("What is the primary role of DNA?", ["Digest food", "Store hereditary information", "Produce all ATP directly", "Absorb water"], 1, "DNA stores genetic information used by cells."),
    ("What does an ecosystem include?", ["Only animals", "Only plants", "Organisms and their nonliving environment", "Only soil"], 2, "Ecosystems include organisms and their physical environment."),
    ("What is the independent variable in an experiment?", ["The factor deliberately changed", "The result measured", "Every constant", "The conclusion"], 0, "The independent variable is the factor the investigator changes.")
]

FLASHCARDS = [
    ("Cell", "The basic structural and functional unit of life."),
    ("Nucleus", "Stores most of a eukaryotic cell's DNA."),
    ("Mitochondrion", "An organelle where major stages of aerobic respiration occur."),
    ("Ribosome", "A cellular structure that builds proteins."),
    ("DNA", "The molecule that stores hereditary information."),
    ("Gene", "A DNA sequence containing functional information."),
    ("Enzyme", "A biological catalyst that speeds up a reaction."),
    ("Photosynthesis", "Using light energy to make sugars from carbon dioxide and water."),
    ("Osmosis", "Net movement of water across a selectively permeable membrane."),
    ("Diffusion", "Net movement of particles down their concentration gradient."),
    ("Homeostasis", "Regulation of internal conditions within suitable ranges."),
    ("Ecosystem", "Organisms interacting with each other and their environment.")
]

# Keep progress while this browser session is active.
if "explored" not in st.session_state:
    st.session_state.explored = set()
if "points" not in st.session_state:
    st.session_state.points = 0
if "best_score" not in st.session_state:
    st.session_state.best_score = 0
if "card_index" not in st.session_state:
    st.session_state.card_index = 0
if "card_flipped" not in st.session_state:
    st.session_state.card_flipped = False
if "cards_reviewed" not in st.session_state:
    st.session_state.cards_reviewed = 0
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = False
if "quiz_feedback" not in st.session_state:
    st.session_state.quiz_feedback = ""
if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

st.title("🧬 BioBloom Biology Lab")
st.caption("SCIENCE EDITION • Discover life. Understand science. Grow your knowledge.")

dashboard, lessons_tab, quiz_tab, cards_tab, toolkit = st.tabs([
    "🏠 Dashboard", "🔬 Lessons", "🎯 Knowledge Test",
    "🧠 Flashcards", "⚗️ Science Toolkit"
])

with dashboard:
    st.markdown("""
    <div class="lab-card">
    <h2>Life is incredible. Let's understand it.</h2>
    <p>Explore cells, decode DNA, discover energy in living things,
    and test your scientific knowledge.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Lessons explored", len(st.session_state.explored))
    c2.metric("Lab points", st.session_state.points)
    c3.metric("Best quiz score", f"{st.session_state.best_score}%")
    c4.metric("Cards reviewed", st.session_state.cards_reviewed)

    progress = len(st.session_state.explored) / len(LESSONS)
    st.write("**Your learning progress**")
    st.progress(progress)
    st.caption(f"{round(progress * 100)}% of available lessons explored.")

    st.subheader("Your science universe")
    for title, icon in [
        ("Cells and Organelles", "🔬"),
        ("DNA and Genetics", "🧬"),
        ("Energy in Living Things", "🌿"),
        ("Chemistry of Life", "⚛️"),
        ("Cell Transport", "💧"),
        ("Ecology and Ecosystems", "🌎")
    ]:
        st.write(f"{icon} **{title}**")

with lessons_tab:
    st.header("Biology Lessons")
    st.write("Choose a topic and explore the key concepts.")

    topic = st.selectbox("Select a lesson", list(LESSONS.keys()))

    if topic not in st.session_state.explored:
        st.session_state.explored.add(topic)
        st.session_state.points += 10

    st.subheader(topic)
    for item in LESSONS[topic]:
        st.markdown(f"- {item}")

    st.info("Study tip: explain each concept in your own words to check your understanding.")

with quiz_tab:
    st.header("20-Question Biology Challenge")
    st.write("Choose an answer, submit it, and read the explanation.")

    if not st.session_state.quiz_finished:
        i = st.session_state.quiz_index
        q, options, correct, explanation = QUESTIONS[i]

        st.progress(i / len(QUESTIONS))
        st.caption(f"Question {i + 1} of {len(QUESTIONS)}")
        st.subheader(q)

        answer = st.radio(
            "Choose one answer:",
            options,
            index=None,
            key=f"answer_{i}",
            disabled=st.session_state.quiz_answered
        )

        if not st.session_state.quiz_answered:
            if st.button("Check answer", key=f"check_{i}"):
                if answer is None:
                    st.warning("Please choose an answer first.")
                else:
                    chosen = options.index(answer)
                    if chosen == correct:
                        st.session_state.quiz_score += 1
                        st.session_state.points += 5
                        st.session_state.quiz_feedback = "✅ Correct! " + explanation
                    else:
                        st.session_state.quiz_feedback = (
                            f"Not quite. The correct answer is **{options[correct]}**. "
                            + explanation
                        )
                    st.session_state.quiz_answered = True
                    st.rerun()
        else:
            st.markdown(st.session_state.quiz_feedback)
            st.write(f"Score: {st.session_state.quiz_score}")

            if st.button(
                "See results" if i == len(QUESTIONS) - 1 else "Next question →",
                key=f"next_{i}"
            ):
                if i == len(QUESTIONS) - 1:
                    st.session_state.quiz_finished = True
                    percentage = round(
                        st.session_state.quiz_score / len(QUESTIONS) * 100
                    )
                    st.session_state.best_score = max(
                        st.session_state.best_score, percentage
                    )
                    st.session_state.points += 10
                else:
                    st.session_state.quiz_index += 1
                st.session_state.quiz_answered = False
                st.session_state.quiz_feedback = ""
                st.rerun()
    else:
        percentage = round(
            st.session_state.quiz_score / len(QUESTIONS) * 100
        )
        st.success("Challenge complete!")
        st.metric("Your score", f"{percentage}%")
        st.write(f"You answered {st.session_state.quiz_score} out of 20 correctly.")

        if percentage >= 80:
            st.write("🌟 Excellent work, scientist!")
        elif percentage >= 60:
            st.write("👏 Good effort. Review the topics you missed.")
        else:
            st.write("📚 Keep learning and try again after reviewing your lessons.")

        if st.button("Retake the test"):
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_answered = False
            st.session_state.quiz_feedback = ""
            st.session_state.quiz_finished = False
            st.rerun()

with cards_tab:
    st.header("Biology Flashcards")
    st.write("Think of the answer, then reveal the card.")

    idx = st.session_state.card_index
    term, definition = FLASHCARDS[idx]

    st.progress((idx + 1) / len(FLASHCARDS))
    st.caption(f"Card {idx + 1} of {len(FLASHCARDS)}")

    st.markdown(
        f"<div class='lab-card'><h2>{term}</h2></div>",
        unsafe_allow_html=True
    )

    if st.session_state.card_flipped:
        st.info(definition)
    else:
        st.caption("Answer hidden. Try to remember it first.")

    if st.button("Reveal answer" if not st.session_state.card_flipped else "Hide answer"):
        if not st.session_state.card_flipped:
            st.session_state.cards_reviewed += 1
        st.session_state.card_flipped = not st.session_state.card_flipped
        st.rerun()

    left, right = st.columns(2)
    with left:
        if st.button("← Previous card"):
            st.session_state.card_index = (idx - 1) % len(FLASHCARDS)
            st.session_state.card_flipped = False
            st.rerun()
    with right:
        if st.button("Next card →"):
            st.session_state.card_index = (idx + 1) % len(FLASHCARDS)
            st.session_state.card_flipped = False
            st.rerun()

with toolkit:
    st.header("Science Toolkit")

    st.subheader("🧪 pH Scale")
    ph = st.slider("Choose a pH value", 0.0, 14.0, 7.0, 0.5)
    if ph < 7:
        st.info(f"pH {ph}: Acidic")
    elif ph > 7:
        st.info(f"pH {ph}: Basic (alkaline)")
    else:
        st.success("pH 7: Neutral")

    st.divider()
    st.subheader("🔬 Microscope Guide")
    st.write("Total magnification = eyepiece magnification × objective magnification.")
    st.write("Example: 10× eyepiece × 40× objective = **400×** total magnification.")

    st.divider()
    st.subheader("⚗️ Scientific Method")
    st.markdown("""
    1. Ask a question.
    2. Research the topic.
    3. Form a hypothesis.
    4. Test it fairly.
    5. Analyze the results.
    6. Draw a conclusion.
    """)

    st.divider()
    st.subheader("📝 Your Study Notes")
    note_title = st.text_input("Topic title")
    note_text = st.text_area("Write your notes here")

    if st.button("Prepare notes for saving"):
        if note_title.strip() and note_text.strip():
            st.download_button(
                "Download notes as a text file",
                data=f"{note_title}\n\n{note_text}",
                file_name="biobloom_notes.txt",
                mime="text/plain"
            )
        else:
            st.warning("Enter a title and some notes first.")

st.divider()
st.caption("BioBloom Biology Lab • Learn something amazing every day 🧬")
