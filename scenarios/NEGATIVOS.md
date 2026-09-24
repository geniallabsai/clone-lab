# NEGATIVOS — bibliotecas do agente 05

## Regra da casa
Quatro bases **imutáveis** (`scenarios/negativos.json`): `base` (pessoas),
`objetos`, `luz` e `naturalismo`. Nenhum job remove termo de base. O cenário
SOMA extras (`negativos_extra` do catálogo). Job pode somar termo próprio —
nunca subtrair. `clone.py qc` exige as âncoras "6 fingers" (pessoas) e
"melted" (objetos) no arquivo.

## Base pessoas (`base`)
6 dedos, dedos fundidos, mãos deformadas, polegar invertido, membros extras,
rosto torto/assimétrico, sorriso torto, olhos desalinhados, pupila dupla,
dentes extras/faltando, língua estranha, pessoa duplicada, pele plástica/
cera, jpeg artifacts, baixa resolução, marca d'água.

## Base objetos (`objetos`) — v1.1
Melted objects, alças distorcidas, logos deformados, geometria quebrada,
objetos flutuando, física impossível, líquido torto, botões extras, zíper
torto, perna de cadeira quebrada, roda distorcida, caneca rachada, garfo
amassado, prop duplicado, texto ilegível em objetos, texto vazando pela cena,
parte faltando, **objeto sem sombra de contato**.

## Base luz (`luz`) — v1.1
Destaques estourados (clipped highlights), sombras esmagadas (crushed
blacks), céu queimado, **duas temperaturas conflitando sem prático visível**,
luz sem fonte visível, sombra sem direção consistente, banding em gradientes,
luz plana morta, sombras duras mortas, pele superexposta, olhos subexpostos,
posições de highlight inconsistentes.

## Base naturalismo (`naturalismo`) — v1.1
Fundo estéril hiperlimpo, pele de boneca, CGI render, pele aerografada,
simetria espelhada perfeita, sorriso posado, lábios de cera, zero textura de
pele, iluminação flat de museu, video game render, unreal engine look, pose
de stock photo, cabelo sem fios soltos, tecido lisinho demais.

## Extras por cenário (resumo — o oficial está no `catalogo.json`)
Cada cenário da tabela 0–15 traz seu próprio bloco: dedos em garra e polegar
invertido no POV · microfones/fones duplicados no Podcast · halter derretido e
espelho traiçoeiro no Fitness · letreiro com letras tortas no Palco/Neon ·
sombra projetada no Branco Limpo, etc. Leia o `negativos_extra` do número
sorteado ANTES de gerar.

## Checklist do QC (16 itens)
Está em `agents/05-negativo-qc.md` e no template `templates/qc.md`. O
`clone.py qc` valida a estrutura: 16 itens presentes + veredito + as duas
âncoras no negativo + blocos novos no prompt. O julgamento visual é do
agente (ou de humano).
