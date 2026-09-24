---
name: clone-lab
version: 1.1.0
description: >
  Esquadrão de agentes para clonagem criativa da imagem do usuário:
  analisa o dataset, mapeia identidade, compõe 16 cenários numerados (0–15)
  com naturalismo, luminosidade medida e objetos perfeitos; ilumina, escreve
  copy social e aplica QC negativo de 16 itens (gate).
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
Confirmar: (a) caminho do dataset (gravar em `CLONE-CONFIG.json`); (b)
cenário pedido ou "à escolha do código"; (c) formato (proporção vem do
cenário; pedido explícito do usuário vence).

### 1. IDENTIFICAR — agente `01-analista-imagens`
- Ler as fotos do dataset; ATUALIZAR `_identity/mapeamento-facial.md` e
  REESCREVER `_identity/identidade.txt` (≤200 palavras, linguagem de prompt).
- Identidade.txt é a ÚNICA fonte do bloco de rosto/corpo nos prompts.
- Dataset mudou desde a última vez = reanálise mínima + data atualizada.

### 2. ESCOLHER CENÁRIO — código (não chute!)
```bash
python3 $CLONE_PKG/clone.py cenario [--tipo POV|PODCAST|NORMAL|...] [--seed N]
```
- Devolve SEMPRE inteiro 0–15 (assert) e grava histórico. Sem pedido, o
  código escolhe (evita os 3 últimos).
- O número define tudo: cenário, luz, luminosidade, objetos-críticos,
  naturalismo, hook — tudo em `scenarios/catalogo.json`.

### 3. COMPOR — agentes `02-criativos-clones` + `03-iluminacao`
- Rodar `python3 $CLONE_PKG/clone.py prompt --nro N --acao "…" [--variacoes K]`
  → `drafts/<job>/` com `prompt.md` (9 blocos), `negativo.md` (4 bases +
  extras), esqueletos `copy.md`/`qc.md`.
- 02 revisa: ação, variação de criativo (máx 3 mudanças; objeto trocado
  leva anatomia), escolhe a ÚNICA imperfeição da lista `realismo` do cenário.
- 03 confirma LUZ e escreve LUMINOSIDADE com os 4 números (EV, K dominante,
  razão key:fill, proteção de destaque/piso de sombra).

### 4. COPY — agente `04-copy-social`
`copy.md`: HOOK (3 s) + LEGENDA + CTA único + 5–10 hashtags + FORMATO
(proporção/plataforma do cenário). Idioma do usuário.

### 5. NEGATIVO/QC — agente `05-negativo-qc` (GATE — não é opcional)
- Negativo com as 4 bases imutáveis (pessoas/objetos/luz/naturalismo) +
  extras do cenário + adições do job.
- Gerar a imagem e executar os 16 itens do `qc.md` UM A UM (dedos contados;
  objetos conferidos parte a parte; exposição e temperatura checar
  contra os números declarados; naturalismo contra a lista do cenário).
- Veredito LIBERADO (16/16) ou RETRABALHO (itens + ajuste específico).
  Máx 2 retrabalhos; itens 13–16 só podem melhora; depois, escala humano.

### 6. ENTREGAR
- Mover o job para `saida/<AAAA-MM-DD>--<hhmm>--<agente>--<nro>-<slug>/`.
- `registrar.md` (10 linhas: cenário N, luz+luminosidade, veredito, correções).
- Opcional (SecondMind): nota de sessão no vault.

## Leis (invioláveis)
1. Sem QC (fase 5) não existe entrega. O agente negativo é gate, não sugestão.
2. O número de cenário SEMPRE está em 0–15; vem do código, nunca da memória.
3. Identidade vive em `_identity/identidade.txt`; prompt nunca "improvisa" rosto.
4. Clone muda SET, LUZ e AÇÃO — nunca rosto, tom de pele ou cabelo.
5. Dataset é somente leitura: nunca editar/renomear/mover fotos originais.
6. Máximo de 2 retrabalhos automáticos; depois, humano decide.
7. Cinco dedos por mão, pares de membros completos — verificação item a item.
8. LUZ SEM NÚMERO É CHUTE: todo prompt declara exposição (EV), temperatura
   dominante (K) e objetos-críticos com anatomia escrita.

## Estrutura do workspace (contrato)
```
<dataset>/
├── (suas fotos — somente leitura)
├── CLONE-CONFIG.json     # dataset, histórico de cenários
├── _identity/
│   ├── mapeamento-facial.md   # análise detalhada (auditable)
│   └── identidade.txt         # BLOCO CONGELADO p/ prompt (≤200 palavras)
├── drafts/<job>/          # prompt.md, negativo.md, copy.md, qc.md (+imagem)
├── saida/<job-final>/     # entregas aprovadas + registrar.md
└── state/                 # logs de cenário (jsonl)
```
