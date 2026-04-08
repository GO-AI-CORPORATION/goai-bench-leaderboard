"""Small inline SVG icons (Gradio Markdown strips most HTML; use in gr.HTML / Dataframe html cells)."""

# Brand: https://huggingface.co/brand — jaune #FFD21E, orange #FF9D00
HF_LOGO_SVG = """<svg class="link-icon hf-logo-svg" viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="128" cy="128" r="120" fill="#FFD21E"/><path d="M70 108c12-28 48-28 60 0" fill="none" stroke="#1f2937" stroke-width="14" stroke-linecap="round"/><path d="M126 108c12-28 48-28 60 0" fill="none" stroke="#1f2937" stroke-width="14" stroke-linecap="round"/><path d="M72 158c20 36 92 36 112 0" fill="none" stroke="#1f2937" stroke-width="12" stroke-linecap="round"/><circle cx="62" cy="148" r="22" fill="#FF9D00" opacity="0.9"/><circle cx="194" cy="148" r="22" fill="#FF9D00" opacity="0.9"/></svg>"""

LINKEDIN_LOGO_SVG = """<svg class="link-icon linkedin-logo-svg" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path fill="#0A66C2" d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>"""


def _medal_svg(rank: int) -> str:
    if rank == 1:
        fill = "#FFD700"
    elif rank == 2:
        fill = "#C0C0C0"
    else:
        fill = "#CD7F32"
    return (
        f'<svg class="medal-icon" width="18" height="18" viewBox="0 0 24 24" '
        f'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
        f'<circle cx="12" cy="12" r="10" fill="{fill}" stroke="#8B6914" stroke-width="0.5"/>'
        f'<text x="12" y="15" text-anchor="middle" font-size="11" font-weight="700" fill="#333">{rank}</text>'
        f"</svg>"
    )


def rank_cell_html(rank: int) -> str:
    if rank <= 3:
        return f'<span class="rank-cell">{_medal_svg(rank)} <span class="rank-num">{rank}</span></span>'
    return f'<span class="rank-cell"><span class="rank-num">{rank}</span></span>'


def icon_lock(size: int = 16) -> str:
    return (
        f'<svg class="inline-icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="2" aria-hidden="true">'
        f'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'
    )


def icon_rocket(size: int = 16) -> str:
    return (
        f'<svg class="inline-icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="2" aria-hidden="true">'
        f'<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/>'
        f'<path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>'
        f'<path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>'
    )


def icon_check(size: int = 16) -> str:
    return (
        f'<svg class="inline-icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="2.5" aria-hidden="true">'
        f'<path d="M20 6L9 17l-5-5"/></svg>'
    )


def icon_clock(size: int = 16) -> str:
    return (
        f'<svg class="inline-icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="2" aria-hidden="true">'
        f'<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
    )


def icon_warning(size: int = 16) -> str:
    return (
        f'<svg class="inline-icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="2" aria-hidden="true">'
        f'<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>'
        f'<line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
    )


def icon_clipboard(size: int = 16) -> str:
    return (
        f'<svg class="inline-icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="2" aria-hidden="true">'
        f'<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/>'
        f'<rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>'
    )


def icon_chart(size: int = 16) -> str:
    return (
        f'<svg class="inline-icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="2" aria-hidden="true">'
        f'<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/>'
        f'<line x1="6" y1="20" x2="6" y2="14"/></svg>'
    )


def icon_tag(size: int = 16) -> str:
    return (
        f'<svg class="inline-icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="2" aria-hidden="true">'
        f'<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/>'
        f'<line x1="7" y1="7" x2="7.01" y2="7"/></svg>'
    )


def icon_note(size: int = 16) -> str:
    return (
        f'<svg class="inline-icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="2" aria-hidden="true">'
        f'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>'
        f'<polyline points="14 2 14 8 20 8"/></svg>'
    )


def icon_medals_row(size: int = 14) -> str:
    """Three medal dots for intro text."""
    gold, sil, brz = "#FFD700", "#C0C0C0", "#CD7F32"
    return (
        f'<span class="medals-inline" aria-hidden="true">'
        f'<svg width="{size}" height="{size}" viewBox="0 0 12 12" style="vertical-align:-2px;margin-right:2px">'
        f'<circle cx="6" cy="6" r="5" fill="{gold}"/></svg>'
        f'<svg width="{size}" height="{size}" viewBox="0 0 12 12" style="vertical-align:-2px;margin-right:2px">'
        f'<circle cx="6" cy="6" r="5" fill="{sil}"/></svg>'
        f'<svg width="{size}" height="{size}" viewBox="0 0 12 12" style="vertical-align:-2px">'
        f'<circle cx="6" cy="6" r="5" fill="{brz}"/></svg>'
        f"</span>"
    )
