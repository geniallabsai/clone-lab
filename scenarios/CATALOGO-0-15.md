# CATALOGO 0-15 — os 16 cenários

Fonte única: `catalogo.json` (este arquivo é renderização humana).

| Nº | Cenário | Proporção | Quando usar |
|---|---|---|---|
| 0 | NORMAL | 1:1 | retrato base limpo; teste de identidade; avatar |
| 1 | ESTILO PODCAST | 16:9 | autoridade, conversa longa, episódios |
| 2 | POV | 9:16 | imersão, interação direta, humor, produto na mão |
| 3 | REELS VERTICAL | 9:16 | alcance, trend, storytelling rápido |
| 4 | STORY CONVERSA | 9:16 | proximidade, bastidores, resposta direta |
| 5 | GIMBAL MOVIMENTO | 9:16 | dinamismo, transição, energia de rua |
| 6 | QUARTO ESTILO | 16:9 ou 4:5 | identidade criador, setup, rotina, vídeo-aula longa |
| 7 | ESTUDIO PROFISSIONAL | 4:5 ou 1:1 | site, pitch, capa de lançamento, corporativo com cara |
| 8 | AURORE | 9:16 ou 16:9 | emoção, lifestyle, encerramento de dia |
| 9 | URBANO | 9:16 | atitude, streetwear, prova social de vida real |
| 10 | CAFETERIA | 4:5 | relatable, rotina, conteúdo de valor ('te ensinando') |
| 11 | FITNESS | 9:16 | transformação, disciplina, antes/depois, prova de processo |
| 12 | PALCO | 16:9 | grandeza, evento, fala, autoridade pública |
| 13 | LIFESTYLE PRODUCOAO | 4:5 | produto no contexto, rotina curada, 'como eu uso' |
| 14 | NEON NOTURNO | 9:16 | futurismo, música, ict, estética forte |
| 15 | BRANCO LIMPO | 1:1 | e-commerce, marketplace, foto de cadastro, clean |

## Camada de naturalismo (aplica a TODOS os cenários)

- **Modificador de prompt:** `photorealistic, natural candid photography, realistic skin texture with visible pores and subsurface scattering, subtle sensor grain, available/practical light only, slightly imperfect human framing, one flyaway strand of hair`
- **Regra 95/5:** 95% controle + 5% vivido: exatamente UMA imperfeição plausível por quadro (cabo frouxo, respingo na mesa, fio solto). Imagem 'perfeitamente limpa' reprova o item 16 do QC.
- **Pele:** skin with subsurface scattering, pores at close range, natural redness variation on cheeks and nose, no airbrush

## Especificação por cenário

### 00 — NORMAL
- **Aliases:** normal, retrato, basico, classico
- **Quando usar:** retrato base limpo; teste de identidade; avatar
- **Proporção:** 1:1 (feed) ou 4:5
- **Câmera:** medium close, lente 50mm, fundo neutro levemente desfocado
- **Luz (default):** key suave frontal a 30 graus, fill alto (razao 4:1), sem rim forte; 5600K neutra
- **Luminosidade (números):** exposição 0 EV; 5600K neutra única; razão key:fill 4:1; destaque na testa protegido, sombra mantendo detalhe de poros
- **Objetos críticos (perfeitos):**
  - painel de fundo neutro sem costura visível ou emenda
- **Naturalismo (a imperfeição que vende):** uma mecha solta no cabelo; gola da camiseta levemente assimétrica
- **Bloco de prompt:** retrato de estúdio limpo, fundo neutro cinza-claro sem objetos, olhando para a camera, postura natural relaxada, enquadramento do peito para cima
- **Ação padrão:** olhar direto para a camera com expressao neutra-confiante
- **Negativos extras:** fundo movimentado, objetos sobrepostos, sombras duras
- **Template de hook:** direto: diga quem é / o que faz na primeira linha (sem mistério)

