"""
Dummy data for the UI phase.
Will be replaced by real DB models in Phase 3.
"""

# ---------- Icon library (Lucide-style, 24x24 stroke icons) ----------
ICONS = {
    "notebook":    '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 3v18"/><path d="M11 8h6M11 12h6M11 16h4"/>',
    "magazine":    '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h4"/>',
    "card":        '<rect x="3" y="6" width="18" height="12" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M6 16c.5-1.5 1.8-2 3-2s2.5.5 3 2"/><path d="M15 11h4M15 14h3"/>',
    "sticker":     '<circle cx="12" cy="12" r="9"/><path d="M21 12a9 9 0 0 1-9 9c0-5 4-9 9-9z"/>',
    "nail":        '<rect x="3" y="9" width="18" height="10" rx="3"/><path d="M9 4v5M12 3v6M15 4v5"/>',
    "uni":         '<rect x="3" y="5" width="18" height="14" rx="3"/><circle cx="9" cy="12" r="2.5"/><path d="M14 11h5M14 14h4"/>',
    "playing":     '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M12 7l2.5 3-2.5 3-2.5-3L12 7z"/><path d="M12 15v2"/>',
    "music":       '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
    "camera":      '<rect x="3" y="4" width="18" height="17" rx="2"/><rect x="6" y="7" width="12" height="10"/><path d="M9 17h6"/>',
    "image":       '<rect x="4" y="3" width="16" height="18" rx="2"/><circle cx="9.5" cy="9" r="1.5"/><path d="M4 17l5-5 4 4 3-3 4 4"/>',
    "layers":      '<rect x="3" y="4" width="14" height="17" rx="2"/><rect x="9" y="3" width="12" height="14" rx="2"/><path d="M6 8h5M6 12h5"/>',
    "award":       '<circle cx="12" cy="9" r="6"/><path d="M8 14l-1 7 5-3 5 3-1-7"/>',
}

