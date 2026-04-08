custom_css = """
/* ===== GO AI Bench Theme ===== */
/* Force light mode via Gradio CSS custom properties — no wildcard overrides */

:root, .dark {
    --goai-blue: #1565C0;
    --goai-blue-light: #1E88E5;
    --goai-blue-dark: #0D47A1;
    --goai-yellow: #FFC107;
    --goai-yellow-light: #FFD54F;
    --goai-yellow-dark: #FFA000;

    --body-background-fill: #ffffff !important;
    --body-text-color: #1a1a1a !important;
    --body-text-color-subdued: #555 !important;
    --block-background-fill: #ffffff !important;
    --block-border-color: #e5e7eb !important;
    --block-label-text-color: #333 !important;
    --block-title-text-color: #1a1a1a !important;
    --input-background-fill: #ffffff !important;
    --input-border-color: #d1d5db !important;
    --input-text-color: #1a1a1a !important;
    --checkbox-background-color: #ffffff !important;
    --checkbox-border-color: #d1d5db !important;
    --checkbox-label-text-color: #1a1a1a !important;
    --button-secondary-background-fill: #f9fafb !important;
    --button-secondary-text-color: #1a1a1a !important;
    --button-secondary-border-color: #d1d5db !important;
    --panel-background-fill: #ffffff !important;
    --table-even-background-fill: #f9fafb !important;
    --table-odd-background-fill: #ffffff !important;
    --table-row-focus: #f0f4fa !important;
    --border-color-primary: #e5e7eb !important;
    --background-fill-primary: #ffffff !important;
    --background-fill-secondary: #f9fafb !important;
    --neutral-50: #f9fafb !important;
    --neutral-100: #f3f4f6 !important;
    --neutral-200: #e5e7eb !important;
    --neutral-300: #d1d5db !important;
    --neutral-700: #374151 !important;
    --neutral-800: #1f2937 !important;
    --link-text-color: #1565C0 !important;
    --link-text-color-hover: #0D47A1 !important;
    --checkbox-label-background-fill: #ffffff !important;
    --checkbox-background-color-selected: #1565C0 !important;
    --checkbox-label-background-fill-hover: #f9fafb !important;
    --checkbox-label-background-fill-selected: #eef2ff !important;
    --checkbox-border-color-selected: #1565C0 !important;
    --color-accent: #1565C0 !important;
    --color-accent-soft: rgba(21,101,192,0.12) !important;
    --shadow-drop: none !important;
    --block-shadow: none !important;
}

/* ===== Fixed app width ===== */
.gradio-container {
    max-width: 1200px !important;
    min-width: 0 !important;
    width: 1200px !important;
    margin: 0 auto !important;
}
@media (max-width: 1240px) {
    .gradio-container {
        width: 100% !important;
        padding: 0 16px !important;
    }
}

/* ===== Header ===== */
.goai-header {
    text-align: center;
    padding: 32px 30px 24px 30px;
    border-bottom: 3px solid var(--goai-blue);
    margin-bottom: 20px;
}
.goai-header h1 {
    color: var(--goai-blue) !important;
    font-size: 38px;
    font-weight: 800;
    margin: 0 0 8px 0;
    letter-spacing: -0.5px;
}
.goai-header .goai-subtitle {
    color: #444 !important;
    font-size: 17px;
    max-width: 850px;
    margin: 6px auto;
    line-height: 1.6;
}
.goai-header .goai-links {
    margin-top: 14px;
    font-size: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
}
.goai-header .goai-links a {
    color: var(--goai-blue) !important;
    text-decoration: none;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 4px 10px;
    border-radius: 6px;
    transition: all 0.2s;
}
.goai-header .goai-links a:hover {
    color: var(--goai-blue-dark) !important;
    background: rgba(21,101,192,0.08);
}
.goai-header .goai-links .link-sep {
    color: #bbb;
    font-size: 18px;
}
.goai-header .goai-links .link-icon {
    width: 18px;
    height: 18px;
    flex-shrink: 0;
}
.goai-header .goai-links .hf-logo-svg {
    width: 24px;
    height: 24px;
    flex-shrink: 0;
}
.goai-header .goai-links .linkedin-logo-svg {
    width: 18px;
    height: 18px;
    flex-shrink: 0;
}
.goai-header .goai-logo {
    display: block;
    margin: 18px auto 0 auto;
    max-height: 120px;
    width: auto;
}

/* ===== Tab styling (Gradio 5.x structure: .tab-wrapper > .tab-container) ===== */
.tab-buttons .tab-container {
    justify-content: center !important;
}
.tab-buttons .tab-container > button {
    font-size: 15px !important;
    font-weight: 600 !important;
    padding: 0 18px !important;
    background: #f0f1f3 !important;
    margin-right: 2px !important;
}
.tab-buttons .tab-container > button:hover:not(.selected) {
    background: #e3e8f0 !important;
    color: var(--goai-blue) !important;
}
.tab-buttons .tab-container > button.selected {
    background: #dce6f5 !important;
    color: var(--goai-blue) !important;
}

/* ===== Guide text blocks (between tabs) ===== */
.guide-text {
    font-size: 14px !important;
    padding: 12px 16px !important;
    background: #f0f4fa !important;
    border-left: 4px solid var(--goai-blue) !important;
    border-radius: 0 8px 8px 0 !important;
    margin: 8px 0 12px 0 !important;
    color: #222 !important;
    border: none !important;
    border-left: 4px solid var(--goai-blue) !important;
    box-shadow: none !important;
}
.guide-text p,
.guide-text span,
.guide-text em,
.guide-text li {
    color: #222 !important;
}
.guide-text strong {
    color: var(--goai-blue) !important;
}

/* Bilingual intro (Leaderboard) */
.bilingual-intro {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 20px !important;
    align-items: flex-start !important;
}
.bilingual-col {
    flex: 1 1 320px;
    min-width: 260px;
    max-width: 100%;
}
.bilingual-col p {
    margin: 0 0 10px 0;
}
.bilingual-col p:last-child {
    margin-bottom: 0;
}
.medals-inline {
    display: inline-flex;
    align-items: center;
    vertical-align: middle;
}
.submission-login-hint {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    flex-wrap: wrap !important;
}
.submission-login-hint .inline-icon {
    flex-shrink: 0;
    color: var(--goai-blue);
}

/* Rank column (HTML cells) */
.rank-cell {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    vertical-align: middle;
}
.medal-icon {
    vertical-align: middle;
    display: inline-block;
}

/* Preview card icons */
.preview-header .preview-h3-icon,
.preview-header .preview-h3-icon .inline-icon {
    vertical-align: middle;
    color: #fff;
}
.preview-section .preview-h4-icon,
.preview-section .preview-h4-icon .inline-icon {
    vertical-align: middle;
    margin-right: 6px;
    color: var(--goai-blue);
}
.preview-footer .inline-icon {
    vertical-align: middle;
    margin-right: 4px;
    color: #555;
}

/* Remove extra box around markdown guide-text */
.guide-text.prose {
    border: none !important;
    box-shadow: none !important;
    padding: 12px 16px !important;
}

/* ===== Gold/Silver/Bronze highlighting ===== */
#llm-benchmark-tab-table table tbody tr:nth-child(1) {
    background: rgba(255, 215, 0, 0.12) !important;
}
#llm-benchmark-tab-table table tbody tr:nth-child(2) {
    background: rgba(192, 192, 192, 0.12) !important;
}
#llm-benchmark-tab-table table tbody tr:nth-child(3) {
    background: rgba(205, 127, 50, 0.12) !important;
}

/* ===== Table ===== */
table th {
    background: var(--goai-blue) !important;
    color: white !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 10px 8px !important;
}
table td {
    font-size: 13px !important;
    padding: 8px !important;
    color: #222 !important;
}
table td:first-child,
table th:first-child {
    max-width: 80px;
    text-align: center;
}

/* ===== Buttons ===== */
.goai-btn {
    background: var(--goai-blue) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 10px 24px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    cursor: pointer;
    transition: all 0.2s;
}
.goai-btn:hover {
    background: var(--goai-blue-dark) !important;
    color: white !important;
}

/* ===== Filter sections ===== */
.filter-row {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    padding: 10px 0;
    align-items: flex-end;
}
.filter-row > div {
    flex: 1;
    min-width: 160px;
}

/* ===== Preview card ===== */
.preview-card {
    border: 2px solid var(--goai-blue);
    border-radius: 12px;
    overflow: hidden;
    margin: 12px 0;
    background: #ffffff;
    color: #222;
}
.preview-header {
    background: linear-gradient(135deg, var(--goai-blue) 0%, var(--goai-blue-light) 100%);
    padding: 16px 20px;
    color: white;
}
.preview-header h3 {
    margin: 0 0 8px 0;
    color: white !important;
    font-size: 18px;
}
.preview-badges {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}
.preview-badge {
    background: rgba(255,255,255,0.2);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    color: white;
}
.preview-badge.task {
    background: var(--goai-yellow);
    color: var(--goai-blue-dark);
}
.preview-badge.lang {
    background: rgba(255,255,255,0.3);
}
.preview-section {
    padding: 16px 20px;
    border-bottom: 1px solid #e0e0e0;
}
.preview-section h4 {
    margin: 0 0 12px 0;
    color: var(--goai-blue) !important;
    font-size: 15px;
}
.metric-grid {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}
.metric-card {
    background: #f5f5f5;
    border-radius: 8px;
    padding: 10px 16px;
    text-align: center;
    min-width: 100px;
    flex: 1;
}
.metric-card.metric-primary {
    background: linear-gradient(135deg, var(--goai-blue) 0%, var(--goai-blue-light) 100%);
    color: white;
}
.metric-card.metric-primary .metric-name {
    color: var(--goai-yellow-light);
}
.metric-card.metric-primary .metric-value {
    color: white;
}
.metric-name {
    display: block;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    margin-bottom: 4px;
    color: #666;
}
.metric-value {
    display: block;
    font-size: 20px;
    font-weight: 700;
    color: #222;
}

/* ===== Preview table ===== */
.preview-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
}
.preview-table th {
    background: var(--goai-blue) !important;
    color: white !important;
    padding: 8px 10px !important;
    text-align: left;
}
.preview-table td {
    padding: 6px 10px;
    border-bottom: 1px solid #e0e0e0;
    color: #222 !important;
}
.preview-table tr:nth-child(even) {
    background: #f8f9fa;
}
.preview-table tr:nth-child(odd) {
    background: #ffffff;
}
.preview-footer {
    padding: 12px 20px;
    background: #f5f5f5;
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    color: #555;
}

/* ===== Documentation styling ===== */
.docs-content {
    font-size: 15px !important;
    line-height: 1.7 !important;
    color: #222 !important;
}
.docs-content h2 {
    color: var(--goai-blue) !important;
    border-bottom: 2px solid var(--goai-yellow);
    padding-bottom: 6px;
    margin-top: 24px;
}
.docs-content h3 {
    color: var(--goai-blue-dark) !important;
}
.docs-content table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
}
.docs-content table th {
    background: var(--goai-blue) !important;
    color: white !important;
    padding: 10px !important;
}
.docs-content table td {
    padding: 8px 10px !important;
    border-bottom: 1px solid #e0e0e0;
    color: #222 !important;
}
.docs-content code {
    background: rgba(21,101,192,0.08);
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 13px;
    color: #333;
}
.docs-content pre {
    background: #f5f6fa !important;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 12px 16px;
    overflow-x: auto;
}
.docs-content pre code {
    background: transparent;
    padding: 0;
}
.docs-content hr {
    border: none;
    border-top: 2px solid var(--goai-yellow);
    margin: 24px 0;
}

/* ===== Citation ===== */
#citation-button span {
    font-size: 14px !important;
}
#citation-button textarea {
    font-size: 13px !important;
}

/* ===== OAuth / Login button ===== */
#oauth-button,
#oauth-button a,
#oauth-button button {
    padding: 10px 20px !important;
    border-radius: 8px !important;
    background: var(--goai-blue) !important;
    color: white !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    border: none !important;
}
#oauth-button:hover,
#oauth-button a:hover,
#oauth-button button:hover {
    background: var(--goai-blue-dark) !important;
    color: white !important;
}
#oauth-button svg {
    filter: none !important;
}
#oauth-button img {
    filter: none !important;
}

/* ===== Hide last dummy column ===== */
#llm-benchmark-tab-table table td:last-child,
#llm-benchmark-tab-table table th:last-child {
    display: none;
}

/* ===== Logo sizing ===== */
#scale-logo {
    border-style: none !important;
    box-shadow: none;
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-width: 600px;
}
"""

get_window_url_params = """
    function(url_params) {
        const params = new URLSearchParams(window.location.search);
        url_params = Object.fromEntries(params);
        return url_params;
    }
"""
