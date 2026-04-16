def load_css():
    return """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background-color: #0d0f14;
        color: #e8e6e1;
    }

    .block-container {
        padding: 2.5rem 2rem 4rem;
        max-width: 780px;
    }

    /* ── Hero ── */
    .hero {
        text-align: center;
        padding: 3.5rem 1rem 2rem;
        margin-bottom: 2.5rem;
    }
    .hero-tag {
        display: inline-block;
        font-size: 0.7rem;
        font-weight: 500;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #c9a84c;
        border: 1px solid #c9a84c44;
        padding: 0.3rem 0.9rem;
        border-radius: 999px;
        margin-bottom: 1.2rem;
    }
    .hero h1 {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 700;
        color: #f0ede8;
        margin: 0 0 0.75rem;
        line-height: 1.2;
    }
    .hero h1 span { color: #c9a84c; }
    .hero p {
        color: #8a8883;
        font-size: 1rem;
        font-weight: 300;
        max-width: 460px;
        margin: 0 auto;
        line-height: 1.6;
    }

    /* ── Section label ── */
    .section-label {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin: 2rem 0 1rem;
    }
    .section-label .line {
        flex: 1;
        height: 1px;
        background: #1e2028;
    }
    .section-label span {
        font-size: 0.7rem;
        font-weight: 500;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #4a4e5a;
    }

    /* ── Inputs & Sliders ── */
    div[data-testid="stNumberInput"] label,
    div[data-testid="stSlider"] label {
        color: #8a8883 !important;
        font-size: 0.82rem !important;
        font-weight: 400 !important;
        letter-spacing: 0.03em;
    }

    div[data-testid="stNumberInput"] input {
        background: #13161d !important;
        border: 1px solid #1e2330 !important;
        border-radius: 8px !important;
        color: #f0ede8 !important;
        font-family: 'DM Sans', sans-serif !important;
        transition: border-color 0.2s;
    }
    div[data-testid="stNumberInput"] input:focus {
        border-color: #c9a84c !important;
        box-shadow: 0 0 0 2px #c9a84c22 !important;
    }

    div[data-testid="stSlider"] [data-testid="stSliderThumb"] {
        background: #c9a84c !important;
    }
    div[data-testid="stSlider"] [role="slider"] {
        background: #c9a84c !important;
    }

    /* ── Divider ── */
    hr {
        border-color: #1a1d24 !important;
        margin: 1.5rem 0 !important;
    }

    /* ── Button ── */
    div[data-testid="stButton"] button {
        background: #c9a84c !important;
        color: #0d0f14 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.85rem !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        width: 100% !important;
        transition: background 0.2s, transform 0.1s !important;
        margin-top: 0.5rem;
    }
    div[data-testid="stButton"] button:hover {
        background: #e0bc62 !important;
        transform: translateY(-1px);
    }
    div[data-testid="stButton"] button:active {
        transform: translateY(0);
    }

    /* ── Result box ── */
    .result-box {
        background: linear-gradient(135deg, #13161d 0%, #191c24 100%);
        border: 1px solid #c9a84c33;
        border-radius: 16px;
        padding: 2.5rem 2rem;
        text-align: center;
        margin-top: 2rem;
        animation: fadeUp 0.4s ease;
    }
    .result-box .label {
        font-size: 0.7rem;
        font-weight: 500;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #c9a84c;
        margin-bottom: 0.75rem;
    }
    .result-box .price {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #f0ede8;
        line-height: 1;
    }
    .result-box .sub {
        color: #4a4e5a;
        font-size: 0.8rem;
        margin-top: 0.6rem;
        font-weight: 300;
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(12px); }
        to   { opacity: 1; transform: translateY(0); }
    }
</style>
"""