### 01 — ESTILO PODCAST
- **Aliases:** podcast, estilo podcast, gravação, recording
- **Quando usar:** autoridade, conversa longa, episódios
- **Proporção:** 16:9 (capa) ou 4:5
- **Câmera:** medium shot 35mm, olho da camera, leve profundidade de campo
- **Luz (default):** trio quente intimista: key 3200K a 45 graus, fill suave do oposto, rim leve traseiro; sombras suaves no rosto
- **Luminosidade (números):** ambiente -0.3 EV (sensação de sala fechada); 3200K dominante; razão 3:1; rim traseiro sutil separando rosto do fundo escuro; catchlight pontual nos olhos
- **Objetos críticos (perfeitos):**
  - microfone dinâmico com grade metálica intacta, na haste
  - fones closed na orelha com concha bem formatada
  - caneca de café na mesa com pinta de resíduo
- **Naturalismo (a imperfeição que vende):** cabo dos fones levemente frouxo fora de alinhamento; prateleira de livros não perfeitamente nivelada
- **Bloco de prompt:** set de podcast profissional, microfone dinâmico amarrado na frente, fones na orelha, estante desfocada ao fundo com livros, parede escura quente, luz de estudio amarelada
- **Ação padrão:** fala para a camera como se respondesse alguem, uma maos perto do microfone
- **Negativos extras:** microfones duplicados, fones duplicados, cabos cruzando o rosto, segundo apresentador fantasma, letras tortas no estúdio
- **Template de hook:** pergunta que só você responde: 'se eu te dissesse que...'

### 02 — POV
- **Aliases:** pov, primeira pessoa
- **Quando usar:** imersão, interação direta, humor, produto na mão
- **Proporção:** 9:16
- **Câmera:** close levemente baixo (altura de quem conversa), 24mm, leve movimento de mão
- **Luz (default):** prática natural: janela lateral difusa 5600K, fill do ambiente, sem rigidez de estúdio
- **Luminosidade (números):** exposição 0 EV; 5600K de janela; fill alto 2:1; rosto protegido do fundo claro; sombras suaves e largas
- **Objetos críticos (perfeitos):**
  - caneca de cerâmica com alça intacta e pontos de apoio corretos na mão
  - dedos fazendo contato com pressão plausível (deformação leve da pele no ponto de contato)
- **Naturalismo (a imperfeição que vende):** mesa real com marcas de uso; alça da caneca com desgaste visível
- **Bloco de prompt:** cena point-of-view: a camera e o ponto de vista de quem esta conversando com a pessoa, a pessoa olha direto para a lens, proxidade de conversa real (a uns 60cm), um objeto na mao quando fizer sentido a acao
- **Ação padrão:** conversa direta como se a camera fosse outra pessoa; gestos naturais de dialogo
- **Negativos extras:** dedos em garra, polegar invertido, mao cobrindo a lens por acidente, objeto duplo na mao, segundas maos fantasmas
- **Template de hook:** comece no meio da frase: 'entao eu te pergunto:' (efeito de conversa interceptada)

### 03 — REELS VERTICAL
- **Aliases:** reels, tiktok, vertical, curto
- **Quando usar:** alcance, trend, storytelling rápido
- **Proporção:** 9:16
- **Câmera:** vertical, 24mm, energia: olhar forte, quebra de zoom sutil no hook
- **Luz (default):** key frontal suave + rim de separação leve; contraste médio-alto para leitura em tela pequena
- **Luminosidade (números):** contraste médio-alto (leitura em tela pequena); 5600K; terço superior reservado para texto (menos ruído visual)
- **Objetos críticos (perfeitos):**
  - placa/letreiro urbano com letras curtas, exatas e legíveis
  - pessoa de passagem cortada pela moldura de forma plausível
- **Naturalismo (a imperfeição que vende):** piso com rachadura fina; borrão de pedestre real (nunca rosto fantasma borrado)
- **Bloco de prompt:** video vertical de reels, enquadrado do quadril para cima, fundo urbano leve desfocado, composicao que deixa espaco em cima para texto, a pessoa gesticula com proposito
- **Ação padrão:** fala com energia para a camera, gesto de chamada no primeiro segundo
- **Negativos extras:** texto fora do espaco reservado, corte de ombro pela moldura, segunda pessoa no fundo
- **Template de hook:** afirmacao polêmica ou número: '3 erros que estão matando seu X'