# ---------- Categories + their products ----------
CATEGORIES = [
    {
        "slug": "notebooks",
        "name": "Notebooks",
        "tagline": "Custom covers, premium paper",
        "icon": ICONS["notebook"],
        "featured": True,
        "products": [
            {"name": "Classic Ruled Notebook",   "price": 300, "unit": "each",   "desc": "A5, 200 pages, matte-laminated cover.",   "badge": "Bestseller"},
            {"name": "Dotted Grid Journal",      "price": 320, "unit": "each",   "desc": "A5, 160 pages, dotted grid, lay-flat spiral."},
            {"name": "Custom Cover Notebook",    "price": 350, "unit": "each",   "desc": "Your artwork printed edge to edge on cover."},
            {"name": "Pocket Notebook",          "price": 180, "unit": "each",   "desc": "A6, 80 pages, saddle-stitched, pack of 3."},
        ],
    },
    {
        "slug": "magazines",
        "name": "Magazines",
        "tagline": "Editorial print, bound to last",
        "icon": ICONS["magazine"],
        "products": [
            {"name": "A4 Full-Color Magazine",   "price": 120, "unit": "per copy", "desc": "32 pages, saddle-stitched, 130 GSM art paper."},
            {"name": "A5 Booklet",               "price": 80,  "unit": "per copy", "desc": "24 pages, folded & stapled, matte finish."},
            {"name": "Premium Cover Magazine",   "price": 180, "unit": "per copy", "desc": "Soft-touch laminated cover, 48 inner pages."},
            {"name": "Bulk Magazine Pack",       "price": 999, "unit": "pack of 10", "desc": "Same title, ten copies, ideal for events.", "badge": "Bulk"},
        ],
    },
    {
        "slug": "business-cards",
        "name": "Business Cards",
        "tagline": "First impressions, printed sharp",
        "icon": ICONS["card"],
        "products": [
            {"name": "Matte Finish Cards",       "price": 399, "unit": "per 100", "desc": "300 GSM, matte lamination, double-sided."},
            {"name": "Glossy Finish Cards",      "price": 449, "unit": "per 100", "desc": "300 GSM, glossy lamination, vivid color."},
            {"name": "Premium Textured Cards",   "price": 699, "unit": "per 100", "desc": "Cotton-textured 400 GSM, letterpress feel."},
            {"name": "Spot UV Cards",            "price": 899, "unit": "per 100", "desc": "Matte base with glossy UV logo highlight.", "badge": "Premium"},
        ],
    },
    {
        "slug": "stickers",
        "name": "Stickers",
        "tagline": "Die-cut, waterproof, every shape",
        "icon": ICONS["sticker"],
        "products": [
            {"name": "Die-Cut Stickers",         "price": 150, "unit": "per 25",  "desc": "Custom shape, any size up to 5cm."},
            {"name": "Vinyl Waterproof Stickers","price": 250, "unit": "per 25",  "desc": "Weatherproof, dishwasher-safe vinyl."},
            {"name": "Sheet Stickers",           "price": 99,  "unit": "per 10",  "desc": "A6 sheet, multiple designs per sheet."},
            {"name": "Holographic Stickers",     "price": 349, "unit": "per 20",  "desc": "Rainbow holographic finish, eye-catching.", "badge": "New"},
        ],
    },
    {
        "slug": "nail-press-on-cards",
        "name": "Nail Press-On Cards",
        "tagline": "Showcase your nail art beautifully",
        "icon": ICONS["nail"],
        "products": [
            {"name": "Classic Nail Card",        "price": 199, "unit": "per 20",  "desc": "Standard display card with 10 nail slots."},
            {"name": "Premium Nail Card",        "price": 349, "unit": "per 20",  "desc": "Gloss-laminated, custom branding strip."},
            {"name": "Custom Brand Nail Card",   "price": 499, "unit": "per 50",  "desc": "Fully custom layout, logo + handle on card.", "badge": "Bulk"},
        ],
    },
    {
        "slug": "uni-cards",
        "name": "Uni Cards",
        "tagline": "Student IDs, club cards, campus merch",
        "icon": ICONS["uni"],
        "products": [
            {"name": "Student ID Card",          "price": 249, "unit": "per 25",  "desc": "PVC-card finish, lanyard-ready punch hole."},
            {"name": "College ID Bundle",        "price": 599, "unit": "per 50",  "desc": "Mixed name batches, single order pricing.", "badge": "Bulk"},
            {"name": "Custom Uni Card",          "price": 399, "unit": "per 25",  "desc": "Design your own layout, double-sided print."},
        ],
    },
    {
        "slug": "playing-cards",
        "name": "Playing Cards",
        "tagline": "Custom decks, casino-grade stock",
        "icon": ICONS["playing"],
        "products": [
            {"name": "Classic Deck",             "price": 299, "unit": "per deck", "desc": "52 cards + 2 jokers, standard poker size."},
            {"name": "Custom Face Deck",         "price": 499, "unit": "per deck", "desc": "Your art on every face card and back."},
            {"name": "Premium Matte Deck",       "price": 699, "unit": "per deck", "desc": "Air-cushion finish, 310 GSM black core.", "badge": "Premium"},
            {"name": "Bulk Deck (Pack of 5)",    "price": 1299,"unit": "pack of 5","desc": "Five identical custom decks, event-ready."},
        ],
    },
    {
        "slug": "spotify-books",
        "name": "Spotify Books",
        "tagline": "Your playlist, printed as art",
        "icon": ICONS["music"],
        "products": [
            {"name": "Spotify Book A5",          "price": 349, "unit": "each",   "desc": "Your playlist cover + track list, spiral bound."},
            {"name": "Spotify Book A4",          "price": 499, "unit": "each",   "desc": "Bigger format, hard cover, premium pages.", "badge": "Bestseller"},
            {"name": "Custom Spotify Book",      "price": 599, "unit": "each",   "desc": "Fully bespoke layout, gift-wrapped."},
        ],
    },
    {
        "slug": "polaroids",
        "name": "Polaroids",
        "tagline": "Retro prints, sharp and glossy",
        "icon": ICONS["camera"],
        "products": [
            {"name": "Mini Polaroid Pack",       "price": 199, "unit": "per 10",  "desc": "2.5 x 3 inch classic format, glossy print."},
            {"name": "Custom Polaroid",          "price": 299, "unit": "per 10",  "desc": "Your photos with custom caption strip."},
            {"name": "Premium Polaroid Frame",   "price": 449, "unit": "per 8",   "desc": "Cardstock-thick frame with matte finish."},
        ],
    },
    {
        "slug": "posters",
        "name": "Posters",
        "tagline": "Wall art, printed large and sharp",
        "icon": ICONS["image"],
        "products": [
            {"name": "A3 Poster",                "price": 99,  "unit": "each",   "desc": "300 DPI print on 200 GSM poster paper."},
            {"name": "A2 Poster",                "price": 149, "unit": "each",   "desc": "Larger format, same premium finish."},
            {"name": "Custom Movie Poster",      "price": 199, "unit": "each",   "desc": "Your design, movie-poster quality print."},
            {"name": "Bulk Poster Pack",         "price": 499, "unit": "pack of 5", "desc": "Any five posters, single price.", "badge": "Bulk"},
        ],
    },
    {
        "slug": "mini-scrapbooks",
        "name": "Mini Scrapbooks",
        "tagline": "Handmade memories, bound tight",
        "icon": ICONS["layers"],
        "products": [
            {"name": "Mini Scrapbook A6",        "price": 249, "unit": "each",   "desc": "20 pages, textured kraft cover."},
            {"name": "Custom Scrapbook",         "price": 399, "unit": "each",   "desc": "Your theme, colours, and cover design."},
            {"name": "Photo Scrapbook",          "price": 349, "unit": "each",   "desc": "Your printed photos placed and glued."},
        ],
    },
    {
        "slug": "certificates",
        "name": "Certificates",
        "tagline": "Recognition, printed to impress",
        "icon": ICONS["award"],
        "products": [
            {"name": "Standard Certificate",     "price": 49,  "unit": "per copy", "desc": "A4, 200 GSM, sharp black-and-color print."},
            {"name": "Foil Certificate",         "price": 99,  "unit": "per copy", "desc": "Gold or silver foil accents on 300 GSM."},
            {"name": "Frame Certificate",        "price": 199, "unit": "per copy", "desc": "Foil print + ready-to-hang A4 frame."},
            {"name": "Bulk Certificate Pack",    "price": 399, "unit": "pack of 10", "desc": "Ten identical certificates, single batch.", "badge": "Bulk"},
        ],
    },
]


def get_category(slug):
    for c in CATEGORIES:
        if c["slug"] == slug:
            return c
    return None