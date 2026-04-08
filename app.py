import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# UI Rendering methods
def render_footer():
    st.markdown("""
    <style>
    .footer {
        margin-top: 3rem;
        padding: 1.2rem 1rem;
        text-align: center;
        font-size: 0.85rem;
        color: #94A3B8;
        border-top: 1px solid #1E293B;
    }

    .footer strong {
        color: #E5E7EB;
    }

    .footer .brand {
        color: #60A5FA;
        font-weight: 600;
    }

    .footer a {
        color: #60A5FA;
        text-decoration: none;
        margin: 0 6px;
    }

    .footer a:hover {
        text-decoration: underline;
    }
    </style>

    <div class="footer">
    <div>PerformX Tracker</div>
    <div>
        Developed by 
        <a href="https://dataanddiscodreamsstudio.com" target="_blank" class="brand">
            Data & Disco Dreams Studio
        </a>
        <a>|<a> 
        Developer 
        <a href="https://www.linkedin.com/in/vivek-singh-858941201" target="_blank" class="brand">
            Vivek Singh
        </a>
    </div>
    <div style="margin-top:6px;">
        Built with ❤️ using Streamlit · Performance Analytics Framework
    </div>
    <div style="margin-top:6px;">
        © 2026 All rights reserved
    </div>
    """, unsafe_allow_html=True)

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="PerformX Tracker - Universal Performance Tracker",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Global */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main {background-color: #F8FAFC !important;}
    .block-container { padding: 2rem 2.5rem 2rem 2.5rem; max-width: 1400px; }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1F3864 0%, #2E5FA3 100%);
    }
    [data-testid="stSidebar"] * { color: white !important; }
    [data-testid="stSidebar"] .stRadio label { 
        color: white !important; 
        font-size: 0.9rem;
    }
    [data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.2); }

    /* Page title */
    .page-title {
        font-size: 1.9rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.2rem;
    }
    .page-subtitle {
        font-size: 0.95rem;
        color: white;
        margin-bottom: 1.8rem;
    }

    /* Section headers */
    .section-header {
        background: linear-gradient(90deg, #1F3864, #2E5FA3);
        color: white;
        padding: 0.75rem 1.2rem;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
        letter-spacing: 0.3px;
    }
    .section-header-orange {
        background: linear-gradient(90deg, #1F3864, #2E5FA3);
        color: white;
        padding: 0.75rem 1.2rem;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
    }
    .section-header-green {
        background: linear-gradient(90deg, #1F3864, #2E5FA3);
        color: white;
        padding: 0.75rem 1.2rem;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
    }
    .section-header-grey {
        background: linear-gradient(90deg, #1F3864, #2E5FA3);
        color: white;
        padding: 0.75rem 1.2rem;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
    }

    /* Cards */
    .metric-card {
        color: black;
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    .category-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #2E5FA3;
        border-radius: 10px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 1px 4px rgba(0,0,0,0.07);
    }
    .prompt-card {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #BD4D00;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
    }
    .summary-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }

    /* Score badges */
    .score-5 { background:#D1FAE5; color:#065F46; padding:3px 10px; border-radius:20px; font-weight:600; font-size:0.85rem; }
    .score-4 { background:#DBEAFE; color:#1E40AF; padding:3px 10px; border-radius:20px; font-weight:600; font-size:0.85rem; }
    .score-3 { background:#FEF9C3; color:#854D0E; padding:3px 10px; border-radius:20px; font-weight:600; font-size:0.85rem; }
    .score-2 { background:#FFEDD5; color:#9A3412; padding:3px 10px; border-radius:20px; font-weight:600; font-size:0.85rem; }
    .score-1 { background:#FEE2E2; color:#991B1B; padding:3px 10px; border-radius:20px; font-weight:600; font-size:0.85rem; }

    /* Risk badges */
    .risk-high   { background:#FEE2E2; color:#991B1B; padding:2px 9px; border-radius:20px; font-size:0.78rem; font-weight:600; }
    .risk-medium { background:#FFEDD5; color:#9A3412; padding:2px 9px; border-radius:20px; font-size:0.78rem; font-weight:600; }
    .risk-low    { background:#D1FAE5; color:#065F46; padding:2px 9px; border-radius:20px; font-size:0.78rem; font-weight:600; }

    /* Type badges */
    .type-q    { background:#D9EAD3; color:#274E13; padding:2px 9px; border-radius:20px; font-size:0.78rem; font-weight:600; }
    .type-qual { background:#FCE4D6; color:#7F2704; padding:2px 9px; border-radius:20px; font-size:0.78rem; font-weight:600; }
    .type-mix  { background:#FFF2CC; color:#7D6608; padding:2px 9px; border-radius:20px; font-size:0.78rem; font-weight:600; }

    /* Info box */
    .info-box {
        background: #EFF6FF;
        border: 1px solid #BFDBFE;
        border-radius: 8px;
        padding: 0.9rem 1.1rem;
        font-size: 0.88rem;
        color: #1E40AF;
        margin-bottom: 1rem;
    }
    .warning-box {
        background: #FFFBEB;
        border: 1px solid #FDE68A;
        border-radius: 8px;
        padding: 0.9rem 1.1rem;
        font-size: 0.88rem;
        color: #92400E;
        margin-bottom: 1rem;
    }

    /* Divider */
    .soft-divider { border: none; border-top: 1px solid #E2E8F0; margin: 1.2rem 0; }

    /* Overview stat boxes */
    .stat-box {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 1.1rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .stat-number { font-size: 2rem; font-weight: 700; color: #1F3864; }
    .stat-label  { font-size: 0.8rem; color: #64748B; margin-top: 0.2rem; }

    /* Sticker label */
    .field-label { font-size:0.82rem; font-weight:600; color: #60A5FA; margin-bottom:0.2rem; }
    .field-hint  { font-size:0.76rem; color:#9CA3AF; font-style:italic; }

    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* header {visibility: hidden;} */

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 6px; }
    .stTabs [data-baseweb="tab"] {
        background: #F1F5F9;
        border-radius: 8px 8px 0 0;
        padding: 0.5rem 1.2rem;
        font-weight: 500;
        font-size: 0.88rem;
        color: #475569;
    }
    .stTabs [aria-selected="true"] {
        background: #1F3864 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# DATA — All phases reflected
# ══════════════════════════════════════════════════════════════════════════════

CATEGORIES = {
    "Execution & Delivery": {
        "definition": "Consistently completes assigned work, milestones, or projects on time with clear prioritization and follow-through.",
        "why_matters": "Reliable delivery ensures commitments are met and builds operational predictability.",
        "classification": "Quantitative-leaning Hybrid",
        "bias_risk": "Medium",
        "bias_note": "Normalize complexity weighting; avoid equating high-visibility with high-impact delivery.",
        "metrics": [
            {
                "name": "On-time Delivery Rate",
                "description": "Measures consistency in meeting deadlines",
                "logic": "% of tasks/milestones completed on or before deadline",
                "type": "Quantitative",
                "source": "Task tracker / project logs",
                "tradeoff": "Focus on delivery timelines may encourage speed over quality."
            },
            {
                "name": "Commitment Reliability",
                "description": "Assesses whether commitments are followed through",
                "logic": "Manager or self review of follow-through across review period",
                "type": "Qualitative",
                "source": "Self-reflection / manager review",
                "tradeoff": "May rely heavily on manager perception."
            }
        ],
        "prompts": [
            ("What obstacles impacted your ability to deliver this quarter, and how did you address them?",
             "Decision-making under constraint and self-awareness in execution gaps."),
            ("Describe a project or task where you had to reprioritize mid-way through. What drove the change and what was the outcome?",
             "Adaptability and structured re-planning under shifting priorities."),
            ("Where did your delivery fall short of the original plan, and what would you do differently?",
             "Honest gap reflection and forward-looking corrective thinking."),
        ]
    },
    "Quality & Attention to Detail": {
        "definition": "Produces work that is accurate, well-reviewed, and meets defined standards with minimal rework required.",
        "why_matters": "High-quality outputs reduce risk and improve decision reliability.",
        "classification": "Quantitative",
        "bias_risk": "Medium",
        "bias_note": "Anchor quality to documented standards and reviewer-independent criteria; use rubrics.",
        "metrics": [
            {
                "name": "Error Rate",
                "description": "Tracks frequency of errors or rework needed",
                "logic": "# of revisions or corrections per deliverable",
                "type": "Quantitative",
                "source": "QA reviews / version history",
                "tradeoff": "Quality assessment may rely partly on subjective feedback."
            },
            {
                "name": "Work Quality Assessment",
                "description": "Evaluates perceived thoroughness and accuracy",
                "logic": "Periodic qualitative review against quality standards",
                "type": "Qualitative",
                "source": "Peer or manager feedback",
                "tradeoff": "Highly role-dependent; harder to standardize across functions."
            }
        ],
        "prompts": [
            ("Describe a piece of work from this quarter you are most proud of. What specifically made it high quality?",
             "Quality standards applied, not just effort invested."),
            ("Where did feedback prompt you to revise or improve your work? What changed?",
             "Receptivity to feedback and ownership of output improvement."),
            ("What standards or benchmarks did you use to evaluate the quality of your outputs this quarter?",
             "Deliberate quality criteria and self-review discipline."),
        ]
    },
    "Communication & Stakeholder Alignment": {
        "definition": "Shares clear updates and aligns expectations with stakeholders proactively.",
        "why_matters": "Clear communication prevents misalignment and delays.",
        "classification": "Qualitative-leaning Hybrid",
        "bias_risk": "High",
        "bias_note": "Evaluate impact of communication (action taken, decisions made) not style or volume.",
        "metrics": [
            {
                "name": "Update Consistency",
                "description": "Measures regularity of status updates",
                "logic": "# of proactive updates per cycle",
                "type": "Quantitative",
                "source": "Communication logs / meeting notes",
                "tradeoff": "Communication effectiveness can be influenced by personality and visibility."
            },
            {
                "name": "Clarity of Communication",
                "description": "Assesses how clearly information is conveyed",
                "logic": "Stakeholder rating or feedback on clarity",
                "type": "Qualitative",
                "source": "Stakeholder surveys / feedback",
                "tradeoff": "Employees in collaborative roles may have more opportunity to demonstrate this."
            }
        ],
        "prompts": [
            ("Describe a time this quarter where you had to translate complex information for a non-technical audience. What approach did you take?",
             "Audience awareness and clarity in communication under complexity."),
            ("How did you ensure your key updates or recommendations were acted upon — not just received?",
             "Driving action through communication, not just delivering information."),
            ("Where did a miscommunication or unclear message create friction, and how did you course-correct?",
             "Accountability for communication missteps and recovery."),
        ]
    },
    "Ownership & Initiative": {
        "definition": "Takes responsibility and proactively moves work forward without being prompted.",
        "why_matters": "Ownership accelerates progress and reduces coordination gaps.",
        "classification": "Qualitative-leaning Hybrid",
        "bias_risk": "High",
        "bias_note": "Document initiative in writing quarterly. Reward prevention alongside resolution.",
        "metrics": [
            {
                "name": "Proactive Issue Identification",
                "description": "Tracks how often risks or improvements are surfaced",
                "logic": "Count of risks/improvements raised proactively",
                "type": "Quantitative",
                "source": "Retrospectives / meeting notes",
                "tradeoff": "Ownership behaviors can be difficult to quantify; may rely on manager perception."
            },
            {
                "name": "Accountability Behavior",
                "description": "Evaluates responsibility for outcomes",
                "logic": "Manager review of ownership behaviors",
                "type": "Qualitative",
                "source": "Manager feedback / 1:1 notes",
                "tradeoff": "Employees in structured roles may have fewer opportunities to demonstrate initiative."
            }
        ],
        "prompts": [
            ("What decisions or actions you took this quarter had the most measurable impact, and why?",
             "Connecting individual actions to tangible outcomes."),
            ("Describe a problem you identified and resolved before it was escalated or assigned to you.",
             "Proactive problem ownership beyond assigned scope."),
            ("What new approach, process, or idea did you introduce this quarter, and how did it move the work forward?",
             "Innovation and independent judgment in improving how work is done."),
        ]
    },
    "Problem Solving & Judgment": {
        "definition": "Analyzes problems and proposes practical, well-reasoned solutions under uncertainty.",
        "why_matters": "Strong judgment improves outcomes and reduces downstream risk.",
        "classification": "Hybrid",
        "bias_risk": "Medium",
        "bias_note": "Contributions may not always be visible to managers; document decisions with outcomes.",
        "metrics": [
            {
                "name": "Solution Effectiveness",
                "description": "Measures whether proposed solutions resolve issues",
                "logic": "% of solutions implemented successfully",
                "type": "Quantitative",
                "source": "Project outcomes / post-mortems",
                "tradeoff": "Problem-solving contributions may not always be visible to managers."
            },
            {
                "name": "Decision Quality",
                "description": "Assesses soundness of decisions under uncertainty",
                "logic": "Review of decisions vs outcomes",
                "type": "Mixed",
                "source": "Review of decisions vs outcomes",
                "tradeoff": "Complex problems may span multiple quarters, making single-period evaluation imperfect."
            }
        ],
        "prompts": [
            ("Describe a decision you made this quarter under uncertainty. How did you approach it and what was the outcome?",
             "Structured reasoning and decision quality under ambiguity."),
            ("Where did an initial solution not work as expected, and how did you adapt?",
             "Resilience in problem-solving and learning from failed approaches."),
            ("What information or perspective changed how you approached a problem this quarter?",
             "Openness to new data and willingness to revise judgment."),
        ]
    },
    "Learning & Adaptability": {
        "definition": "Applies feedback, acquires new skills, and adapts to change across the review period.",
        "why_matters": "Continuous learning supports long-term effectiveness and career growth.",
        "classification": "Qualitative",
        "bias_risk": "Low–Medium",
        "bias_note": "Ensure equitable access to learning resources; do not penalize for gaps in formal training access.",
        "metrics": [
            {
                "name": "Skill Development Progress",
                "description": "Tracks progress in acquiring new skills",
                "logic": "# of new tools/skills learned or applied",
                "type": "Quantitative",
                "source": "Learning logs / manager observation",
                "tradeoff": "Learning activities do not always translate immediately into measurable outcomes."
            },
            {
                "name": "Adaptability Feedback",
                "description": "Assesses response to change or feedback",
                "logic": "Manager/peer rating on adaptability",
                "type": "Qualitative",
                "source": "Feedback sessions / peer input",
                "tradeoff": "This category may rely on qualitative inputs rather than direct performance metrics."
            }
        ],
        "prompts": [
            ("What skill or capability did you actively develop this quarter, and how did you apply it to your work?",
             "Applied learning — behavior change, not just development activity."),
            ("Describe a mistake or failure from this quarter and what you learned from it.",
             "Learning agility and honest reflection on setbacks."),
            ("How did feedback from this period influence how you approach your work going forward?",
             "Feedback integration translated into visible behavioral shift."),
        ]
    },
    "Collaboration & Influence": {
        "definition": "Works effectively with others toward shared outcomes and contributes to team success.",
        "why_matters": "Effective collaboration improves execution speed and team cohesion.",
        "classification": "Qualitative",
        "bias_risk": "High",
        "bias_note": "Require documented collaboration outcomes, not frequency. Include async formats.",
        "metrics": [
            {
                "name": "Collaboration Effectiveness",
                "description": "Measures teamwork and contribution",
                "logic": "Peer feedback score or survey",
                "type": "Mixed",
                "source": "Peer review / team feedback",
                "tradeoff": "May unintentionally favor employees in roles with higher interaction levels."
            },
            {
                "name": "Knowledge Sharing",
                "description": "Tracks contribution to team learning",
                "logic": "# of knowledge shares or documentation contributions",
                "type": "Quantitative",
                "source": "Docs / sessions / Slack threads",
                "tradeoff": "Influence is difficult to measure objectively; may depend on peer/manager perception."
            }
        ],
        "prompts": [
            ("Describe one instance this quarter where cross-functional alignment changed the outcome of your work.",
             "Collaboration with measurable impact — not just participation."),
            ("How did you handle a situation where stakeholder expectations and team capacity were misaligned?",
             "Conflict navigation and realistic expectation management."),
            ("What relationships or partnerships did you invest in this quarter that were not required but added value?",
             "Proactive relationship building beyond minimum role requirements."),
        ]
    },
}

SCORE_LABELS = {
    1: "Needs Improvement",
    2: "Developing",
    3: "Meets Expectations",
    4: "Strong",
    5: "Exceptional"
}

SCORE_COLORS = {
    1: "#EF4444", 2: "#F97316", 3: "#EAB308", 4: "#3B82F6", 5: "#22C55E"
}

QUARTERS = ["Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025",
            "Q1 2026", "Q2 2026", "Q3 2026", "Q4 2026"]

# ══════════════════════════════════════════════════════════════════════════════
# SESSION STATE INIT
# ══════════════════════════════════════════════════════════════════════════════
def init_state():
    if "employee_info" not in st.session_state:
        st.session_state.employee_info = {
            "name": "", "role": "", "department": "",
            "manager": "", "quarter": "Q1 2025", "date": str(datetime.today().date())
        }
    if "metric_scores" not in st.session_state:
        st.session_state.metric_scores = {}
    if "metric_targets" not in st.session_state:
        st.session_state.metric_targets = {}
    if "metric_actuals" not in st.session_state:
        st.session_state.metric_actuals = {}
    if "metric_evidence" not in st.session_state:
        st.session_state.metric_evidence = {}
    if "qual_responses" not in st.session_state:
        st.session_state.qual_responses = {}
    if "manager_notes" not in st.session_state:
        st.session_state.manager_notes = {}
    if "active_page" not in st.session_state:
        st.session_state.active_page = "Overview & Summary"

init_state()

# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def get_category_score(cat_name):
    cat_data = CATEGORIES[cat_name]
    scores = []
    for m in cat_data["metrics"]:
        key = f"{cat_name}__{m['name']}"
        s = st.session_state.metric_scores.get(key, 0)
        if s > 0:
            scores.append(s)
    return round(sum(scores) / len(scores), 1) if scores else None

def get_completion_pct():
    total = sum(len(c["metrics"]) for c in CATEGORIES.values())
    filled = sum(1 for v in st.session_state.metric_scores.values() if v > 0)
    return int((filled / total) * 100) if total > 0 else 0

def score_badge(score):
    if not score:
        return "<span style='color:#94A3B8;font-size:0.85rem;'>Not scored</span>"
    cls = f"score-{int(score)}" if score == int(score) else "score-3"
    label = SCORE_LABELS.get(int(round(score)), "")
    return f"<span class='{cls}'>{score} — {label}</span>"

def risk_badge(risk):
    r = risk.lower()
    if "high" in r:
        return f"<span class='risk-high'>⚠ High Risk</span>"
    elif "medium" in r:
        return f"<span class='risk-medium'>◆ Medium Risk</span>"
    else:
        return f"<span class='risk-low'>✓ Low Risk</span>"

def type_badge(t):
    if t == "Quantitative":
        return "<span class='type-q'>Quantitative</span>"
    elif t == "Qualitative":
        return "<span class='type-qual'>Qualitative</span>"
    else:
        return "<span class='type-mix'>Mixed</span>"

# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""<div style='font-size:1.8rem;font-weight:700;color:#F9FAFB;'>PerformX</div>""", unsafe_allow_html=True)
    st.markdown("<small style='opacity:0.65;color:#CBD5E1;'>Universal Performance Tracker</small>", unsafe_allow_html=True)

    st.markdown("""
    <div style='margin-bottom:0.2rem;'>

    <div style='margin-top:0.2rem;font-size:0.88rem;color:#CBD5E1;line-height:1.4;'>
    An implementation of a universal performance framework that combines quantitative metrics and qualitative insights across 7 core categories. 
    Designed for real-world usability, it enables consistent tracking, structured evaluation, and meaningful performance discussions.
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""<div style='font-size:1.1rem;font-weight:700;color:#F9FAFB;'>Navigations</div>""", unsafe_allow_html=True)
    st.markdown("""<div style='margin-top:0.2rem;font-size:0.88rem;color:#CBD5E1;line-height:1.5;'></div>""", unsafe_allow_html=True)
    pages = [
        "🏠  Overview & Summary",
        "👤  Employee Setup",
        "📋  Category Input",
        "💬  Qualitative Reflection",
        "📖  Usage Instructions",
    ]
    page_labels = [p.split("  ")[1] for p in pages]
    page_map = dict(zip(page_labels, pages))

    selected_raw = st.radio("Navigate", pages, label_visibility="collapsed")
    selected_page = selected_raw.split("  ")[1]

    st.markdown("---")
    # Employee quick info
    emp = st.session_state.employee_info
    if emp["name"]:
        st.markdown(f"<div style='font-size:0.9rem;font-weight:600;color:#F9FAFB;'>{emp['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<small style='color:#CBD5E1;'>{emp['role']}</small>", unsafe_allow_html=True)
        st.markdown(f"<small style='color:#94A3B8;'>📅 {emp['quarter']}</small>", unsafe_allow_html=True)
    else:
        st.markdown("""<div style='background:rgba(96,165,250,0.12);border:1px solid rgba(96,165,250,0.3);border-radius:6px;padding:0.6rem 0.8rem;font-size:0.82rem;color:#93C5FD;'>
        👆 Start here: <strong style='color:#BFDBFE;'>Employee Setup</strong>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    # Progress
    pct = get_completion_pct()
    st.markdown(f"<div style='font-size:0.8rem;color:#94A3B8;margin-bottom:0.3rem;'>Review Progress</div>", unsafe_allow_html=True)
    st.progress(pct / 100)
    st.markdown(f"<small style='color:#94A3B8;'>{pct}% of metrics scored</small>", unsafe_allow_html=True)

    st.markdown("---")
    # Score guide — compact
    st.markdown("<div style='font-size:0.78rem;color:#94A3B8;margin-bottom:0.4rem;'>SCORING GUIDE</div>", unsafe_allow_html=True)
    for score, label in SCORE_LABELS.items():
        color = SCORE_COLORS[score]
        st.markdown(f"<div style='font-size:0.78rem;margin-bottom:1px;'><span style='color:{color};font-weight:700;'>{score}</span> <span style='color:#94A3B8;'>— {label}</span></div>",
                    unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: OVERVIEW & SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
if selected_page == "Overview & Summary":
    st.markdown('<div class="page-title">📈 Overview & Summary</div>', unsafe_allow_html=True)
    emp = st.session_state.employee_info
    quarter_label = emp.get("quarter", "—")
    name_label = emp.get("name", "—") if emp.get("name") else "Not set"
    st.markdown(f'<div class="page-subtitle">Performance review dashboard for <strong>{name_label}</strong> · {quarter_label}</div>', unsafe_allow_html=True)
    

    # ── Top stat row ──────────────────────────────────────────────────────────
    scores_available = [get_category_score(c) for c in CATEGORIES if get_category_score(c)]
    overall_avg = round(sum(scores_available) / len(scores_available), 2) if scores_available else None
    cats_scored = len(scores_available)
    pct = get_completion_pct()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""<div class='stat-box'>
            <div class='stat-number'>{overall_avg if overall_avg else '—'}</div>
            <div class='stat-label'>Overall Score (/ 5)</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class='stat-box'>
            <div class='stat-number'>{cats_scored}</div>
            <div class='stat-label'>Categories Scored</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class='stat-box'>
            <div class='stat-number'>{pct}%</div>
            <div class='stat-label'>Tracker Completion</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        st.markdown(f"""<div class='stat-box'>
            <div class='stat-number'>{len(CATEGORIES)}</div>
            <div class='stat-label'>Total Categories</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Quick Insight Strip — strongest, focus, completion ───────────────────
    if cats_scored >= 2:
        sorted_all = sorted(
            [(c, get_category_score(c)) for c in CATEGORIES if get_category_score(c)],
            key=lambda x: x[1], reverse=True
        )
        top_cat, top_score = sorted_all[0]
        low_cat, low_score = sorted_all[-1]
        focus_score_color = SCORE_COLORS.get(int(round(low_score)), "#94A3B8")
        st.markdown(f"""
        <div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-bottom:1.4rem;'>
            <div style='background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:1rem 1.2rem;'>
                <div style='font-size:0.7rem;font-weight:700;color:#16A34A;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:5px;'>💪 Strongest Area</div>
                <div style='font-size:0.97rem;font-weight:700;color:#14532D;line-height:1.3;'>{top_cat}</div>
                <div style='font-size:0.82rem;color:#22C55E;font-weight:600;margin-top:4px;'>Score: {top_score} / 5</div>
            </div>
            <div style='background:#FFF7ED;border:1px solid #FED7AA;border-radius:10px;padding:1rem 1.2rem;'>
                <div style='font-size:0.7rem;font-weight:700;color:#EA580C;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:5px;'>🎯 Suggested Focus</div>
                <div style='font-size:0.97rem;font-weight:700;color:#7C2D12;line-height:1.3;'>{low_cat}</div>
                <div style='font-size:0.82rem;color:{focus_score_color};font-weight:600;margin-top:4px;'>Score: {low_score} / 5</div>
            </div>
            <div style='background:#EFF6FF;border:1px solid #BFDBFE;border-radius:10px;padding:1rem 1.2rem;'>
                <div style='font-size:0.7rem;font-weight:700;color:#2563EB;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:5px;'>📋 Review Progress</div>
                <div style='font-size:0.97rem;font-weight:700;color:#1E3A8A;'>{cats_scored} of {len(CATEGORIES)} scored</div>
                <div style='font-size:0.82rem;color:#3B82F6;font-weight:600;margin-top:4px;'>{pct}% metrics complete</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Category score table ──────────────────────────────────────────────────
    st.markdown('<div class="section-header">📊 Category Score Summary</div>', unsafe_allow_html=True)

    if cats_scored == 0:
        st.markdown('<div class="info-box">ℹ️ No scores entered yet. Complete <strong>Category Input</strong> to see your summary here.</div>',
                    unsafe_allow_html=True)
    else:
        col_left, col_right = st.columns([1.1, 1])
        with col_left:
            for cat_name, cat_data in CATEGORIES.items():
                score = get_category_score(cat_name)
                bar_val = score / 5 if score else 0
                bar_color = SCORE_COLORS.get(int(round(score)), "#94A3B8") if score else "#E2E8F0"
                label = SCORE_LABELS.get(int(round(score)), "") if score else "Not scored"
                score_disp = f"{score}" if score else "—"

                st.markdown(f"""
                <div style='margin-bottom:0.7rem;'>
                  <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:0.25rem;'>
                    <span style='font-size:0.88rem;font-weight:500;color:#E2E8F0;'>{cat_name}</span>
                    <span style='font-size:0.88rem;font-weight:700;color:{bar_color};'>{score_disp} <span style='font-weight:400;color:#94A3B8;font-size:0.8rem;'>— {label}</span>
                  </div>
                  <div style='background:#F1F5F9;border-radius:99px;height:8px;'>
                    <div style='background:{bar_color};width:{bar_val*100:.0f}%;height:8px;border-radius:99px;transition:width 0.3s;'></div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

        with col_right:
            if cats_scored >= 2:
                cat_names = [c for c in CATEGORIES if get_category_score(c)]
                cat_scores = [get_category_score(c) for c in cat_names]
                short_names = [c.split(" & ")[0] if " & " in c else c for c in cat_names]

                fig = go.Figure(go.Scatterpolar(
                    r=cat_scores + [cat_scores[0]],
                    theta=short_names + [short_names[0]],
                    fill='toself',
                    fillcolor='rgba(46,95,163,0.15)',
                    line=dict(color='#2E5FA3', width=2),
                    marker=dict(size=7, color='#1F3864')
                ))
                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[0, 5],
                            tickfont=dict(size=9, color="#CBD5E1"),
                            gridcolor="#334155"
                        ),
                        angularaxis=dict(tickfont=dict(size=10, color="#E2E8F0"))
                    ),
                    showlegend=False,
                    margin=dict(l=40, r=40, t=30, b=30),
                    height=310,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
                st.plotly_chart(fig, use_container_width=True)

    # ── Strengths & Watch Areas ───────────────────────────────────────────────
    if cats_scored >= 2:
        st.markdown('<div class="section-header">🔍 Strengths & Areas to Watch</div>', unsafe_allow_html=True)
        col_s, col_w = st.columns(2)
        sorted_cats = sorted(
            [(c, get_category_score(c)) for c in CATEGORIES if get_category_score(c)],
            key=lambda x: x[1], reverse=True
        )
        with col_s:
            st.markdown("**Top Performing Areas**")
            for cat, score in sorted_cats[:3]:
                st.markdown(f"""<div style='display:flex;align-items:center;gap:0.6rem;margin-bottom:0.5rem;'>
                    <span style='font-size:1.1rem;'>✅</span>
                    <span style='font-size:0.88rem;color:#E2E8F0;'>{cat}</span>
                    <span style='margin-left:auto;'>{score_badge(score)}</span>
                </div>""", unsafe_allow_html=True)
        with col_w:
            st.markdown("**Areas Needing Attention**")
            for cat, score in sorted_cats[-3:]:
                if score and score < 4:
                    st.markdown(f"""<div style='display:flex;align-items:center;gap:0.6rem;margin-bottom:0.5rem;'>
                        <span style='font-size:1.1rem;'>⚠️</span>
                        <span style='font-size:0.88rem;color:#E2E8F0;'>{cat}</span>
                        <span style='margin-left:auto;'>{score_badge(score)}</span>
                    </div>""", unsafe_allow_html=True)

    # ── Reflection connection nudge ──────────────────────────────────────────
    if cats_scored > 0:
        qual_done = sum(1 for c in CATEGORIES for i in range(3)
                        if st.session_state.qual_responses.get(f"{c}__p{i}", "").strip())
        qual_total = len(CATEGORIES) * 3
        if qual_done < qual_total:
            st.markdown(f"""
            <div style='background:#FFFBEB;border:1px solid #FDE68A;border-radius:8px;padding:0.8rem 1.1rem;
                        display:flex;align-items:center;gap:0.8rem;margin-bottom:1rem;'>
                <span style='font-size:1.2rem;'>💬</span>
                <div>
                    <span style='font-size:0.88rem;font-weight:600;color:#92400E;'>Add qualitative context to your scores.</span>
                    <span style='font-size:0.85rem;color:#92400E;'> {qual_done}/{qual_total} prompts answered. Go to <strong>Qualitative Reflection</strong> to complete the picture.</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='background:#F0FDF4;border:1px solid #BBF7D0;border-radius:8px;padding:0.8rem 1.1rem;
                        display:flex;align-items:center;gap:0.8rem;margin-bottom:1rem;'>
                <span style='font-size:1.2rem;'>✅</span>
                <span style='font-size:0.88rem;font-weight:600;color:#166534;'>All qualitative reflections complete. The tracker is ready for review.</span>
            </div>
            """, unsafe_allow_html=True)

    # ── Employee info summary ─────────────────────────────────────────────────
    st.markdown('<div class="section-header-grey">👤 Review Details</div>', unsafe_allow_html=True)
    emp = st.session_state.employee_info
    cols = st.columns(3)
    fields = [
        ("Employee", emp.get("name", "—") or "—"),
        ("Role", emp.get("role", "—") or "—"),
        ("Department", emp.get("department", "—") or "—"),
        ("Manager", emp.get("manager", "—") or "—"),
        ("Quarter", emp.get("quarter", "—") or "—"),
        ("Date", emp.get("date", "—") or "—"),
    ]
    for i, (label, val) in enumerate(fields):
        with cols[i % 3]:
            st.markdown(f"<div class='field-label'>{label}</div><div style='font-size:0.95rem;color:white;font-weight:600;'>{val}</div><br>",
                        unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📥 Export Summary</div>', unsafe_allow_html=True)

    # Prepare summary data
    summary_data = []

    for cat_name in CATEGORIES:
        score = get_category_score(cat_name)
        summary_data.append({
            "Category": cat_name,
            "Score": score if score else "Not Scored"
        })

    df_summary = pd.DataFrame(summary_data)

    # Add employee info
    emp = st.session_state.employee_info

    scores_available = [get_category_score(c) for c in CATEGORIES if get_category_score(c)]
    overall_avg = round(sum(scores_available) / len(scores_available), 2) if scores_available else "N/A"

    meta_df = pd.DataFrame([
        {"Category": "Employee", "Score": emp.get("name", "")},
        {"Category": "Role", "Score": emp.get("role", "")},
        {"Category": "Quarter", "Score": emp.get("quarter", "")},
        {"Category": "Overall Score", "Score": overall_avg}
    ])

    final_df = pd.concat([meta_df, df_summary], ignore_index=True)

    # 👇 SHOW TABLE (this was missing)
    table_html = "<table style='width:100%;border-collapse:collapse;background:white;border-radius:10px;'>"

    # Header
    table_html += (
        "<tr style='background:#F1F5F9;color:#1F2937;font-size:0.85rem;'>"
        "<th style='text-align:left;padding:10px;'>Category</th>"
        "<th style='text-align:left;padding:10px;'>Score</th>"
        "</tr>"
    )

    # Rows
    for _, row in final_df.iterrows():
        table_html += (
            "<tr style='border-bottom:1px solid #E2E8F0;font-size:0.85rem;color:#1F2937;'>"
            f"<td style='padding:10px;'>{row['Category']}</td>"
            f"<td style='padding:10px;font-weight:600;color:#1F3864;'>{row['Score']}</td>"
            "</tr>"
        )

    table_html += "</table>"

    st.markdown(table_html, unsafe_allow_html=True)

    # Convert to CSV
    csv = final_df.to_csv(index=False).encode('utf-8')

    st.markdown("<br>", unsafe_allow_html=True)

    st.download_button(
        label="⬇️ Download Performance Summary (CSV)",
        data=csv,
        file_name=f"{emp.get('name','employee')}_performance_summary.csv",
        mime="text/csv",
        use_container_width=True
    )



    render_footer()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: EMPLOYEE SETUP
# ══════════════════════════════════════════════════════════════════════════════
elif selected_page == "Employee Setup":
    st.markdown('<div class="page-title">Employee Setup</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Complete this section before starting your review. This information anchors the tracker to a specific person and review period.</div>',
                unsafe_allow_html=True)

    st.markdown('<div class="section-header">👤 Employee Information</div>', unsafe_allow_html=True)

    with st.form("employee_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Employee Name *",
                                  value=st.session_state.employee_info["name"],
                                  placeholder="e.g. Vivek Singh")
            department = st.text_input("Department / Team",
                                        value=st.session_state.employee_info["department"],
                                        placeholder="e.g. Data & Analytics")
            quarter = st.selectbox("Review Quarter *", QUARTERS,
                                    index=QUARTERS.index(st.session_state.employee_info.get("quarter", "Q1 2025")))
        with col2:
            role = st.text_input("Role / Title *",
                                  value=st.session_state.employee_info["role"],
                                  placeholder="e.g. Business Intelligence Analyst")
            manager = st.text_input("Manager Name",
                                     value=st.session_state.employee_info["manager"],
                                     placeholder="e.g. Jana")
            review_date = st.text_input("Review Date",
                                         value=st.session_state.employee_info["date"],
                                         placeholder="e.g. 2025-03-31")

        submitted = st.form_submit_button("💾  Save Employee Information", use_container_width=True)
        if submitted:
            if not name or not role:
                st.error("Employee Name and Role are required.")
            else:
                # 🔥 Reset all tracker data when new employee is set
                st.session_state.metric_scores = {}
                st.session_state.metric_targets = {}
                st.session_state.metric_actuals = {}
                st.session_state.metric_evidence = {}
                st.session_state.qual_responses = {}
                st.session_state.manager_notes = {}

                # Update employee info
                st.session_state.employee_info.update({
                    "name": name,
                    "role": role,
                    "department": department,
                    "manager": manager,
                    "quarter": quarter,
                    "date": review_date
                })

                st.success("✅ Employee information saved. Tracker reset for new review.")
    # Usage context
    st.markdown('<div class="section-header-grey">ℹ️ How the Tracker Works</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box">This tracker covers 7 performance categories aligned with the Universal Performance Framework (Phase 1). Each category contains 2 metrics (Phase 2) and 3 qualitative prompts (Phase 3). Scores are entered in <strong>Category Input</strong>, qualitative context in <strong>Qualitative Reflection</strong>, and the <strong>Overview</strong> shows your full picture.</div>',
                unsafe_allow_html=True)

    steps = [
        ("1", "Complete Employee Setup", "Fill in your name, role, and review quarter above."),
        ("2", "Score Category Input", "For each of the 7 categories, review the metrics, set targets, enter actuals, and assign a 1–5 score with evidence."),
        ("3", "Complete Qualitative Reflection", "Respond to 3 behavioral prompts per category. Manager adds observations in parallel."),
        ("4", "Review Overview & Summary", "See your scores, radar chart, strengths, and areas to watch — all in one view."),
    ]
    for num, title, detail in steps:
        st.markdown(f"""
        <div class='metric-card' style='display:flex;gap:1rem;align-items:flex-start;padding:1rem 1.2rem;'>
            <div style='background:#1F3864;color:white;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.85rem;flex-shrink:0;'>{num}</div>
            <div>
                <div style='font-weight:600;color:#1F3864;font-size:0.9rem;'>{title}</div>
                <div style='color:#64748B;font-size:0.85rem;margin-top:0.2rem;'>{detail}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    render_footer()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: CATEGORY INPUT
# ══════════════════════════════════════════════════════════════════════════════
elif selected_page == "Category Input":
    st.markdown('<div class="page-title">Category Input</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">For each category: set a target → enter the actual → pick a score → add evidence. Category scores calculate automatically.</div>',
                unsafe_allow_html=True)

    if not st.session_state.employee_info.get("name"):
        st.markdown('<div class="warning-box">⚠️ Please complete <strong>Employee Setup</strong> first — then return here to score.</div>',
                    unsafe_allow_html=True)

    # Category selector tabs
    cat_names = list(CATEGORIES.keys())
    cat_tabs = st.tabs([f"{'✅' if get_category_score(c) else '○'} {c.split(' & ')[0] if ' & ' in c else c[:20]}" for c in cat_names])

    for tab, cat_name in zip(cat_tabs, cat_names):
        cat_data = CATEGORIES[cat_name]
        with tab:
            # Category header info
            col_def, col_score = st.columns([3, 1])
            with col_def:
                st.markdown(f"<div style='font-size:1.05rem;font-weight:700;color:#60A5FA;margin-bottom:0.3rem;'>{cat_name}</div>",
                            unsafe_allow_html=True)
                st.markdown(f"<div style='font-size:0.85rem;color:#E2E8F0;margin-bottom:0.3rem;'>{cat_data['definition']}</div>",
                            unsafe_allow_html=True)
                st.markdown(f"<div style='font-size:0.82rem;color:#94A3B8;font-style:italic;'>Why it matters: {cat_data['why_matters']}</div>",
                            unsafe_allow_html=True)
            with col_score:
                score = get_category_score(cat_name)
                st.markdown(f"""
                <div style='background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:1rem;text-align:center;'>
                    <div style='font-size:0.75rem;color:#64748B;margin-bottom:0.3rem;'>Category Score</div>
                    <div style='font-size:2rem;font-weight:700;color:{SCORE_COLORS.get(int(round(score)), "#94A3B8") if score else "#94A3B8"};'>{score if score else '—'}</div>
                    <div style='font-size:0.75rem;color:#64748B;'>{SCORE_LABELS.get(int(round(score)), "") if score else "Not scored"}</div>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(f"<div style='margin-top:0.5rem;text-align:center;'>{risk_badge(cat_data['bias_risk'])}</div>",
                            unsafe_allow_html=True)

            st.markdown("<hr class='soft-divider'>", unsafe_allow_html=True)

            # Bias note — compact, doesn't compete with metric flow
            st.markdown(f"""<div style='font-size:0.78rem;color:#92400E;background:#FFFBEB;border-left:3px solid #F59E0B;
                border-radius:0 6px 6px 0;padding:0.45rem 0.8rem;margin-bottom:0.9rem;'>
                ⚡ <strong>Bias note ({cat_data["bias_risk"]}):</strong> {cat_data["bias_note"]}
            </div>""", unsafe_allow_html=True)

            for metric in cat_data["metrics"]:
                key_prefix = f"{cat_name}__{metric['name']}"
                with st.container():
                    # Metric header — name, type, what's being measured
                    st.markdown(f"""
                    <div class='category-card' style='padding:0.75rem 1rem;margin-bottom:0.5rem;'>
                        <div style='display:flex;align-items:center;gap:0.6rem;margin-bottom:0.3rem;'>
                            <span style='font-weight:700;color:#1F3864;font-size:0.95rem;'>{metric['name']}</span>
                            {type_badge(metric['type'])}
                        </div>
                        <div style='font-size:0.81rem;color:#64748B;'>{metric['description']} · <em>Logic: {metric['logic']}</em></div>
                    </div>
                    """, unsafe_allow_html=True)

                    # Flow: Target → Actual → Score (3 columns, clear order)
                    col_t, col_a, col_s = st.columns([1.2, 1.2, 0.8])
                    with col_t:
                        target = st.text_input(
                            "① Target / Benchmark", key=f"{key_prefix}__target",
                            value=st.session_state.metric_targets.get(key_prefix, ""),
                            placeholder="e.g. ≥90% on-time"
                        )
                        st.session_state.metric_targets[key_prefix] = target

                    with col_a:
                        actual = st.text_input(
                            "② Actual Value", key=f"{key_prefix}__actual",
                            value=st.session_state.metric_actuals.get(key_prefix, ""),
                            placeholder="e.g. 87%"
                        )
                        st.session_state.metric_actuals[key_prefix] = actual

                    with col_s:
                        score_val = st.selectbox(
                            "③ Score (1–5)", [0, 1, 2, 3, 4, 5],
                            format_func=lambda x: "Select..." if x == 0 else f"{x} — {SCORE_LABELS[x]}",
                            key=f"{key_prefix}__score",
                            index=st.session_state.metric_scores.get(key_prefix, 0)
                        )
                        st.session_state.metric_scores[key_prefix] = score_val

                    # Evidence — last step, clearly numbered
                    evidence = st.text_area(
                        f"④ Evidence Notes  (Source: {metric['source']})",
                        key=f"{key_prefix}__evidence",
                        value=st.session_state.metric_evidence.get(key_prefix, ""),
                        placeholder="Reference a specific deliverable, date, outcome, or data point — not a general description.",
                        height=76
                    )
                    st.session_state.metric_evidence[key_prefix] = evidence
                    st.markdown("<br>", unsafe_allow_html=True)

            # Category score summary
            score = get_category_score(cat_name)
            score_color = SCORE_COLORS.get(int(round(score)), "#94A3B8") if score else "#94A3B8"
            score_label = SCORE_LABELS.get(int(round(score)), "Not scored") if score else "Not scored"
            st.markdown(f"""
            <div style='background:linear-gradient(90deg,#1F3864,#2E5FA3);color:white;padding:1rem 1.5rem;border-radius:10px;display:flex;justify-content:space-between;align-items:center;'>
                <span style='font-weight:600;'>Category Score — {cat_name}</span>
                <span style='font-size:1.4rem;font-weight:700;color:{"#86EFAC" if score and score>=4 else "#FCD34D" if score and score>=3 else "#FCA5A5" if score else "rgba(255,255,255,0.5)"};'>{score if score else "—"} / 5 &nbsp;<span style='font-size:0.85rem;font-weight:400;opacity:0.85;'>{score_label}</span></span>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
    
    render_footer()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: QUALITATIVE REFLECTION
# ══════════════════════════════════════════════════════════════════════════════
elif selected_page == "Qualitative Reflection":
    st.markdown('<div class="page-title">Qualitative Reflection</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Respond to 3 behavioral prompts per category. Reference specific decisions, actions, or outcomes from this quarter — not general self-evaluation. Manager adds observations in the parallel column.</div>',
                unsafe_allow_html=True)

    if not st.session_state.employee_info.get("name"):
        st.markdown('<div class="warning-box">⚠️ Please complete <strong>Employee Setup</strong> first.</div>',
                    unsafe_allow_html=True)

    st.markdown('<div class="info-box">💡 <strong>Strong responses</strong> reference a specific situation, state what you did and why, and describe the outcome. Avoid general statements — describe what actually happened this quarter.</div>',
                unsafe_allow_html=True)

    cat_names = list(CATEGORIES.keys())
    qual_tabs = st.tabs([f"{'✅' if any(st.session_state.qual_responses.get(f'{c}__p{i}','') for i in range(3)) else '○'} {c.split(' & ')[0] if ' & ' in c else c[:20]}" for c in cat_names])

    for tab, cat_name in zip(qual_tabs, cat_names):
        cat_data = CATEGORIES[cat_name]
        with tab:
            # Category context — score + prompt to connect quantitative with qualitative
            score = get_category_score(cat_name)
            score_context = f"Quantitative score: <strong>{score_badge(score)}</strong> — use the prompts below to explain the story behind this score." if score else "No score entered yet. Complete <strong>Category Input</strong> for this category first, then add your reflection here."
            bar_color = "#F0FDF4" if score and score >= 4 else "#FFFBEB" if score and score >= 3 else "#FEF2F2" if score else "#EFF6FF"
            border_color = "#BBF7D0" if score and score >= 4 else "#FDE68A" if score and score >= 3 else "#FECACA" if score else "#BFDBFE"
            st.markdown(f"""
            <div style='background:{bar_color};border:1px solid {border_color};border-radius:8px;
                        padding:0.75rem 1.1rem;margin-bottom:1rem;font-size:0.85rem;color:#374151;'>
                {score_context}
            </div>
            """, unsafe_allow_html=True)

            # Prompts
            for p_idx, (prompt, intent) in enumerate(cat_data["prompts"]):
                st.markdown(f"""
                <div class='prompt-card'>
                    <div style='font-size:0.82rem;color:#9A3412;font-weight:600;margin-bottom:0.3rem;'>PROMPT {p_idx + 1}</div>
                    <div style='font-size:0.92rem;font-weight:600;color:#1F3864;margin-bottom:0.3rem;'>{prompt}</div>
                    <div style='font-size:0.8rem;color:#64748B;font-style:italic;'>Focus: {intent}</div>
                </div>
                """, unsafe_allow_html=True)

                col_emp, col_mgr = st.columns(2)
                emp_key = f"{cat_name}__p{p_idx}"
                mgr_key = f"{cat_name}__mgr__p{p_idx}"

                with col_emp:
                    st.markdown('<div class="field-label">👤 Employee Self-Reflection</div>', unsafe_allow_html=True)
                    emp_resp = st.text_area(
                        f"emp_{emp_key}",
                        value=st.session_state.qual_responses.get(emp_key, ""),
                        placeholder="Describe a specific situation, decision, or outcome from this quarter...",
                        height=130,
                        key=f"qual_emp_{cat_name}_{p_idx}",
                        label_visibility="collapsed"
                    )
                    st.session_state.qual_responses[emp_key] = emp_resp

                with col_mgr:
                    st.markdown('<div class="field-label">👔 Manager Observations</div>', unsafe_allow_html=True)
                    mgr_resp = st.text_area(
                        f"mgr_{mgr_key}",
                        value=st.session_state.manager_notes.get(mgr_key, ""),
                        placeholder="Add independent observations — separate from employee response...",
                        height=130,
                        key=f"qual_mgr_{cat_name}_{p_idx}",
                        label_visibility="collapsed"
                    )
                    st.session_state.manager_notes[mgr_key] = mgr_resp

                st.markdown("<br>", unsafe_allow_html=True)
    
    render_footer()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: USAGE INSTRUCTIONS
# ══════════════════════════════════════════════════════════════════════════════
elif selected_page == "Usage Instructions":
    st.markdown('<div class="page-title">Usage Instructions</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Complete reference guide for employees and managers using this tracker.</div>',
                unsafe_allow_html=True)

    st.markdown('<div class="section-header">📌 What Is This Tracker?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class='metric-card'>
    The PerformX Tracker is a structured framework for documenting, measuring, and reflecting on professional performance 
    across <strong>7 core categories</strong>. It is designed to support quarterly reviews for individuals at any career stage — 
    from early-career to leadership roles.<br><br>
    It was built across 4 phases:
    <ul>
        <li><strong>Phase 1</strong> — Defined 7 universal performance categories with definitions and classifications</li>
        <li><strong>Phase 2</strong> — Designed 2 measurable metrics per category with measurement logic and data sources</li>
        <li><strong>Phase 3</strong> — Created 3 qualitative prompts per category and conducted a bias risk review across all categories</li>
        <li><strong>Phase 4</strong> — This tracker: translates the full framework into a usable, recurring quarterly tool</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">🪜 Step-by-Step Usage</div>', unsafe_allow_html=True)
    steps_detailed = [
        ("Step 1 — Employee Setup", "👤",
         "Navigate to <strong>Employee Setup</strong>. Fill in your name, role, department, manager, and review quarter. This anchors all entries to a specific person and period. Required before any other section."),
        ("Step 2 — Category Input (Employee)", "📋",
         "Navigate to <strong>Category Input</strong>. For each of the 7 categories, you will see 2 metrics. For each metric: set a quarterly target/benchmark, enter the actual value achieved, select a score from 1–5, and add evidence notes citing specific examples or data. The category score auto-calculates as the average of its two metric scores."),
        ("Step 3 — Qualitative Reflection (Employee)", "💬",
         "Navigate to <strong>Qualitative Reflection</strong>. For each category, respond to all 3 prompts in the Employee Self-Reflection column. Responses must reference a specific situation, decision, or outcome from the quarter. Responses of 2–5 sentences are expected. Vague or general answers do not meet the intent of this section."),
        ("Step 4 — Manager Review", "👔",
         "Manager completes the <strong>Manager Observations</strong> column in Qualitative Reflection <em>independently</em> — before discussing with the employee. This ensures observations reflect genuine independent judgment, not a reaction to what the employee wrote."),
        ("Step 5 — Review Together", "🤝",
         "Both parties open the <strong>Overview & Summary</strong> together. Walk through category scores, the radar chart, and strengths vs. watch areas. Then open Qualitative Reflection and compare employee responses with manager observations side-by-side. Focus discussion on categories where perspectives diverge most."),
        ("Step 6 — Agree on Focus Areas", "🎯",
         "Agree on 1–3 priority categories for the next quarter. Document the agreed development focus in the Evidence Notes field of those categories. This creates a direct link between this review and the next quarter's targets."),
    ]
    for title, icon, detail in steps_detailed:
        st.markdown(f"""
        <div class='metric-card' style='display:flex;gap:1rem;'>
            <div style='font-size:1.4rem;flex-shrink:0;'>{icon}</div>
            <div>
                <div style='font-weight:600;color:#1F3864;font-size:0.93rem;margin-bottom:0.3rem;'>{title}</div>
                <div style='font-size:0.85rem;color:#374151;line-height:1.6;'>{detail}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header-grey">⚙️ Key Design Assumptions</div>', unsafe_allow_html=True)
    assumptions = [
        ("Update Frequency", "Quarterly. This tracker is designed for recurring use — complete a new review cycle each quarter."),
        ("Category Weighting", "All 7 categories are weighted equally by default. Managers may adjust emphasis based on role level — reduce weight on Collaboration & Influence for highly independent roles; increase Ownership & Initiative for senior roles."),
        ("Scoring Scale", "All metrics are scored 1–5. Scores should reflect observed outcomes, not effort or intent alone. See the scoring guide in the sidebar."),
        ("Early-Career Roles", "For early-career employees, all 7 categories apply but expect lower scores on Collaboration & Influence. Focus development conversations on Execution, Quality, and Learning & Adaptability."),
        ("Self-Report Reliability", "Qualitative responses depend on honest self-reporting. Where possible, triangulate with peer or stakeholder input. Do not use qualitative responses as the sole basis for high-stakes evaluations."),
        ("No Final Composite Score", "The tracker intentionally does not produce a single composite rating. A single number risks masking important nuance. Use category scores and qualitative responses together to form a holistic view."),
    ]
    for label, detail in assumptions:
        col_l, col_r = st.columns([1, 3])
        with col_l:
            st.markdown(f"<div style='font-weight:600;color:#1F3864;font-size:0.88rem;padding:0.8rem 0;border-bottom:1px solid #E2E8F0;'>{label}</div>", unsafe_allow_html=True)
        with col_r:
            st.markdown(f"<div style='font-size:0.85rem;color:#374151;padding:0.8rem 0;border-bottom:1px solid #E2E8F0;'>{detail}</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-header-orange">⚠️ Known Limitations (from Phase 3 Bias Review)</div>', unsafe_allow_html=True)
    limitations = [
        ("Collaboration & Influence — High Risk", "Favors visible, high-interaction roles. Require documented outcomes, not frequency of collaboration."),
        ("Communication — High Risk", "Risk of rewarding communication style over effectiveness. Evaluate based on actions taken, not volume."),
        ("Ownership & Initiative — High Risk", "Behind-the-scenes prevention work often goes uncredited. Encourage employees to document proactive actions in writing."),
        ("Subjectivity in Qualitative Scoring", "Two managers assessing the same behavior may rate it differently. Calibration sessions recommended."),
        ("Quarterly Fatigue", "Completing all 7 categories every quarter takes effort. If fatigue is an issue, rotate focus: do 3–4 categories deeply each quarter."),
    ]
    for risk, detail in limitations:
        st.markdown(f"""
        <div style='display:flex;gap:0.8rem;align-items:flex-start;padding:0.75rem 0.9rem;
                    border-bottom:1px solid #E2E8F0;background:#FFFBEB;border-radius:6px;margin-bottom:6px;'>
            <span style='font-size:0.9rem;flex-shrink:0;'>⚠️</span>
            <div>
                <div style='font-weight:600;color:#92400E;font-size:0.85rem;'>{risk}</div>
                <div style='font-size:0.83rem;color:#374151;margin-top:0.2rem;'>{detail}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    render_footer()
