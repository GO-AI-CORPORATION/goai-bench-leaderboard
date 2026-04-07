custom_css = """
/* ===== GO AI Bench Theme: Blue (#1565C0) + Yellow (#FFC107) on white ===== */

:root {
    --goai-blue: #1565C0;
    --goai-blue-light: #1E88E5;
    --goai-blue-dark: #0D47A1;
    --goai-yellow: #FFC107;
    --goai-yellow-light: #FFD54F;
    --goai-yellow-dark: #FFA000;
    --goai-gold: #FFD700;
    --goai-silver: #C0C0C0;
    --goai-bronze: #CD7F32;
}

/* ===== Force light mode everywhere ===== */
body,
body.dark,
.gradio-container,
.dark .gradio-container {
    background: #ffffff !important;
    color: #1a1a1a !important;
}

/* Force all text to be dark on white — covers dark-mode browsers */
.gradio-container *,
.dark .gradio-container * {
    --body-text-color: #1a1a1a !important;
    --block-label-text-color: #333 !important;
    --block-title-text-color: #1a1a1a !important;
    --input-text-color: #1a1a1a !important;
}
.gradio-container p,
.gradio-container span,
.gradio-container li,
.gradio-container label,
.gradio-container .prose,
.gradio-container .markdown,
.dark .gradio-container p,
.dark .gradio-container span,
.dark .gradio-container li,
.dark .gradio-container label,
.dark .gradio-container .prose,
.dark .gradio-container .markdown {
    color: #1a1a1a !important;
}
.gradio-container strong,
.dark .gradio-container strong {
    color: var(--goai-blue) !important;
}
.gradio-container em,
.dark .gradio-container em {
    color: #333 !important;
}
.gradio-container a,
.dark .gradio-container a {
    color: var(--goai-blue) !important;
}

/* All panels/blocks white background */
.gradio-container .block,
.gradio-container .panel,
.gradio-container .form,
.gradio-container .tabitem,
.dark .gradio-container .block,
.dark .gradio-container .panel,
.dark .gradio-container .form,
.dark .gradio-container .tabitem {
    background: #ffffff !important;
    border-color: #e0e0e0 !important;
}

/* ===== Header — white background ===== */
.goai-header {
    text-align: center;
    padding: 28px 30px 20px 30px;
    background: #ffffff !important;
    border-bottom: 3px solid var(--goai-blue);
    margin-bottom: 20px;
}
.goai-header h1 {
    color: var(--goai-blue) !important;
    font-size: 30px;
    font-weight: 800;
    margin: 0 0 6px 0;
}
.goai-header .goai-subtitle {
    color: #444 !important;
    font-size: 15px;
    max-width: 800px;
    margin: 4px auto;
    line-height: 1.5;
}
.goai-header .goai-links {
    margin-top: 10px;
    font-size: 14px;
}
.goai-header .goai-links a {
    color: var(--goai-blue) !important;
    text-decoration: none;
    font-weight: 600;
    margin: 0 8px;
}
.goai-header .goai-links a:hover {
    color: var(--goai-yellow-dark) !important;
    text-decoration: underline;
}
.goai-header .goai-logo {
    display: block;
    margin: 14px auto 0 auto;
    max-height: 90px;
    width: auto;
}

/* ===== Tab styling — centered labels ===== */
/* Target Gradio's internal tablist container at every nesting level */
.tab-buttons > div,
.tab-buttons [role="tablist"],
.tabs > .tab-nav,
div.tabs > div.tab-nav,
div.tabitem .tabs > .tab-nav,
.gradio-container .tabs > .tab-nav {
    justify-content: center !important;
    display: flex !important;
}
.tab-buttons button,
.tabs > .tab-nav > button {
    font-size: 15px !important;
    font-weight: 600 !important;
    border-radius: 8px 8px 0 0 !important;
    color: #444 !important;
    background: transparent !important;
    border-bottom: 2px solid transparent !important;
    padding: 10px 18px !important;
}
.tab-buttons button:hover,
.tabs > .tab-nav > button:hover {
    color: var(--goai-blue) !important;
    background: rgba(21,101,192,0.04) !important;
}
.tab-buttons button.selected,
.tabs > .tab-nav > button.selected {
    background: rgba(21,101,192,0.08) !important;
    color: var(--goai-blue) !important;
    border-bottom: 3px solid var(--goai-yellow) !important;
}

/* ===== Guide text blocks ===== */
.guide-text {
    font-size: 14px !important;
    padding: 12px 16px !important;
    background: #f0f4fa !important;
    border-left: 4px solid var(--goai-blue) !important;
    border-radius: 0 8px 8px 0 !important;
    margin: 8px 0 12px 0 !important;
    color: #222 !important;
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
    background: #ffffff !important;
}
table td:first-child,
table th:first-child {
    max-width: 80px;
    text-align: center;
}

/* (buttons styled below with OAuth section) */

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
    background: #ffffff !important;
    color: #222 !important;
}
.preview-header {
    background: linear-gradient(135deg, var(--goai-blue) 0%, var(--goai-blue-light) 100%);
    padding: 16px 20px;
    color: white !important;
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
    color: white !important;
}
.preview-badge.task {
    background: var(--goai-yellow);
    color: var(--goai-blue-dark) !important;
}
.preview-badge.lang {
    background: rgba(255,255,255,0.3);
}
.preview-section {
    padding: 16px 20px;
    border-bottom: 1px solid #e0e0e0;
    background: #ffffff !important;
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
    background: #f5f5f5 !important;
    border-radius: 8px;
    padding: 10px 16px;
    text-align: center;
    min-width: 100px;
    flex: 1;
}
.metric-card.metric-primary {
    background: linear-gradient(135deg, var(--goai-blue) 0%, var(--goai-blue-light) 100%) !important;
    color: white !important;
}
.metric-card.metric-primary .metric-name {
    color: var(--goai-yellow-light) !important;
}
.metric-card.metric-primary .metric-value {
    color: white !important;
}
.metric-card.metric-secondary .metric-value {
    color: #222 !important;
}
.metric-name {
    display: block;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    margin-bottom: 4px;
    color: #666 !important;
}
.metric-value {
    display: block;
    font-size: 20px;
    font-weight: 700;
    color: #222 !important;
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
    background: transparent;
}
.preview-table tr:nth-child(even) {
    background: #f8f9fa !important;
}
.preview-table tr:nth-child(odd) {
    background: #ffffff !important;
}
.preview-footer {
    padding: 12px 20px;
    background: #f5f5f5 !important;
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    color: #555 !important;
}

/* ===== Documentation styling ===== */
.docs-content {
    font-size: 15px !important;
    line-height: 1.7 !important;
    color: #222 !important;
}
.docs-content p,
.docs-content li,
.docs-content span {
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
    background: #ffffff !important;
}
.docs-content code {
    background: rgba(21,101,192,0.08) !important;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 13px;
    color: #333 !important;
}
.docs-content pre {
    background: #f5f6fa !important;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 12px 16px;
    overflow-x: auto;
}
.docs-content pre code {
    background: transparent !important;
    padding: 0;
    color: #333 !important;
}
.docs-content hr {
    border: none;
    border-top: 2px solid var(--goai-yellow);
    margin: 24px 0;
}

/* ===== Citation ===== */
#citation-button span {
    font-size: 14px !important;
    color: #222 !important;
}
#citation-button textarea {
    font-size: 13px !important;
    color: #222 !important;
    background: #ffffff !important;
}

/* ===== OAuth / Login button ===== */
#oauth-button,
#oauth-button a,
#oauth-button button {
    height: auto;
    min-width: max-content;
    white-space: nowrap;
    padding: 10px 20px !important;
    border-radius: 8px !important;
    background: var(--goai-blue) !important;
    color: white !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    border: none !important;
    transition: all 0.2s;
}
#oauth-button:hover,
#oauth-button:hover a,
#oauth-button:hover button,
#oauth-button a:hover,
#oauth-button button:hover {
    background: var(--goai-blue-dark) !important;
    color: white !important;
}
#oauth-button *,
#oauth-button:hover * {
    color: white !important;
}

/* ===== Submit button — same style as OAuth ===== */
.goai-btn,
.goai-btn:active {
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

/* ===== Gradio component overrides for forced light ===== */
.gradio-container input,
.gradio-container textarea,
.gradio-container select,
.dark .gradio-container input,
.dark .gradio-container textarea,
.dark .gradio-container select {
    color: #1a1a1a !important;
    background: #ffffff !important;
}
.gradio-container .label-wrap,
.gradio-container .label-wrap span,
.dark .gradio-container .label-wrap,
.dark .gradio-container .label-wrap span {
    color: #333 !important;
}
"""

get_window_url_params = """
    function(url_params) {
        const params = new URLSearchParams(window.location.search);
        url_params = Object.fromEntries(params);
        return url_params;
    }
"""
