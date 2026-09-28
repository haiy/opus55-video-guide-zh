#!/usr/bin/env python3
"""Validate this repository's navigation data without contacting third parties."""
from pathlib import Path
import json
import re
from urllib.parse import unquote,urlsplit

ROOT=Path(__file__).resolve().parents[1]
summary=json.loads((ROOT/'data/index-summary.json').read_text())
repos=json.loads((ROOT/'data/github-resources.json').read_text())['repositories']
cases=json.loads((ROOT/'data/x-cases.json').read_text())['cases']
assert len(repos)==summary['github_repositories']
assert len(cases)==summary['x_posts']
assert len({r['full_name'].lower() for r in repos})==len(repos)
assert len({c['id'] for c in cases})==len(cases)
assert sum(summary['x_categories'].values())==len(cases)
for r in repos:
    assert isinstance(r['stargazers_count'],int) and r['stargazers_count']>=0
    assert r['html_url'].startswith('https://github.com/')
for c in cases:
    assert re.fullmatch(r'https://x\.com/[\w]+/status/\d+',c['url']),c['url']
    assert c['source_refs']
    assert c['category'] in summary['x_categories']
checked=0
for p in ROOT.rglob('*.md'):
    s=p.read_text()
    assert '/Users/' not in s and '/var/folders/' not in s,p
    links=re.findall(r'\]\(([^\s)]+)\)',s)+re.findall(r'<img[^>]+src="([^"]+)"',s)
    for link in links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        target=p if not u.path else (p.parent/unquote(u.path)).resolve()
        assert target.is_relative_to(ROOT),link
        assert target.exists(),f'{p}: missing {link}'
        if u.fragment and target.suffix=='.md':
            body=target.read_text();fragment=unquote(u.fragment)
            anchors=set(re.findall(r'<a\s+id="([^"]+)"',body))
            for h in re.findall(r'^#{1,6}\s+(.+)$',body,re.M):
                h=re.sub(r'[^\w\-\s]','',h.lower()).replace(' ','-')
                anchors.add(h)
            assert fragment in anchors,f'{p}: missing anchor {link}'
        checked+=1
print(f"OK: {len(repos)} GitHub projects; {len(cases)} X posts; {checked} internal links.")
