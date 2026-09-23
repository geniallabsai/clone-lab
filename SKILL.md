---
name: clone-lab
version: 1.0.0
description: >
  Esquadrão de agentes para clonagem criativa da imagem do usuário:
  analisa o dataset, mapeia identidade, compõe 16 cenários numerados (0–15),
  ilumina, escreve copy social e aplica QC negativo (vetos a distorções).
entrypoint: BOOT.md
requires: python3 (para clone.py; geração de imagem via ferramenta/API do agente)
---

# CloneLab — Skill principal (orquestração)

## Quando acionar
Pedido envolvendo: clonar/gerar a imagem do usuário, criar criativo com o
rosto dele, cenários (POV, podcast, normal…), variações de um criativo,
copy/legenda para imagem sua, ou qualquer "me põe nesse cenário".

## As 6 fases (ordem fixa, sem pular)

### 0. CONTRATO
Confirmar: (a) caminho do dataset (perguntar se nunca foi dado; gravar em
`CLONE-CONFIG.json`); (b) cenário pedido ou "à escolha do código"; (c) formato
de saída (proporção vem do cenário, mas respeitar pedido explícito do usuário).

### 1. IDENTIFICAR — agente `01-analista-imagens`
- Ler as fotos do dataset; ATUALIZAR `_identity/mapeamento-facial.md`
  (seções fixas) e REESCREVER `_identity/identidade.txt` (bloco pronto para
  prompt, ≤200 palavras, linguagem de prompt).
- Regra: identidade.txt é a ÚNICA fonte do bloco de rosto/corpo em prompts.
- Se dataset mudou desde a última vez (arquivos novos), reanalisar o mínimo
  necessário e atualizar o mapeamento com campo `atualizado_em`.

### 2. ESCOLHER CENÁRIO — código (não chute!)
```bash
python3 $CLONE_PKG/clone.py cenario [--tipo POV|PODCAST|NORMAL|...] [--seed N]
```
- O comando devolve SEMPRE um inteiro 0–15 (garantido por assert) e grava no
  histórico. Cenário sem pedido = o código escolhe (evita os 3 últimos).
- O número escolhido define TUDO do bloco de cenário: `scenarios/catalogo.json`.

### 3. COMPOR — agentes `02-criativos-clones` + `03-iluminacao`
- Rodar `python3 $CLONE_PKG/clone.py prompt --nro N --acao "…" [--variacoes K]`
  → cria `drafts/<job>/` com `prompt.md` + `negativo.md` + esqueletos
  `copy.md`/`qc.md`.
- O agente 02 revisa o `prompt.md`: ação do conteúdo, variação de criativo
  (se for clonar um criativo existente: lista variáveis congeladas + máximo
  3 mudanças de set/roupa/adereço — NUNCA rosto/pele/cabelo).
- O agente 03 confirma o bloco LUZ (pode ajustar temperatura/ângulo por
  ocasião, mas o tipo de luz vem do catálogo do número sorteado).

### 4. COPY — agente `04-copy-social`
Preencher `drafts/<job>/copy.md`: HOOK (3 s, fala ou texto na tela), LEGENDA,
CTA, HASHTAGS (5–10, misto de alcance+nicho), FORMATO (proporção + plataforma
ideal do cenário). Linguagem = a do usuário.

### 5. NEGATIVO/QC — agente `05-negativo-qc` (GATE — não é opcional)
- Garantir que `negativo.md` contém a biblioteca base (inclui "6 fingers") +
  extras do cenário (já montado pelo código; o agente pode adicionar
  termos específicos do job, nunca remover da base).
- Gerar a imagem. Executar os 12 itens do checklist do `qc.md` UM A UM
  (contar dedos literalmente; conferir rosto contra `_identity/mapeamento-facial.md`).
- Veredito: **LIBERADO** (todos os 12 ok) ou **RETRABALHO** (lista itens
  reproados + ajuste específico no prompt). RETRABALHO volta para a fase 3
  com no MÁXIMO 2 repetições; após isso, escala para o humano com o relatório.

### 6. ENTREGAR
- Mover o job completo para `saida/<AAAA-MM-DD>--<hhmm>--<agente>--<nro>-<slug>/`.
- Escrever `registrar.md` (10 linhas: cenário N, decisão de luz, veredito QC,
  o que reprovou e como foi corrigido).
- Opcional (SecondMind configurado): nota de sessão no vault com links p/
  decisão de cenário e aprendizados (reaproveitamento entre sessões).

## Leis (invioláveis)
1. Sem QC (fase 5) não existe entrega. O agente negativo é gate, não sugestão.
2. O número de cenário SEMPRE está em 0–15; vem do código, nunca da memória.
3. Identidade vive em `_identity/identidade.txt`; prompt nunca "improvisa" rosto.
4. Clone muda SET, LUZ e AÇÃO — nunca rosto, tom de pele ou cabelo.
5. Dataset é somente leitura: nunca editar/renomear/mover fotos originais.
6. Máximo de 2 retrabalhos automáticos; depois, humano decide.
7. Cinco dedos por mão, pares de membros completos — verificação item a item,
   nunca "parece certo".

## Estrutura do workspace (contrato)
```
<dataset>/
├── (suas fotos — somente leitura)
├── CLONE-CONFIG.json     # dataset, histórico de cenários
├── _identity/
│   ├── mapeamento-facial.md   # análise detalhada (humano pode auditar)
│   └── identidade.txt         # BLOCO CONGELADO p/ prompt (≤200 palavras)
├── drafts/<job>/          # prompt.md, negativo.md, copy.md, qc.md (+imagem)
├── saida/<job-final>/     # entregas aprovadas + registrar.md
└── state/                 # logs de cenário (jsonl)
```
