"""Exporta o fragmento Civu usando o invólucro standalone preservado."""
from pathlib import Path
from html import escape
root=Path(__file__).resolve().parents[1]
fragment=(root/'src/civu.html').read_text(encoding='utf-8')
shell=(root/'scripts/index-shell.html').read_text(encoding='utf-8')
assert shell.count('<!--CIVU_FRAGMENT-->')==1
(root/'index.html').write_text(shell.replace('<!--CIVU_FRAGMENT-->',escape(fragment,quote=True)),encoding='utf-8')
print('index.html atualizado')
