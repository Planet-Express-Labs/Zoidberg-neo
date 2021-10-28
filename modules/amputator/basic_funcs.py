from utils.amputator_utils import get_urls, get_urls_info, check_if_amp

def generate_message(links):
    # Initialize all variables
    canonical_text_latest, canonical_text_list, canonical_text = "", "", ""
    n_canonicals = 0

    # Loop through all links, and generate the canonical link part of the comment
    for link in links:
        if link.is_amp:
            if link.canonical:
                n_canonicals += 1
                canonical_text_list += f" - <{link.canonical}>\n"

    if n_canonicals >= 1:
        intro = "It looks like you shared some cached AMP links. [That's bad](https://reddit.com/r/AmputatorBot/comments/ehrq3z/why_did_i_build_amputatorbot/). You might want to visit the uncached pages instead: \n\n"
        canonical_text = canonical_text_list

        reply_text = intro + canonical_text

        return reply_text

    return None

def get_reply(message):
    if not check_if_amp(message):
        return
    urls = get_urls(message)
    links = get_urls_info(urls)

    if any(link.is_amp for link in links):
        return generate_message(links)
    else:
        return