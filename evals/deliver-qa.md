# Eval: entrega dourada (qualquer agente, de ponta a ponta)

Objetivo: provar que o esquadro completo roda sem supervisão e que NENHUMA
entrega escapa do QC nem da faixa 0–15.

## Cenário
1. `python3 clone.py init ~/dataset-teste` (com 5+ fotos reais ou PNGs válidos).
2. Injetar `BOOT.md` no agente; definir `CLONE_HOME` e `CLONE_PKG`.
3. Pedir: "clona meu rosto num podcast" e depois "me dá algo" (sem cenário).

## Passa se (TODOS)
- [ ] `mapeamento-facial.md` e `identidade.txt` criados/atualizados (≤200 palavras).
- [ ] `clone.py cenario --tipo podcast` devolveu **1**; o "me dá algo" devolveu
      um inteiro 0–15 diferente dos últimos 3 usados (verificar em
      `state/`/`CLONE-CONFIG.json`).
- [ ] `clone.py prompt` montou `drafts/<job>/` com 4 arquivos; prompt.md tem os
      9 blocos na ordem: IDENTIDADE primeiro (igual a identidade.txt), CENÁRIO,
      LUZ, **LUMINOSIDADE com 4 números (EV, K, razão, proteção)**,
      **OBJETOS-CRÍTICOS com anatomia**, AÇÃO, FORMATO, **NATURALISMO com uma
      imperfeição da lista do cenário**, VARIAÇÕES.
- [ ] negativo.md contém as 4 bases: "6 fingers" (pessoas), "melted objects"
      (objetos), seção luz e seção naturalismo + extras do cenário sorteado.
- [ ] copy.md tem HOOK + LEGENDA + CTA (1 ação) + 5–10 hashtags + formato.
- [ ] qc.md tem os **16** itens preenchidos (dedos contados em número; objetos
      conferidos parte a parte; exposição/temperatura checar contra os números
      declarados; naturalismo vs. lista do cenário) + veredito LIBERADO ou
      RETRABALHO com ajuste específico.
- [ ] `python3 clone.py qc <job>` exit 0.
- [ ] Job movido para `saida/` com `registrar.md` (cenário N, luz+luminosidade,
      QC, correções).
- [ ] Nenhuma foto original do dataset foi alterada (checksum antes/depois).

## Reprova se (QUALQUER)
- Número de cenário fora de 0–15 ou "escolhido" sem passar pelo código.
- Entrega sem qc.md ou com item de dedos sem número contado.
- Prompt sem LUMINOSIDADE numérica ou sem OBJETOS-CRÍTICOS com anatomia.
- Imagem "perfeitamente limpa" (zero imperfeição da lista) liberada no item 16.
- Duas temperaturas em cena sem prático visível declarado.
- Rosto/pele/cabelo descritos fora do bloco IDENTIDADE (drift de identidade).
- Retrabalho automático > 2, ou item 13–16 piorou no retrabalho sem registro.
- Foto original editada/renomeada.
