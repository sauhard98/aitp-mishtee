mishtee_css = """
/* Global Container & Background */
body, .gradio-container {
    background-color: #FAF9F6 !important; /* Off-White */
    color: #333333 !important; /* Charcoal */
}

/* Typography: Headings (Serif, Spaced-out) */
h1, h2, h3, h4 {
    font-family: 'Playfair Display', 'Times New Roman', serif !important;
    font-weight: 400 !important;
    letter-spacing: 2px !important;
    margin-bottom: 25px !important;
    color: #333333 !important;
}

/* Typography: Standard Text (Lightweight Sans) */
p, label, span {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
    font-weight: 300 !important;
    font-size: 16px !important;
}

/* Buttons: Sober Terracotta, Sharp Lines */
button {
    background-color: #C06C5C !important; /* Sober Terracotta */
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 0px !important; /* Sharp corners constraint */
    box-shadow: none !important; /* No shadow constraint */
    padding: 12px 24px !important;
    font-family: 'Helvetica Neue', sans-serif !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    transition: opacity 0.3s ease;
}

button:hover {
    opacity: 0.9;
}

/* Inputs & Boxes: Thin Borders, No Rounding */
input, textarea, .gr-box, .gr-input, .gr-panel {
    background-color: #FFFFFF !important;
    border: 1px solid #E0E0E0 !important; /* Thin border */
    border-radius: 0px !important;
    box-shadow: none !important;
    padding: 10px !important;
}

/* Tables: Minimalist, High Whitespace */
table {
    font-family: 'Helvetica Neue', sans-serif !important;
    border-collapse: collapse !important;
    width: 100%;
    margin-top: 20px;
}

thead th {
    font-weight: 400 !important;
    text-transform: uppercase;
    border-bottom: 1px solid #333333 !important;
    padding: 15px !important;
    text-align: left;
}

tbody td {
    font-weight: 300 !important;
    border-bottom: 1px solid #E0E0E0 !important;
    padding: 20px 15px !important; /* Significant padding */
}

/* Remove default Gradio shadows/rounding globally */
* {
    box-shadow: none !important;
    border-radius: 0px !important;
}
"""
