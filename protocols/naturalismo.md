# Protocolo Naturalismo — anti-olhar-IA (v1.1)

Este protocolo existe porque o maior defeito de imagem gerada não é defeito —
é **perfeição**. Quadro sem vida some do feed em 0,4 s.

## A regra 95/5
Cada quadro carrega 95% de controle (identidade, luz, composição, objetos) +
exatamente 5% de vida: **uma** imperfeição plausível por quadro, escolhida da
lista `realismo` do cenário sorteado no catálogo. Duas imperfeições = bagunça;
zero = maquete. Imagem "perfeitamente limpa" reprova o item 16 do QC.

## Os sinais de olhar-IA (reprovam automaticamente)
- pele lisa de boneca (sem poros, sem sub-superfície, sem vermelhidão natural
  em bocheira/nariz)
- cabelo perfeitamente alinhado (falta de 2–3 fios soltos)
- simetria espelhada de composição ou de rosto
- fundo estéril, sem nada vivo (uma textura, uma marca, uma sombra de janela)
- sorriso de catálogo, olhos sem catchlight real
- roupa cerada, sem um único vinco físico
- luz plana sem direção de sombra identificável
- "unreal engine look": saturação alta demais + sombras mortas + banding

## Anatomia de pele (obrigatória em close)
Poros visíveis no enquadramento, sub-surface scattering (translúcido nas
orelhas/dedos), variação natural de vermelhidão, sutil oleosidade T-zone em
cenários quentes, cicatriz/sinal exatamente onde o mapeamento registra.

## Objetos perfeitos ≠ objetos decorativos
"Perfeito" aqui significa **geometricamente correto**, não decorado: alça
inteira, grade do microfone completa, logotipo com a palavra exata entre
aspas no prompt, sombra de contato sob o objeto, física de líquido plausível.
Objeto crítico SEM anatomia escrita no prompt = dado como derretido pelo QC
(item 13), independente de estar "bonito".

## Luminosidade com números
Nenhum prompt sai sem: exposição (EV), temperatura dominante (K), razão
key:fill, proteção de destaques e piso de sombra. Duas temperaturas só quando
há prático visível que as justifica (lâmpada de mesa no cenário 06, sol+reflexo
no 08). O campo `luminosidade` do catálogo já traz os números do cenário —
o agente 03 aplica, não inventa.

## Verificação
Item 16 do QC (naturalismo) + item 15 (luminosidade) + item 13 (objetos)
formam o trio anti-IA. Todos três precisaram passar na tentativa anterior
para o retrabalho considerar "melhora" — se um deles piorou, a variação
anterior vale mais.