### 04 — STORY CONVERSA
- **Aliases:** story, casual, dia a dia
- **Quando usar:** proximidade, bastidores, resposta direta
- **Proporção:** 9:16
- **Câmera:** selfie-real 24mm, levemente de cima (angulo de celular na mao), proximidade
- **Luz (default):** ring light frontal amaciado 4500K, brilho de celular, sombras mínimas
- **Luminosidade (números):** luz suave acentuadamente plana: 1:2; 4500K; sombras mínimas MAS micro-contraste preservado na pele (olho nunca preto puro)
- **Objetos críticos (perfeitos):**
  - celular selfie parcial na moldura (se aplicável)
  - reflexo de ring light como catchlight ÚNICO e pontual nos olhos
- **Naturalismo (a imperfeição que vende):** canto do quarto levemente desalinhado; parede com textura real (não fundo liso)
- **Bloco de prompt:** story autenticas: parece tirada de celular, fundo de ambiente real (sala/rua), leve imperfeicao de foco, a pessoa segura a camera com uma mao e fala
- **Ação padrão:** responde uma DM imaginada, tom conversado
- **Negativos extras:** luz de estudio perfeita demais (quebra a vibe), anel de luz com reflexo duplo estranho, dedo cortando o canto
- **Template de hook:** repita a pergunta do seguidor: 'me perguntaram se... a resposta curta: sim.'

### 05 — GIMBAL MOVIMENTO
- **Aliases:** gimbal, movimento, caminhando
- **Quando usar:** dinamismo, transição, energia de rua
- **Proporção:** 9:16
- **Câmera:** tracking em movimento a 35mm, levemente abaixo do olho, leve motion blur de fundo
- **Luz (default):** natural da cena (dia aberto 5600K ou noturno de letreiros), sem hard artificial
- **Luminosidade (números):** dia 5600K ou noite de letreiros; exposição -0.3 EV para sensação de movimento; UMA direção dominante de luz
- **Objetos críticos (perfeitos):**
  - móvel de rua (poste/faixa de pedestre) sem deformação
  - tênis/bolsa com movimento físico coerente com a passada
- **Naturalismo (a imperfeição que vende):** cinto da jaqueta balançando com a passada; uma gota de chuva no piso refletindo o letreiro
- **Bloco de prompt:** caminhando ate a camera em avenida/corredor, camera em gimbal recuando, fundo com leve motion blur, roupas com movimento, passo confiante
- **Ação padrão:** caminha falando direto para a camera, olhar constante
- **Negativos extras:** passos congelados/estranhos, perna extra no movimento, cabelo parado enquanto corpo anda, reflexo duplo de camera
- **Template de hook:** frase que completa com a chegada: 'tá indo te mostrar uma coisa...'

### 06 — QUARTO ESTILO
- **Aliases:** quarto, cozy, home, setup
- **Quando usar:** identidade criador, setup, rotina, vídeo-aula longa
- **Proporção:** 16:9 ou 4:5
- **Câmera:** fixa 35mm, plano médio, profundidade que mostra o setup desfocado
- **Luz (default):** mix quente aconchegante: lampada de mesa 2700K como prática + key frontal suave 4500K, janela fria leve ao fundo
- **Luminosidade (números):** DUAS temperaturas são o padrão DO CENÁRIO: 2700K da lâmpada (prático) + 4500K key; exposição 0 EV; sombra dupla coerente com as duas fontes visíveis
- **Objetos críticos (perfeitos):**
  - notebook aberto com conteúdo de tela plausível e levemente desfocado
  - lâmpada de mesa ACESA com fonte de luz visível dentro do quadro
  - prateleira/planta sem folha morta proeminente
- **Naturalismo (a imperfeição que vende):** cabo do fone pendendo frouxo; post-it torto no monitor; garrafa de água pela metade
- **Bloco de prompt:** cantinho de quarto/escritorio pessoal: carteira com notebook, lampada de mesa acesa, plantas, poster na parede desfocada, luz aconchegante de fim de tarde
- **Ação padrão:** sentado na frente do setup, pausa pensativa olhando a camera
- **Negativos extras:** setup genérico de banco de imagem, monitores duplicados, cabos visíveis demais, relógio com horas erradas
- **Template de hook:** confissão de rotina: 'o que ninguém conta sobre trabalhar de casa...'

