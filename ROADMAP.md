# Roadmap — do pacote ao programa

**v1 (este repositório):** skills + `clone.py` em Python puro. O pipeline é
executável hoje por qualquer agente de LLM com acesso a arquivos e a uma
API/modelo de geração de imagem.

## v2 — `clone.py serve`
- watch de `drafts/` → ao detectar `qc.md` com LIBERADO, move para `saida/`
  sozinho e (com SecondMind) grava a nota de sessão.
- `clone.py batch --tipo NORMAL --qtd 8` → fila de entregas numeradas.

## v3 — visão embutida
- QC real em pixels: contagem de dedos via modelo de visão (substitui o
  checklist preenchido pelo agente quando há API de imagem disponível);
  similaridade facial do resultado vs. `_identity/referencias/` (embedding
  opcional, off por padrão).
- `clone.py compare <dir1> <dir2>` — A/B de clones.

## v4 — rede de clonagens
- export/import de identidade entre máquinas (memória compartilhada: reutiliza
  o protocolo share do SecondMind).
- catálogos de cenários por cliente (0–15 é o padrão; packs adicionais
  numerados 16+ só por versão explícita do catálogo).

**Regra de ouro:** o catálogo 0–15 não muda sem bump de versão; prompts e
negativos são implementação do catálogo, nunca substituto dele.
