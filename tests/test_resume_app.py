"""Unit tests for the helper functions and resume data in resume_app.py."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import resume_app  # noqa: E402


DATA = resume_app.default_resume()


def test_clean_name_strips_unsafe_characters():
    assert resume_app.clean_name("  <b>Anna</b> & co!  ") == "bAnnab  co"


def test_clean_name_is_limited_to_30_characters():
    assert len(resume_app.clean_name("a" * 100)) == 30


def test_email_link_adds_reader_name_to_subject():
    link = resume_app.email_link(DATA["profile"], "Anna Tan")
    assert link.startswith("mailto:" + DATA["profile"]["email"])
    assert link.endswith("subject=Business%20Analytics%20Enquiry%20from%20Anna%20Tan")


def test_esc_escapes_html():
    assert resume_app.esc("R&D <team>") == "R&amp;D &lt;team>"


def test_badges_highlight_selected_items():
    assert resume_app.badges(["SQL", "Excel"], ["SQL"], "blue") == ":orange-badge[SQL] :blue-badge[Excel]"


def test_split_by_filter():
    entries = [{"name": "A", "tags": ["SQL"]}, {"name": "B", "tags": ["Excel"]}]
    matching, others = resume_app.split_by_filter(entries, ["SQL"])
    assert [e["name"] for e in matching] == ["A"]
    assert [e["name"] for e in others] == ["B"]
    assert resume_app.split_by_filter(entries, []) == (entries, [])


def test_text_resume_has_every_section_and_no_markdown():
    text = resume_app.build_text_resume(DATA)
    for heading in ("EXPERIENCE", "PROJECTS", "SKILLS", "EDUCATION"):
        assert heading in text
    assert "**" not in text
    for job in DATA["experience"]:
        assert job["name"] in text


def test_resume_data_is_complete():
    assert len(DATA["sections"]) == resume_app.SECTION_TOTAL
    for entry in DATA["experience"] + DATA["projects"]:
        assert entry["name"] and entry["period"] and entry["bullets"]


def test_highlighted_skills_exist_in_toolkit():
    toolkit = resume_app.collect_toolkit(DATA)
    assert set(DATA["highlight_skills"]) <= toolkit


def test_profile_photo_exists():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assert os.path.exists(os.path.join(root, DATA["profile"]["photo"]))
