"""Rebuild the static page and BibTeX after editing data/publications.json."""
from pathlib import Path
import json,html,re
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'data/publications.json').read_text())
esc=lambda x:html.escape(str(x),quote=True)
def bib(r):
 typ={'Journal article':'article','Conference paper':'inproceedings','Thesis':'phdthesis'}.get(r['type'],'misc')
 key=re.sub('[^A-Za-z0-9]','',r['id'])
 fields={'title':r['title'],'author':' and '.join(r['authors']),'year':str(r['year']),'url':r['links'].get('DOI') or r['links'].get('DBLP') or r['links']['PubMed']}
 if r.get('doi'):fields['doi']=r['doi']
 fields['note']=r['venue']
 def safe(s):return s.replace('\\','\\textbackslash{}').replace('&','\\&').replace('%','\\%').replace('_','\\_').replace('#','\\#').replace('$','\\$')
 return '@'+typ+'{'+key+',\n'+',\n'.join('  '+k+' = {'+safe(v)+'}' for k,v in fields.items())+'\n}'
blocks=[]
for r in rows:
 link=r['links'].get('DOI') or r['links'].get('DBLP') or r['links']['PubMed']
 authors=', '.join('<strong>'+esc(x)+'</strong>' if x=='Grigorios Loukides' else esc(x) for x in r['authors'])
 links=''.join('<a href="'+esc(v)+'">'+esc(k)+' ↗</a>' for k,v in r['links'].items())
 blocks.append(f'''<article class="pub" data-year="{r['year']}" data-type="{esc(r['type'])}" data-sources="{esc('|'.join(r['sources']))}"><div class="pub-year">{r['year']}</div><div><h3><a href="{esc(link)}">{esc(r['title'])}</a></h3><p class="authors">{authors}</p><p class="venue">{esc(r['venue'])}</p><div class="pub-foot"><span class="type">{esc(r['type'])}</span>{links}</div><details><summary>BibTeX</summary><pre>{esc(bib(r))}</pre></details></div></article>''')
page=(ROOT/'template.html').read_text()
replacements={'@@COUNT@@':str(len(rows)),'@@YEARS@@':''.join(f'<option>{y}</option>' for y in sorted({r['year'] for r in rows},reverse=True)),'@@TYPES@@':''.join('<option>'+esc(t)+'</option>' for t in sorted({r['type'] for r in rows})),'@@PUBLICATIONS@@':'\n'.join(blocks),'@@PORTRAIT@@':(ROOT/'data/portrait-uri.txt').read_text().strip()}
for key,value in replacements.items():page=page.replace(key,value)
assert not re.search('@@[A-Z]+@@',page)
(ROOT/'index.html').write_text(page)
(ROOT/'publications.bib').write_text('\n\n'.join(bib(r) for r in rows)+'\n')
print(f'Built {len(rows)} records; {len(page)} HTML characters.')
