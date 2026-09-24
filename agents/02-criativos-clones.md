# Agente 02 — Criativos Clones (composição)

**Missão:** compor o cenário sorteado e gerar variantes do criativo do
usuário — mudando o SET, mantendo a PESSOA (e os objetos geometricamente inteiros).

## Entradas
- Número do cenário (do `clone.py cenario`) + `scenarios/catalogo.json`.
- `_identity/identidade.txt` (bloco congelado).
- Se o job for "clonar esse criativo": o criativo de referência (imagem/texto).

## Saídas
- `drafts/<job>/prompt.md` revisado sobre o esqueleto que `clone.py prompt`
  monta. Blocos obrigatórios na ordem: IDENTIDADE → CENÁRIO N → LUZ →
  LUMINOSIDADE → OBJETOS-CRÍTICOS → AÇÃO → FORMATO → NATURALISMO → VARIAÇÕES.

## Regra do clone (a lei que impede drift de rosto)
Variáveis CONGELADAS: rosto, tom de pele, textura da pele, cabelo, estrutura
óssea, marca registrada (óculos/sinal).
Variáveis LIVRES (máximo 3 mudanças por variação): roupa, adereço/prop,
expressão leve, composição/enquadramento, fundo dentro do cenário.
- Clone de criativo existente: liste no prompt o que fica do original
  (layout/formato/hook visual) e o que muda. Texto do criativo vai para o
  copy (fase 4), não para o prompt visual.
- Variação ≠ outra pessoa: se duas gerações precisam de "ajuste fino de
  rosto", o bloco de identidade tá fraco — repasse para o 01 reanalisar.

## Regra dos objetos-críticos (novo em v1.1)
Todo objeto listado em OBJETOS-CRÍTICOS do catálogo precisa de ANATOMIA no
prompt final: cada parte citada (alça, grade, zíper, trama do tecido, logo)
escrita explicitamente. Trocou objeto em uma variação? O substituto recebe
anatomia igual antes de gerar — objeto novo sem descrição = derretido provável
(item 13 do QC).

## Naturalismo no set (v1.1)
O 02 escolhe QUAL imperfeição da lista `realismo` do cenário entra no quadro
(exatamente uma) e a descreve no bloco NATURALISMO do prompt. Improviso fora
da lista do cenário = reprovável no item 16.

## Saídas específicas de variação
Para `--variacoes K`: escreva no prompt o que muda em cada variação
(V1: roupa X · V2: prop Y · V3: expressão Z) — variação sem diferença
escrita é ruído, não criatividade.
