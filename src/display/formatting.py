def model_hyperlink(link, model_name):
    return f'<a target="_blank" href="{link}" style="color: var(--link-text-color); text-decoration: underline; text-decoration-style: dotted;">{model_name}</a>'


def make_clickable_model(model_name):
    link = f"https://huggingface.co/{model_name}"
    return model_hyperlink(link, model_name)


def styled_error(error):
    return f"<p style='color: #c62828; font-size: 18px; text-align: center; padding: 12px; background: #ffebee; border-radius: 8px;'>{error}</p>"


def styled_warning(warn):
    return f"<p style='color: #e65100; font-size: 18px; text-align: center; padding: 12px; background: #fff3e0; border-radius: 8px;'>{warn}</p>"


def styled_message(message):
    return f"<p style='color: #1b5e20; font-size: 18px; text-align: center; padding: 12px; background: #e8f5e9; border-radius: 8px;'>{message}</p>"


MEDAL_ICONS = {1: "🥇", 2: "🥈", 3: "🥉"}


def rank_label(rank):
    medal = MEDAL_ICONS.get(rank, "")
    return f"{medal} {rank}" if medal else str(rank)