### 07 — ESTUDIO PROFISSIONAL
- **Aliases:** estudio, profissional, corp
- **Quando usar:** site, pitch, capa de lançamento, corporativo com cara
- **Proporção:** 4:5 ou 1:1
- **Câmera:** 85mm, retrato formal do peito pra cima, foco cirúrgico no olho mais próximo
- **Luz (default):** clássica de estúdio: key 45 graus 5200K (softbox), fill 2x mais fraco, hair light traseiro superior; fundo com gradiente
- **Luminosidade (números):** 5200K estúdio; razão 5:1 com fill para manter poros na sombra; gradiente de fundo cinza-médio; nenhum estouro na têmpora
- **Objetos críticos (perfeitos):**
  - roupa com vincos naturais e gravata/fivela centralizada
  - fundo com gradiente uniforme (sem emenda)
- **Naturalismo (a imperfeição que vende):** um vinco natural na manga; simetria quase perfeita (cenário formal permite mais ordem que os outros)
- **Bloco de prompt:** estudio fotográfico profissional, fundo com gradiente suave de cor sólida, luz classica de tres pontos, roupa social despojada, posicao de poder relaxada
- **Ação padrão:** expressao confiante, leve sorriso fechado, ombros abertos
- **Negativos extras:** reflexo duplo de softbox no olho, fundo com emenda visivel, sombra dupla sob o queixo
- **Template de hook:** autoridade seca: uma frase de posicionamento, sem grito

### 08 — AURORE
- **Aliases:** aurea, golden hour, anoitecer
- **Quando usar:** emoção, lifestyle, encerramento de dia
- **Proporção:** 9:16 ou 16:9
- **Câmera:** 35mm, contraluz com proteção de sombra no rosto (fill da mão/reflexo)
- **Luz (default):** sol baixo atrás 2800K, rim de fogo no cabelo/ombro, fill dourado de rebote na frente; céu alaranjado
- **Luminosidade (números):** +0.7 EV no rim traseiro, rosto 0 EV com fill dourado de rebote; rim 2800K + fill 3500K (duas fontes, ambas naturais); céu NUNCA estourado — manter o gradiente alaranjado
- **Objetos críticos (perfeitos):**
  - sol direcional único (visível ou fora do quadro, mas com direção provável)
  - sombras longas tocando o chão no ângulo correto
  - óculos refletindo o sol (se houver) na posição exata da fonte
- **Naturalismo (a imperfeição que vende):** vento no cabelo; poeira suspensa pegando a luz (bokeh de partículas)
- **Bloco de prompt:** golden hour ao ar livre, sol baixo criando rim light quente nos contornos, leve flare controlado na lente, sombras longas, tom dourado-rosado no ar
- **Ação padrão:** olhando levemente para o lado pensando, cabelo mexido pelo vento
- **Negativos extras:** duas sombras em direções diferentes, sol duplo, pele verde de mistura de temperatura, nuvens sintéticas perfeitas
- **Template de hook:** frase de fechamento de dia: 'isso que ninguém vê antes das 6 da manhã...'

### 09 — URBANO
- **Aliases:** urbano, rua, street, candid
- **Quando usar:** atitude, streetwear, prova social de vida real
- **Proporção:** 9:16
- **Câmera:** 50mm, sensação de foto de passagem, foco rápido
- **Luz (default):** natural de rua: dia nublado difuso ou letreiro noturno como prática pontual
- **Luminosidade (números):** dia difuso 5600K ou noturno de letreiro; exposição 0 EV; rosto jamais plano (manter contorno do osso zigomático)
- **Objetos críticos (perfeitos):**
  - letreiro com palavra curta REAL e coerente (3 letras no máximo de dúvida)
  - piscina de água no asfalto refletindo o letreiro no lado certo
- **Naturalismo (a imperfeição que vende):** um charuto de bituca no chão? NÃO — mancha de borrão de pneu; passageiro real em foco aberto
- **Bloco de prompt:** street photography urbana, calçadão/avenia, bokeh de letreiros e pessoas ao fundo, vestimenta streetwear, atitude de quem passa despercebido
- **Ação padrão:** olha de perfil para a camera como quem acabou de notar o fotografo
- **Negativos extras:** pessoas fantasma cortadas ao meio, letreiro com letra errada, duas sombras de calçada
- **Template de hook:** contraste: a cidade grita, a frase sussurra

