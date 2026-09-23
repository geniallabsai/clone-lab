# MATRIX — onde injetar o CloneLab

| Agente | Mecanismo | Passo |
|---|---|---|
| Claude Code | skill + CLAUDE.md | copie o pacote para `~/.claude/skills/clone-lab/`; aponte CLONE_HOME/CLONE_PKG no CLAUDE.md |
| Codex CLI / Copilot / Amp | AGENTS.md | este `AGENTS.md` + `BOOT.md` inlined na raiz do workspace |
| Hermes / OpenClaw / Gemini CLI | system prompt | cole `BOOT.md` integral (ele é autossuficiente) |
| Cursor | `.cursor/rules/clonelab.mdc` (alwaysApply) | `BOOT.md` no corpo da regra |
| Aider | `CONVENTIONS.md` | `BOOT.md` no topo do arquivo |
| Cline / Roo Code | `.clinerules/clonelab.md` | `BOOT.md` no corpo |
| Goose | `~/.config/goose/skills/clone-lab/SKILL.md` | copie o pacote inteiro |
| Windsurf | `.windsurf/rules/clonelab.md` | `BOOT.md` no corpo |

## Requisitos mínimos do ambiente
- Python 3 (stdlib apenas) para `clone.py`.
- Ferramenta de geração de imagem do agente (API ou plugin) — o pacote define
  prompt/negativo/formato; quem gera é o agente.
- Leitura/escrita na pasta do dataset.

## Receita para novo agente
1. Descubra o mecanismo de instrução dele (arquivo de regras ou prompt).
2. Cole `BOOT.md` integral lá (nunca resumo — as leis estão nele).
3. Defina `CLONE_HOME` e `CLONE_PKG`.
4. Rode `evals/deliver-qa.md` e adicione a linha na matriz.
