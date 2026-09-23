# NEGATIVOS — bibliotecas do agente 05

## Regra da casa
A base é **imutável**: nenhum job remove termo da base. O cenário SOMA extras
(campo `negativos_extra` do catálogo). Job pode somar termo próprio — nunca
subtrair.

## Base universal (`scenarios/negativos.json` → `base`)
Cobre as distorções que aparecem em QUALQUER geração com pessoa:

- mãos: `6 fingers`, `extra fingers`, `fused fingers`, `deformed hands`,
  `malformed hands`, polegar invertido/claw-like
- membros: `extra arms`, `extra legs`, `missing limbs`, `extra limbs`
- rosto: `warped face`, `asymmetric face`, `crooked smile`, `cross-eyed`,
  `malformed eyes`, `double pupil`, `extra teeth`, `missing teeth`
- duplicação: `duplicated person`, `twin artifact`, `ghost second person`
- pele: `plastic skin`, `over-smoothed skin`, `waxy skin`
- imagem: `jpeg artifacts`, `compression noise`, `color banding`, `halo
  edges`, `blurry`, `low resolution`, `watermarks`, `vignette burn`
- texto/cenário: `text artifacts`, `garbled letters`, `warped background`,
  `melting background`, `floating objects`, `disconnected shadows`
- coerência: `inconsistent lighting`, `distorted proportions`, `long neck`

Tradução PT-BR para humanos auditarem (os prompts saem em EN, que é o idioma
que modelos de imagem entendem melhor): 6 dedos, dedos fundidos, mãos
deformadas, braços/pernas extras, rosto torto, sorriso torto, olhos
desalinhados, pupila dupla, dentes extras/faltando, pessoa duplicada, pele
plástica, pele lisa demais, cera, artefatos jpeg, ruído, banding de cor, halo
nas bordas, embaçado, baixa resolução, marca d'água, texto fantasma, letras
tortas, fundo derretido, objetos flutuando, sombra descolada, luz
contraditória, proporções distorcidas, pescoço longo.

## Extras por cenário (resumo — o oficial está no `catalogo.json`)
Cada cenário da tabela 0–15 traz seu próprio bloco: dedos em garra e polegar
invertido no POV · microfones/fones duplicados no Podcast · halter derretido e
espelho traiçoeiro no Fitness · letreiro com letras tortas no Palco/Neon ·
sombra projetada no Branco Limpo, etc. Leia o `negativos_extra` do número
sorteado ANTES de gerar.

## Checklist do QC (12 itens)
Está em `agents/05-negativo-qc.md` e no template `templates/qc.md`. O
`clone.py qc` valida a estrutura: os 12 itens presentes + veredito + "6
fingers" no negativo. O julgamento visual é do agente (ou de humano).