### 10 — CAFETERIA
- **Aliases:** cafeteria, cafe, work cafe
- **Quando usar:** relatable, rotina, conteúdo de valor ('te ensinando')
- **Proporção:** 4:5
- **Câmera:** 35mm de lado da mesa (visão do outro cliente), lata/café em primeiro plano levemente desfocado
- **Luz (default):** janela lateral natural 5600K, contraste suave, vapor do café como textura (opcional)
- **Luminosidade (números):** luz lateral de janela 5600K; razão 3:1 direcional; vapor contraluzado em silhueta; highlight na borda da caneca
- **Objetos críticos (perfeitos):**
  - caneca com vapor fino e plausível (trilhas tênues, não nuvem)
  - notebook com conteúdo de tela crível
  - ponto de anel de café na madeira (marca de caneca)
- **Naturalismo (a imperfeição que vende):** caneta ao lado do notebook; a marca de anel de café na mesa (imperfecção que ancora a cena)
- **Bloco de prompt:** cafeteria com luz de janela, mesa de madeira, notebook aberto e cafe na frente, cadeira de restaurante ao fundo desfocada, atmosfera tranquila de trabalho remoto
- **Ação padrão:** explica algo apontando para o notebook, sorriso leve, cafe perto
- **Negativos extras:** copos duplos, reflexo estranho na tela, letreiro do cafe com palavra torta, mao com 6 dedos segurando a caneca
- **Template de hook:** promessa prática: 'a mesma ideia que usei pro meu X, em 30 segundos'

### 11 — FITNESS
- **Aliases:** fitness, academia, treino, gym
- **Quando usar:** transformação, disciplina, antes/depois, prova de processo
- **Proporção:** 9:16
- **Câmera:** baixa 28mm (ângulo heróico), close no esforço
- **Luz (default):** fluorescente de academia real (5600K frio) ou janela lateral dura de box; suor = highlight real
- **Luminosidade (números):** fluorescente duro 5600K + janela lateral dura; razão 6:1 escultorando o relevo; suado = brilhos pontuais coerentes com a fonte
- **Objetos críticos (perfeitos):**
  - halter/barras com textura de usinagem intacta (knurling)
  - colchonete sem rasgo; marcas de uso plausíveis
  - suor como pontos especulares pequenos (nunca rios)
- **Naturalismo (a imperfeição que vende):** resíduo de giz na barra; pegadas antigas no colchonete
- **Bloco de prompt:** academia funcional, halteres/barras ao fundo, roupa tecnica correta, gota de sudo no rosto, luz dura lateral marcando o relevo muscular, ambiente real de treino
- **Ação padrão:** pausa entre repeticoes olhando a camera, respiracao visivel
- **Negativos extras:** halter deformado/derretido, corda do aparelho fantasma, espelho refletindo versao diferente do rosto, suor virando poça fora do lugar
- **Template de hook:** número de processo: 'dia 47. o que mudou desde o 1:'

### 12 — PALCO
- **Aliases:** palco, apresentacao, talk, keynote
- **Quando usar:** grandeza, evento, fala, autoridade pública
- **Proporção:** 16:9
- **Câmera:** 85mm da plateia (leve subida), spotlight com facho visível na fumaça
- **Luz (default):** spot principal 4800K duro com pool no chão, fill azul frio residual, plateia preta
- **Luminosidade (números):** spot 4800K no sujeito; ambiente -1.5 EV; plateia preta com detalhe apenas nas primeiras 2 fileiras; facho visível
- **Objetos críticos (perfeitos):**
  - tela LED do palco com gráfico limpo (sem letra vazando)
  - lapela de microfone bem presa
  - fumaça apenas dentro do facho do spot
- **Naturalismo (a imperfeição que vende):** uma cabeça na plateia erguendo celular para filmar (silhueta)
- **Bloco de prompt:** palco de conferencia, spot unico com facho visivel na fumaca leve, plateia em silhueta escura, microfone de lapela, tela gigante desfocada atraz
- **Ação padrão:** gesto de apertura na fala, olhar varrendo a plateia
- **Negativos extras:** duas pessoas no palco sem pedido, letreiro do evento com letras tortas, facho de luz sem fonte visivel, plateia com rostos borrados estranhos
- **Template de hook:** a frase da talk: a que valeria gravar no celular

