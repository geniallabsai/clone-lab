# Changelog

## 1.1.0 (2026-09-23)
- **Camada de naturalismo** (`protocols/naturalismo.md`): regra 95/5, sinais
  de olhar-IA, anatomia de pele obrigatória, imperfeição única por quadro
  escolhida da lista `realismo` de cada cenário.
- **Luminosidade com números**: novo campo `luminosidade` no catálogo
  (exposição EV, Kelvin dominante, razão key:fill, proteção de destaque e
  piso de sombra) em 16/16 cenários; novo bloco no prompt; agente 03
  reescrito com os 4 números obrigatórios.
- **Objetos perfeitos**: novo campo `objetos` (anatomia crítica) em 16/16
  cenários; bloco OBJETOS-CRÍTICOS no prompt; regra do 02: objeto trocado em
  variação precisa anatomia igual.
- **Negativos: 1 base virou 4 imutáveis** (pessoas / objetos / luz /
  naturalismo) em `negativos.json`.
- **QC de 12 → 16 itens**: +13 objetos críticos, +14 física, +15
  luminosidade, +16 naturalismo. `clone.py qc` valida 16 keywords (imunes a
  acento), âncoras duplas no negativo ("6 fingers" + "melted") e os blocos
  novos do prompt.
- Retrabalho: itens 13–16 só podem melhora (senão a tentativa anterior vale
  mais) — decisão registrada.


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
