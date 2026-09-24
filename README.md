# CloneLab 🎭 (v1.1)

**Pacote ultra de skills: um esquadrão de agentes que transforma o SEU dataset
de fotos em clonagens consistentes suas — em qualquer cenário, com número,
luz, copy e vetos anti-distorção.**

O CloneLab é 5 especialistas + 1 código que nunca erra a faixa:

| Agente | Missão |
|---|---|
| `01-analista-imagens` | Varre o dataset, mapeia seu rosto/corpo/e estilo → arquivo de identidade |
| `02-criativos-clones` | Compõe o cenário e gera clones: variações que MUDAM o set, NUNCA o rosto |
| `03-iluminacao` | Escreve a luz do cenário (key/fill/back, áurea, estúdio, neon) |
| `04-copy-social` | Hook de 3 s, legenda, CTA, hashtags e formato por plataforma |
| `05-negativo-qc` | O agente NEGATIVO: veta 6 dedos, membros extras, rosto errado, texto torto |

## Os 16 cenários numerados (0–15)

| # | Cenário | # | Cenário |
|---|---|---|---|
| 0 | NORMAL (retrato base) | 8 | ÁUREA (golden hour) |
| 1 | ESTILO PODCAST | 9 | URBANO (rua, bokeh) |
| 2 | POV (câmera 1ª pessoa) | 10 | CAFETERIA |
| 3 | REELS VERTICAL | 11 | FITNESS |
| 4 | STORY CONVERSA | 12 | PALCO / APRESENTAÇÃO |
| 5 | GIMBAL MOVIMENTO | 13 | LIFESTYLE PRODUÇÃO |
| 6 | QUARTO ESTILO (cozy) | 14 | NEON NOTURNO |
| 7 | ESTÚDIO PROFISSIONAL | 15 | BRANCO LIMPO (e-commerce) |

**A numeração é lei do código**: `clone.py cenario` SEMPRE devolve 0–15
(asserted), seja pedindo por nome (`--tipo PODCAST` → 1, `--tipo POV` → 2,
`--tipo NORMAL` → 0) ou deixando o código escolher (evita os 3 últimos já
usados, registrado em `state`).

## Instalação (90 segundos)

```bash
git clone https://github.com/geniallabsai/clone-lab
cd clone-lab
python3 clone.py init ~/minhas-fotos      # estrutura + varredura do dataset
```

Injete o esquadro no seu agente: cole `BOOT.md` no system prompt (Hermes,
OpenClaw, Gemini, qualquer um) — ou siga `agents/MATRIX.md` (Claude Code,
Codex/Copilot, Cursor, Aider, Cline/Roo, Goose…).

## Uso (linguagem natural)

> "Clona meu rosto num podcast" → cenários 1 · "modo POV" → 2 ·
> "me dá algo" (sem pedir nada) → o código sorteia um número 0–15
> nunca repetido 3x seguidos.

Pipeline em 6 fases (SKILL.md): CONTRATO → IDENTIFICAR → ESCOLHER CENÁRIO
(código) → COMPOR (clones+luz) → COPY → NEGATIVO/QC (gate) → ENTREGAR.
Toda entrega sai em `saida/<data>--<nro>--<slug>/` com `prompt.md`,
`negativo.md`, `copy.md`, `qc.md` — reprodutível de ponta a ponta.

## Garantias

1. **Sem QC, não tem entrega** — o agente negativo roda em toda saída com
   **16 itens**: pessoas, objetos conferidos parte a parte, física,
   luminosidade e naturalismo (anti-olhar-IA).
2. **Número sempre 0–15** — fora da faixa o próprio código aborta.
3. **Identidade é arquivo** — prompts nunca saem da memória; saem de
   `_identity/identidade.txt` (congelado: rosto/pele/cabelo são variáveis imutáveis).
4. **Luz com números** — todo prompt declara exposição (EV), temperatura
   dominante (K), razão key:fill e proteção de destaques/sombras.
5. **Objetos perfeitos** — cada cenário traz sua lista de objetos-críticos
   com anatomia obrigatória no prompt (alça, grade, logo, trama do tecido).
6. **Cena com vida** — regra 95/5: exatamente uma imperfeição plausível por
   quadro, escolhida da lista do cenário (`protocols/naturalismo.md`).
7. **Dataset é somente leitura** — os agentes não tocam suas fotos originais.
8. **Reverso é possível** — cada entrega guarda prompt + negativo + veredito.

## Integração (opcional)

Se você rodar SecondMind junto (`geniallabsai/secondmind`), a fase 6 escreve
a nota de sessão no vault: o histórico de clonagens vira memória persistente.

## Licença

MIT
