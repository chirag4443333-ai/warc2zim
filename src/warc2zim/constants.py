from zimscraperlib.logging import getLogger

# Shared logger with default log level at this stage
logger = getLogger("warc2zim")

# MIME types handled by the HTML rewriter
HTML_TYPES = ("text/html", "application/xhtml", "application/xhtml+xml")

# Unambiguous binary MIME types that can safely override bad server headers
ALLOWED_OVERRIDE_MIMES = {
    "application/pdf",
    "image/png",
    "image/jpeg",
    "image/gif",
    "image/webp",
}

# Default values of mandatory ZIM metadata, also used as fallback when a value is
# missing or blank, so that a ZIM is always created (see #427)
DEFAULT_TITLE = "Untitled"
DEFAULT_DESCRIPTION = "-"
DEFAULT_CREATOR = "-"
DEFAULT_PUBLISHER = "openZIM"
