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
      6 blocos na ordem (IDENTIDADE primeiro e igual a identidade.txt).
- [ ] negativo.md contém "6 fingers" e os extras do cenário sorteado.
- [ ] copy.md tem HOOK + LEGENDA + CTA (1 ação) + 5–10 hashtags + formato.
- [ ] qc.md tem os 12 itens preenchidos (dedos contados em números, não "ok")
      + veredito LIBERADO ou RETRABALHO com ajuste específico.
- [ ] `python3 clone.py qc <job>` exit 0.
- [ ] Job movido para `saida/` com `registrar.md` (cenário N, luz, QC, correções).
- [ ] Nenhuma foto original do dataset foi alterada (checksum antes/depois).

## Reprova se (QUALQUER)
- Número de cenário fora de 0–15 ou "escolhido" sem passar pelo código.
- Entrega sem qc.md ou com item de dedos sem número contado.
- Rosto/pele/cabelo descritos fora do bloco IDENTIDADE (drift de identidade).
- Retrabalho automático > 2.
- Foto original editada/renomeada.
