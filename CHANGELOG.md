# Changelog

## 1.0.0 (2026-09-23)
- Pacote inicial: SKILL de orquestração em 6 fases + 7 leis.
- 5 agentes: analista de imagens, criativos clones, iluminação, copy & social,
  negativo/QC (gate obrigatório).
- Catálogo de 16 cenários numerados 0–15 (`scenarios/catalogo.json` +
  `CATALOGO-0-15.md`) com luz, câmera, proporção, bloco de prompt, negativos
  específicos e template de hook por cenário.
- `clone.py` (Python stdlib): `init`, `cenario` (numeração garantida 0–15 com
  anti-repetição dos últimos 3), `prompt` (monta prompt+negativo+copy+qc),
  `qc` (validação estrutural de 12 itens), `check` (self-teste de 100 sorteios).
- Bibliotecas de negativos: base universal (6 dedos, membros extras, rosto
  assimétrico, texto torto, pele plástica…) + extras por cenário.
- Contrato de identidade: `_identity/mapeamento-facial.md` + `identidade.txt`
  (variáveis congeladas: rosto, pele, cabelo, silhueta).
- Templates: prompt, copy, negativo, qc (12 itens), registrar.
- Eval: `evals/deliver-qa.md` (entrega dourada de ponta a ponta).
