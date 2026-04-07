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

/* Force light mode */
.gradio-container {
    background: #ffffff !important;
    color: #1a1a1a !important;
    max-width: 1200px;
    margin: auto;
}
.dark .gradio-container,
.dark {
    background: #ffffff !important;
    color: #1a1a1a !important;
}

/* Header — white background */
.goai-header {
    text-align: center;
    padding: 28px 30px 20px 30px;
    background: #ffffff;
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
    color: #444;
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

/* Tab styling — centered */
.tab-buttons {
    display: flex;
    justify-content: center !important;
}
.tab-buttons > div {
    display: flex;
    justify-content: center !important;
}
.tab-buttons button {
    font-size: 15px !important;
    font-weight: 600;
    border-radius: 8px 8px 0 0 !important;
    color: #555 !important;
    background: transparent !important;
    border-bottom: 2px solid transparent !important;
    padding: 10px 18px !important;
}
.tab-buttons button:hover {
    color: var(--goai-blue) !important;
    background: rgba(21,101,192,0.04) !important;
}
.tab-buttons button.selected {
    background: rgba(21,101,192,0.08) !important;
    color: var(--goai-blue) !important;
    border-bottom: 3px solid var(--goai-yellow) !important;
}

/* Guide text blocks between tabs */
.guide-text {
    font-size: 14px !important;
    padding: 12px 16px;
    background: linear-gradient(90deg, rgba(21,101,192,0.05) 0%, rgba(255,193,7,0.04) 100%);
    border-left: 4px solid var(--goai-blue);
    border-radius: 0 8px 8px 0;
    margin: 8px 0 12px 0;
    color: #333;
}
.guide-text strong {
    color: var(--goai-blue);
}

/* Gold/Silver/Bronze highlighting */
#llm-benchmark-tab-table table tbody tr:nth-child(1) {
    background: rgba(255, 215, 0, 0.12) !important;
}
#llm-benchmark-tab-table table tbody tr:nth-child(2) {
    background: rgba(192, 192, 192, 0.12) !important;
}
#llm-benchmark-tab-table table tbody tr:nth-child(3) {
    background: rgba(205, 127, 50, 0.12) !important;
}

/* Table headers */
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

/* Buttons */
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
    background: var(--goai-yellow) !important;
    color: var(--goai-blue-dark) !important;
}

/* Filter sections */
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

/* Preview card */
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
    color: var(--goai-blue);
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
.metric-card.metric-secondary .metric-value {
    color: #222;
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

/* Preview table — dark text on light backgrounds */
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

/* Documentation styling */
.docs-content {
    font-size: 15px;
    line-height: 1.7;
    color: #222;
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

/* Citation */
#citation-button span {
    font-size: 14px !important;
}
#citation-button textarea {
    font-size: 13px !important;
}

/* OAuth button */
#oauth-button {
    height: auto;
    min-width: max-content;
    white-space: nowrap;
    padding: 10px 20px;
    border-radius: 8px;
    background: var(--goai-blue) !important;
}

/* Hide last dummy column */
#llm-benchmark-tab-table table td:last-child,
#llm-benchmark-tab-table table th:last-child {
    display: none;
}

/* Logo sizing */
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