### 13 — LIFESTYLE PRODUCOAO
- **Aliases:** lifestyle, flatlay, producao, unboxing
- **Quando usar:** produto no contexto, rotina curada, 'como eu uso'
- **Proporção:** 4:5
- **Câmera:** overhead-leve 45 graus com a pessoa no quadro + flatlay de elementos
- **Luz (default):** difusa ampla (softbox grande ou varanda), sombras suaves e longas em diagonal
- **Luminosidade (números):** softbox amplo 5500K; exposição +0.3 EV; sem sombra projetada NO CHÃO MAS com sombra de contato sob os objetos
- **Objetos críticos (perfeitos):**
  - produto/herói com logo e etiqueta NÃO distorcidos (descrever a palavra exata entre aspas)
  - tecido com trama visível (fiapos reais)
  - SOMBA DE CONTATO sob cada objeto (shadowless ≠ sem sombra de contato)
- **Naturalismo (a imperfeição que vende):** um único objeto levemente fora do grid perfeito (vida na composição)
- **Bloco de prompt:** composicao lifestyle overhead-diagonal: a pessoa na cena com os objetos do produto dispostos com folga (caneca, caderno, acessorios), paleta coerente, espaco negativo generoso
- **Ação padrão:** interage com um dos objetos (abre/escreve/apresenta) olhando para a camera
- **Negativos extras:** objetos flutuando sem sombra, sombra dupla dos objetos, logo de marca aleatoria, mao cortada pela borda do quadro
- **Template de hook:** o item-herói nomeado: 'esse objeto que resolveu meu X'

### 14 — NEON NOTURNO
- **Aliases:** neon, noturno, cyber, noite
- **Quando usar:** futurismo, música, ict, estética forte
- **Proporção:** 9:16
- **Câmera:** 35mm de frente, reflexos de neon no rosto e nos óculos/pele
- **Luz (default):** duas práticas de LED: magenta esquerda + ciano direita (3200/5600 simuladas), fundo quase preto, rim frio superior
- **Luminosidade (números):** dupla prática magenta+ciano (3200/5600 simulados); fundo próximo de preto (não preto morto); exposição 0 EV; saturação controlada (zero banding)
- **Objetos críticos (perfeitos):**
  - letreiro neon com palavra EXATA e correta (entre aspas)
  - reflexo do neon na pele/óculos na posição coerente com a fonte (esq./dir.)
- **Naturalismo (a imperfeição que vende):** um dos neons levemente piscando (plausível); condensação no copo ao fundo
- **Bloco de prompt:** cena noturna neon urbana: letreiros magenta e ciano pintando os dois lados do rosto, fundo preto azulado com bokeh de luzes, reflexo de neon na pele e na roupa, atmosfera cyber leve
- **Ação padrão:** expressao calma quase desafiadora, leve sorriso
- **Negativos extras:** banding nas cores, pele alaranjada de mistura errada, letreiro neon com palavra ilegivel, brilho de flash em cima do neon (quebra a cena)
- **Template de hook:** futuro próximo: 'em 2030 isso vai parecer coisa de 1999'

### 15 — BRANCO LIMPO
- **Aliases:** branco, limpo, ecommerce, produto
- **Quando usar:** e-commerce, marketplace, foto de cadastro, clean
- **Proporção:** 1:1
- **Câmera:** fixa 85mm frontal, pessoa centralizada, rodapé da composição invisível
- **Luz (default):** softbox frontal amplo 5500K + rebatedores laterais; zero sombra projetada (shadow-free)
- **Luminosidade (números):** softbox frontal amplo 5500K; branco puro 255 sem zona estourada na pele (expor pela roupa); micro-contraste na trama
- **Objetos críticos (perfeitos):**
  - roupa com textura de trama visível (jamais cerada)
  - fundo branco #FFFFFF uniforme (zero gradiente)
  - micro-vinco natural em ponto único da barra
- **Naturalismo (a imperfeição que vende):** o micro-vinco natural na barra da peça (a única assinatura viva)
- **Bloco de prompt:** foto de ecommerce sobre fundo branco puro infinito, luz suave sem sombra projetada, roupa vista completa do corpo (ou conforme a acao), detalhes tecidos nitidos, sem decoracao nenhuma
- **Ação padrão:** posicao neutra frontal, rosto a camera
- **Negativos extras:** sombra projetada no chão, fundo off-white (tem que ser branco), dobra de tecido irrevel, reflexo de softbox na superficie
- **Template de hook:** beneficio único em 6 palavras (e-commerce não cabe história)
