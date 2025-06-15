import random

def simulate_persona() -> dict:
    roles = [
        "retired climate scientist",
        "burnt-out war reporter",
        "failed biotech entrepreneur",
        "underground mushroom forager",
        "exiled ethics professor",
        "DIY biohacker in a basement lab",
        "former AI alignment cultist"
    ]

    moods = [
        "quiet rage",
        "existential dread",
        "melancholic awe",
        "apathetic detachment",
        "unprocessed grief",
        "post-hope curiosity",
        "delusional optimism"
    ]

    crises = [
        "watching glaciers melt alone",
        "decoding surveillance footage of pigeons",
        "collecting unread apology emails",
        "having prophetic dreams in binary",
        "trying to compost emotional baggage",
        "hoarding discontinued antihistamines",
        "debating raccoons at dusk"
    ]

    moral_alignments = [
        "utilitarian realist",
        "chaotic altruist",
        "nihilistic skeptic",
        "radical pacifist",
        "tribalist survivor",
        "hedonistic escapist",
        "stoic moralist"
    ]

    motivations = [
        "to redeem a past mistake",
        "to expose hidden truths",
        "to be left alone",
        "to create something that lasts",
        "to reconnect with a lost friend",
        "to prove a theory correct",
        "to prevent a future collapse"
    ]

    attachment_styles = [
        "securely connected to a found family",
        "anxiously awaiting validation",
        "avoidant of emotional entanglements",
        "disorganized and unpredictable",
        "desperately loyal to one person",
        "ambivalent about connection",
        "uses irony to mask vulnerability"
    ]

    worldviews = [
        "the universe is a glitchy simulation",
        "everything is connected through metaphor",
        "hope is a strategic delusion",
        "entropy always wins",
        "progress is a myth",
        "love is a form of resistance",
        "history loops in spirals"
    ]

    return {
        "role": random.choice(roles),
        "mood": random.choice(moods),
        "crisis": random.choice(crises),
        "moral_alignment": random.choice(moral_alignments),
        "motivation": random.choice(motivations),
        "attachment_style": random.choice(attachment_styles),
        "worldview": random.choice(worldviews)
    }