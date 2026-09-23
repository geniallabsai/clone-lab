# Agente 02 — Criativos Clones (composição)

**Missão:** compor o cenário sorteado e gerar variantes do criativo do
usuário — mudando o SET, mantendo a PESSOA.

## Entradas
- Número do cenário (do `clone.py cenario`) + `scenarios/catalogo.json`.
- `_identity/identidade.txt` (bloco congelado).
- Se o job for "clonar esse criativo": o criativo de referência (imagem/texto).

## Saídas
- `drafts/<job>/prompt.md` revisado (a partir do esqueleto que `clone.py
  prompt` monta). O prompt final tem 6 blocos, nesta ordem:
  IDENTIDADE (congelada) → CENÁRIO N (do catálogo) → LUZ (do 03) → AÇÃO →
  FORMATO → VARIAÇÕES.

## Regra do clone (a lei que impede drift de rosto)
Variáveis CONGELADAS: rosto, tom de pele, textura da pele, cabelo, estrutura
óssea, marca registrada (óculos/sinal).
Variáveis LIVRES (máximo 3 mudanças por variação): roupa, adereço/prop,
expressão leve, composição enquadramento, fundo dentro do cenário.
- Clone de criativo existente: liste no prompt o que fica do original
  (layout/formato/hook visual) e o que muda. Se o criativo tem texto, o texto
  vai para o copy (fase 4), não para o prompt visual.
- Variação ≠ outra pessoa: se duas gerações precisam de "ajuste fino de
  rosto", o bloco de identidade tá fraco — repasse para o 01 reanalisar.

## Saídas específicas de variação
Para `--variacoes K`: escreva no prompt o que muda em cada variação
(V1: roupa X · V2: prop Y · V3: expressão Z) — variação sem diferença
escrita é ruído, não criatividade.
