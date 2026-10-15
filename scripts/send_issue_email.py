"""Email the newest Puppy Chow issue from the personal Gmail account.

Called by .github/workflows/email-issue.yml after a push adds docs/YYYY-MM/index.html.
Env: ISSUE_DIR (e.g. docs/2026-11), PAGES_URL, GMAIL_USER, GMAIL_APP_PASSWORD, MAIL_TO (comma-separated).
Recipients live in a repo secret because the repo is public.
"""
import html
import os
import re
import smtplib
import sys
from email.message import EmailMessage


def text(fragment: str) -> str:
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", fragment))).strip()


def main() -> None:
    issue_dir = os.environ["ISSUE_DIR"].rstrip("/")
    page = open(f"{issue_dir}/index.html", encoding="utf-8").read()

    title = text(re.search(r"<title>(.*?)</title>", page, re.S).group(1))
    mast = re.search(r'<div class="mast">(.*?)</div>', page, re.S).group(1)
    window = text(re.sub(r"</span>", " · ", mast)).rstrip(" ·")
    tldr = re.search(r'<section class="tldr".*?</section>', page, re.S)
    bullets = []
    if tldr:
        for li in re.findall(r"<li>(.*?)</li>", tldr.group(0), re.S):
            # Drop the trailing source links; the issue page has them.
            bullets.append(text(re.sub(r"<a [^>]*>.*?</a>", "", li)).rstrip(" ·"))

    url = os.environ["PAGES_URL"].rstrip("/") + "/" + issue_dir.split("/", 1)[1] + "/"
    body = [f"{title} is out.", "", url, "", "This month's top three:"]
    body += [f"  {i}. {b}" for i, b in enumerate(bullets, 1)]
    body += ["", f"Window: {window}", "Past issues: " + os.environ["PAGES_URL"]]

    msg = EmailMessage()
    msg["Subject"] = title
    msg["From"] = f"Puppy Chow <{os.environ['GMAIL_USER']}>"
    recipients = [a.strip() for a in os.environ["MAIL_TO"].split(",") if a.strip()]
    msg["To"] = ", ".join(recipients)
    msg.set_content("\n".join(body))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.environ["GMAIL_USER"], os.environ["GMAIL_APP_PASSWORD"])
        smtp.send_message(msg)
    print(f"Sent '{title}' to {len(recipients)} recipient(s): {url}")


if __name__ == "__main__":
    sys.exit(main())
