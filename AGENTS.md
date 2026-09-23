# AGENTS.md

Este workspace segue o protocolo **CloneLab** (clonagem criativa da imagem do
usuário com squad de 5 agentes e cenários numerados 0–15).

- Entrada da skill: `SKILL.md` (6 fases + 7 leis)
- Bloco autossuficiente para prompt: `BOOT.md`
- Catálogo de cenários: `scenarios/CATALOGO-0-15.md` + `catalogo.json`
- Bibliotecas de negativos: `scenarios/negativos.json` + `NEGATIVOS.md`
- Código: `clone.py` (init / cenario / prompt / qc / check)

Em todo trabalho: rode as 6 fases de `SKILL.md` sem pular a fase de QC.
O número de cenário vem de `clone.py cenario` — sempre inteiro 0–15.
