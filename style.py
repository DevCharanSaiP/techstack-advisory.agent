# style.py
# Accessible, theme-aware CSS for the Tech Stack Architecture Advisor (works with app.py)
# Exports a single string variable `CSS` which app.py injects via gr.HTML(CSS + "...").

CSS = """
<!-- Optional Google fonts (safe, but app works without them) -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Roboto+Slab:ital,wght@0,400;0,700&display=swap" rel="stylesheet">

<style>
/* Basic reset and sensible defaults */
:root{
  --radius: 12px;
  --transition-fast: 0.12s ease;
  --focus-ring: 3px;
  --max-width: 1100px;

  /* Light theme defaults */
  --bg-page: #f6f7fb;
  --bg-panel: rgba(255,255,255,0.9);
  --panel-border: rgba(16,24,40,0.06);
  --text-primary: #0f1724;
  --text-muted: #506075;
  --accent: linear-gradient(90deg,#005fff,#00c6ff);
  --accent-solid: #ff6a00; /* for primary button if you prefer a solid color */
  --card-bg: linear-gradient(180deg, rgba(255,255,255,0.96), rgba(255,255,255,0.92));
  --shadow-strong: 0 22px 56px rgba(15,20,30,0.12);
  --shadow-subtle: 0 6px 20px rgba(15,20,30,0.06);
}

/* Dark theme overrides: high contrast text for dark mode */
@media (prefers-color-scheme: dark) {
  :root{
    --bg-page: linear-gradient(180deg, #05060a, #0b0d14);
    --bg-panel: rgba(10,12,20,0.6);
    --panel-border: rgba(255,255,255,0.04);
    --text-primary: #e7eefc;
    --text-muted: #a9b6d6;
    --accent: linear-gradient(90deg,#6b5cff,#00c6ff);
    --accent-solid: #ff8a3d;
    --card-bg: linear-gradient(180deg, rgba(8,10,18,0.6), rgba(8,10,18,0.5));
    --shadow-strong: 0 26px 68px rgba(2,4,10,0.7);
    --shadow-subtle: 0 8px 26px rgba(2,4,10,0.35);
  }
}

/* Page background + container centering */
html,body{
  height:100%;
  margin:0;
  background: var(--bg-page);
  font-family: 'Inter', system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  -webkit-font-smoothing:antialiased;
  -moz-osx-font-smoothing:grayscale;
  color: var(--text-primary);
}

/* Top title block used by app.py */
#title-wrap{
  max-width: var(--max-width);
  margin: 28px auto 18px;
  padding: 18px 22px;
  text-align: center;
  border-radius: calc(var(--radius) + 6px);
  background: transparent;
  border: 1px solid var(--panel-border);
  box-shadow: var(--shadow-subtle);
}
#title-wrap h1{
  margin: 0 0 6px;
  font-family: 'Roboto Slab', 'Playfair Display', serif;
  font-size: 28px;
  font-weight:700;
  color: var(--text-primary);
}
#title-wrap p{
  margin:0;
  font-size:13px;
  color: var(--text-muted);
}

/* Main panel container (app.py uses elem_classes=["panel"]) */
.panel, .spellbook-panel, .gradio-container .panel {
  max-width: var(--max-width);
  margin: 20px auto;
  padding: 22px;
  border-radius: calc(var(--radius) + 4px);
  background: var(--bg-panel);
  border: 1px solid var(--panel-border);
  box-shadow: var(--shadow-strong);
  backdrop-filter: blur(6px) saturate(120%);
}

/* Make gradio inner containers transparent so our panel color shows */
.gradio-container, .gradio-html {
  background: transparent !important;
}

/* Rows and layout helpers */
.panel .gr-row, .panel .gradio-row {
  display:flex;
  flex-wrap:wrap;
  gap:12px;
  align-items:center;
}

/* Labels */
.panel label, .panel .gr-label {
  display:block;
  margin-bottom:6px;
  color: var(--text-primary);
  font-weight:600;
  font-size:13px;
}

/* Inputs sizing hint */
.panel .gr-dropdown, .panel .gr-textbox, .panel .gr-radio {
  min-width:160px;
}

/* Primary and secondary buttons */
button, .gr-button, .gradio-button {
  font-family: inherit;
  font-weight: 600;
  border-radius: 10px;
  padding: 10px 16px;
  border: none;
  cursor: pointer;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), opacity var(--transition-fast);
  box-shadow: var(--shadow-subtle);
  color: white;
}

/* Primary variant: gradient, accessible contrast */
.gr-button[variant="primary"], .gr-button--primary, .gradio-button--primary {
  background: var(--accent);
  background-clip: padding-box;
  color: white;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  border: 1px solid rgba(255,255,255,0.04);
}

/* If you want a solid accent alternative for clearer contrast, .btn-solid can be applied */
.btn-solid { background: var(--accent-solid); color: white; }

/* Secondary variant is subtle and readable */
.gr-button[variant="secondary"], .gr-button--secondary {
  background: transparent;
  color: var(--text-primary);
  border: 1px solid var(--panel-border);
}

/* Button hover/focus */
button:hover, .gr-button:hover { transform: translateY(-2px); opacity:0.98; }
button:active { transform: translateY(0); }
button:focus, .gr-button:focus {
  outline: none;
  box-shadow: 0 8px 34px rgba(0,0,0,0.12), 0 0 0 var(--focus-ring) rgba(100,116,255,0.12);
  border-radius:10px;
}

/* Output / Markdown (.arch-output element_class used in app.py) */
.arch-output, .gr-markdown.arch-output {
  margin-top: 14px;
  padding: 16px;
  border-radius: 10px;
  background: var(--card-bg);
  border: 1px solid var(--panel-border);
  box-shadow: var(--shadow-subtle);
  color: var(--text-primary);
  font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  line-height: 1.45;
  white-space: pre-wrap;
  word-break: break-word;
  min-height: 88px;
}

/* Make sure links and code in the Markdown are visible in both themes */
.arch-output a {
  color: #7fb7ff;
}
@media (prefers-color-scheme: dark) {
  .arch-output a { color: #9fd8ff; }
}
.arch-output code, .arch-output pre {
  background: rgba(0,0,0,0.06);
  padding: 4px 8px;
  border-radius: 6px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", monospace;
  color: var(--text-primary);
}
@media (prefers-color-scheme: dark) {
  .arch-output code, .arch-output pre {
    background: rgba(255,255,255,0.03);
  }
}

/* Accessibility: increase font size a bit for better legibility */
.panel, .arch-output { font-size: 15px; }

/* Small helper note style */
.small-note {
  font-size: 12px;
  color: var(--text-muted);
}

/* Responsive tweaks */
@media (max-width: 880px){
  .panel { padding: 14px; margin: 14px; border-radius: 12px; }
  #title-wrap h1 { font-size: 20px; }
  .arch-output { font-size: 14px; min-height: 72px; }
}

/* Ensure contrast on extremely small/low-contrast devices:
   if the user's system has forced colors, fall back to very high contrast */
@media (forced-colors: active) {
  :root {
    --bg-page: #000;
    --bg-panel: #000;
    --panel-border: #fff;
    --text-primary: #fff;
    --text-muted: #ddd;
    --card-bg: #000;
  }
  .gr-button[variant="primary"], .gr-button--primary { background: #000; color: #fff; border: 2px solid #fff; }
}

/* Small utility: ensure placeholder text is readable */
input::placeholder, textarea::placeholder {
  color: rgba(80,96,128,0.36);
}
@media (prefers-color-scheme: dark) {
  input::placeholder, textarea::placeholder { color: rgba(180,190,220,0.28); }
}
</style>
"""