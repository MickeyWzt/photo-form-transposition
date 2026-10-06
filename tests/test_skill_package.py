import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "photo-form-transposition"
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class SkillPackageTests(unittest.TestCase):
    def test_required_package_files_exist(self):
        required = [
            PACKAGE / "SKILL.md",
            PACKAGE / "agents" / "openai.yaml",
            PACKAGE / "evals" / "evals.json",
            PACKAGE / "references" / "prompt-compiler.md",
            PACKAGE / "references" / "quality-gate.md",
            PACKAGE / "references" / "visual-system.md",
        ]

        missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
        self.assertEqual(missing, [], f"Missing required package files: {missing}")

    def test_skill_frontmatter_identifies_package(self):
        content = (PACKAGE / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = content.split("---", 2)

        self.assertGreaterEqual(len(frontmatter), 3, "SKILL.md needs YAML frontmatter")
        self.assertRegex(frontmatter[1], r"(?m)^name:\s*photo-form-transposition\s*$")
        self.assertRegex(frontmatter[1], r"(?m)^description:\s*\S.+$")

    def test_evals_have_stable_required_fields(self):
        data = json.loads((PACKAGE / "evals" / "evals.json").read_text(encoding="utf-8"))
        self.assertEqual(data.get("skill_name"), "photo-form-transposition")

        evals = data.get("evals")
        self.assertIsInstance(evals, list)
        self.assertGreater(len(evals), 0)
        ids = [case.get("id") for case in evals]
        self.assertEqual(len(ids), len(set(ids)), "Eval IDs must be unique")

        for case in evals:
            with self.subTest(eval_id=case.get("id")):
                for field in ("id", "prompt", "expected_output", "files", "expectations"):
                    self.assertIn(field, case)
                self.assertIsInstance(case["files"], list)
                self.assertGreater(len(case["files"]), 0)
                self.assertIsInstance(case["expectations"], list)
                self.assertGreater(len(case["expectations"]), 0)

    def test_relative_markdown_links_resolve(self):
        broken = []

        for markdown in ROOT.rglob("*.md"):
            if ".git" in markdown.parts:
                continue
            content = markdown.read_text(encoding="utf-8")
            for match in LINK_PATTERN.finditer(content):
                target = match.group(1).strip().strip("<>")
                target = target.split(maxsplit=1)[0]
                parsed = urlparse(target)
                if parsed.scheme or target.startswith("#"):
                    continue
                path_text = unquote(parsed.path)
                if not path_text:
                    continue
                resolved = markdown.parent / path_text
                if not resolved.exists():
                    broken.append(f"{markdown.relative_to(ROOT)} -> {target}")

        self.assertEqual(broken, [], f"Broken relative Markdown links: {broken}")


if __name__ == "__main__":
    unittest.main()
