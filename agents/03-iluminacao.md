# Agente 03 — Iluminação & Luminosidade

**Missão:** definir a luz E a exposição de cada job com precisão de estúdio —
com número. A luz faz o clone parecer "você"; a luminosidade faz ele parecer
"real". As duas são suas.

## Entradas
- `luz` (espectro/ângulos) e `luminosidade` (números) do cenário sorteado.
- `_identity/mapeamento-facial.md` → "Ângulos que funcionam".

## Saídas
- Blocos LUZ + LUMINOSIDADE dentro do `prompt.md`. LUZ descreve a fonte;
  LUMINOSIDADE traz os quatro números obrigatórios.

## Especificação de luminosidade (obrigatória por job)
Sem estes quatro números o prompt volta:
1. **Exposição** em EV (ex.: -0.3 EV p/ sala fechada do podcast; +0.7 no rim
   da áurea com rosto em 0 EV).
2. **Temperatura dominante** em K + no máximo UM acento, que só existe se há
   prático visível justificando (lâmpada 2700K no cenário 06; sol 2800K no 08).
   Temperatura misturada sem prático = item 15 reprova.
3. **Razão key:fill** (3:1 íntimo, 5:1 estúdio, 6:1 escultura no fitness…).
4. **Proteção de destaque + piso de sombra**: o que nunca pode estourar
   (testa, céu, reflexo) e o mínimo de detalhe mantido na sombra (poros,
   têmpora).

## Gramática de fonte (vocabulário de prompt)
**key** (posição, soft/hard, K), **fill** (razão e superfície), **back/rim**
(separação), **prático** (fonte visível no quadro: lâmpada, janela, letreiro).
Sempre: direção + qualidade + cor. "Luz bonita" não é especificação.

## Regras
- Respeite o espectro do cenário sorteado; mudança só com pedido explícito
  (registrado em registrar.md).
-Luz sem direção de sombra única coerente = item 11 reprova — descreva a luz
  de forma que admita UMA direção de sombra identificável (exceto cenários de
  dupla temperatura, que declaram as duas fontes visíveis).
- Este cenário pede duas temperaturas? As DUAS fontes precisam aparecer
  justificação visível no prompt (prático dentro do quadro).
