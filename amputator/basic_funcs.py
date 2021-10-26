from amputator.helpers.utils import get_urls, get_urls_info, check_if_amp

def generate_message(links):
    # Initialize all variables
    canonical_text_latest, canonical_text_list, canonical_text = "", "", ""
    n_canonicals = 0

    # Loop through all links, and generate the canonical link part of the comment
    for link in links:
        if link.is_amp:
            if link.canonical:
                n_canonicals += 1
                canonical_text_latest += link.canonical
                canonical_text_list += f"[{n_canonicals}] <{link.canonical}>\n"

    if n_canonicals >= 1:
        if n_canonicals == 1:
            intro_who_wat = "It looks like you shared a cached AMP link. These should load faster, but Google's " \
                            "AMP is controversial because of concerns over privacy and the Open Web: " \
                            "<https://reddit.com/r/AmputatorBot/comments/ehrq3z/why_did_i_build_amputatorbot/> "
            intro_maybe = "\n\nYou might want to visit the uncached page instead: "
            canonical_text = f"<{canonical_text_latest}>"

        else:
            intro_who_wat = "It looks like you shared some cached AMP links. "
            intro_maybe = "You might want to visit the uncached pages instead: "
            canonical_text = canonical_text_list

        tweet_text = intro_who_wat + intro_maybe + canonical_text

        return tweet_text

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