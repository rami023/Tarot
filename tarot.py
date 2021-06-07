import random
###Reverse Def###
def reversed():
    global rev1,rev2,rev3
    rev1=random.randint(1,2)
    rev2=random.randint(1,2)
    rev3=random.randint(1,2)
    if rev1 == 1:
        rev1='reversed'
    else:
        rev1='normal'
    if rev2 == 1:
        rev2='reversed'
    else:
        rev2='normal'
    if rev3 == 1:
        rev3='reversed'
    else:
        rev3='normal'
reversed()
#To test
#print(rev1,rev2,rev3)
###ASSIGN VALUES TO CARDS###
def definicion(tirada,orientacion):
    if tirada =='El Mago'and orientacion =='normal':
        print('[I] El Mago, El Alquimista, El Prestidigitador Originalidad. Iniciativa,')
        print('centro de acción, inteligencia espontánea. Posesión de sí mismo,')
        print('autonomía, emancipación de todo prejuicio. Elocuencia, destreza,')
        print('habilidad, finura, diplomacia. Abogado, orador, diplomático o político.')
    elif tirada== 'El Mago' and orientacion=='reversed':
        print('Carente de escrúpulos, arribista, intrigrante, embustero, pillo, estafador')
        print('charlatán. Indecisión, ineptitud, voluntad débil, retraso, inseguridad.')
        print('Voluntad aplicada a malos fines.')
    elif tirada== 'La Sacerdotista' and orientacion=='normal':
        print('[II] La Sacerdotisa Paciencia, silencio, discreción, reserva, meditación,')
        print('modestia, resignación y piedad. Decisión meditada.')
    elif tirada== 'La Sacerdotista' and orientacion=='reversed':
        print('Disimulo, intenciones ocultas, rencor, pereza, intolerancia, fanatismo. Se')
        print('vuelve pesada y pasiva, es como una carga. Retraso, tensión y torpeza')
        print('en las relaciones. Decisión inmeditada.')
    elif tirada== 'La Emperatriz' and orientacion=='normal':
        print('[III] La Emperatriz Comprensión, inteligencia, instrucción. Encanto,')
        print('afabilidad, elegancia, distinción. Cortesía, abundancia, riqueza.')
        print('Matrimonio, fecundidad, dulzura.')
    elif tirada== 'La Emperatriz' and orientacion=='reversed':
        print('Afectación, pose, frivolidad, coquetería, vanidad. Desdén, presunción.')
        print('Lujo innecesario. Sensible a los halagos. Falta de refinamiento.')
        print('Discusiones en todos los planos. Esterilidad.')
    elif tirada== 'El Emperador' and orientacion=='normal':
        print('[IV] El Emperador Poder, voluntad, energía, certeza, constancia,')
        print('firmeza, rigor, exactitud, equidad y positivismo. Realización. Protector')
        print('poderoso.')
    elif tirada== 'El Emperador' and orientacion=='reversed':
        print('Testarudez, falta de idealismo. Adversario obstinado. Caída, pérdida de')
        print('los bienes.')
    elif tirada == 'El Papa' and orientacion == 'normal':
        print('[V] El Sumo Sacerdote, El Papa Sabiduría, perseverancia, enseñanzas')
        print('consejos equitativos, generosidad e indulgencia, mansedumbre. Ayuda')
        print('de los superiores, organización. La carga que representa al consultante')
        print('(usted), en la forma de la voz interior. Dogma.')
    elif tirada == 'El Papa' and orientacion == 'reversed':
        print('Jefe sentencioso, excesivamente crítico, moralista estrecho de miras,')
        print('profesor autoritario, teórico limitado, consejero desprovisto de sentido')
        print('práctico, carencia de apoyo espiritual. Inconvencional, ilógico,')
        print('supersticioso, incapaz de actuar coherente y racionalmente.')
    elif tirada == 'Los Enamorados' and orientacion == 'normal':
        print('[VI] Los Enamorados Elección o decisión. Unión, matrimonio, amor, la')
        print('unión de los opuestos, atracción, balance, apertura a la inspiración.')
        print('Pruebas superadas. Armonía de la vida interior y el mundo exterior.')
    elif tirada == 'Los Enamorados' and orientacion == 'reversed':
        print('Desorden, fracaso, divorcio, amor desgraciado y contrariedades de')
        print('todo tipo. Matrimonio frustrado, tentación peligrosa. Peligro de ser')
        print('seducido. Inconducta, libertinaje y debilidad. Peleas, infidelidad.')
        print('Inestabilidad emocional.')
    elif tirada == 'El Carro' and orientacion == 'normal':
        print('[VII] El Carro Triunfo, victoria, superación de obstáculos, esperanza,')
        print('conquista. Buena noticia inesperada. Gran autocontrol, habilidad para')
        print('determinar el propio destino. Gran fuerza física y mental. Velocidad.')
        print('Viaje.')
    elif tirada == 'El Carro' and orientacion == 'reversed':
        print('Desorden generalizado. Enfermedad. Peligroso descontrol. Peligro de un')
        print('accidente violento. Malas noticias. Fatiga. Falta de tacto. Mala conducta.')
        print('Actividad afiebrada y sin reposo.')
    elif tirada == 'La Justicia' and orientacion == 'normal':
        print('[VIII] La Justicia Justicia, armonía, equidad, integridad, regla de')
        print('conducta, firme propósito, acción de juzgar, moderación en todas las')
        print('cosas. Indepenencia de espíritu. Para mantener el balance ciertas cosas')
        print('deben ser sacrificadas. Puede estar relacionada con asuntos legales,')
        print('jucios, matrimonios, divorcios, etc.')
    elif tirada == 'La Justicia' and orientacion == 'reversed':
        print('Fanatismo, injusticia, severidad en el juicio, abuso, acusaciones falsas.')
        print('Inseguridad. Marañas legales. Inseguridad. Falta de un apropiado')
        print('balance.')
    elif tirada == 'El Ermitaño' and orientacion == 'normal':
        print('[IX] El Ermitaño, El Peregrino Prudencia, sabiduría, paciencia, silencio,')
        print('avance espiritual, inspiración divina, circunspección. Retiro del mundo,')
        print('soledad. Peregrinaje. Puede ser un maestro. La realización de un')
        print('balance y progresar.')
    elif tirada == 'El Ermitaño' and orientacion == 'reversed':
        print('Inmadurez, vicios, oscuridad, testarudez, traición, engaño. Misantropía,')
        print('misoginia, celibato. Persona excesivamente tímida e insociable.')
        print('Enemigos ocultos. Prudencia que sobra o que falta.')
    elif tirada == 'La Rueda de La Fortuna' and orientacion == 'normal':
        print('[X] La Rueda de la Fortuna Cambio, evolución, éxito, buena fortuna,')
        print('destino. Felicidad, abundancia. Nuevas condiciones. Abundancia,')
        print('crecimiento.')
    elif tirada == 'La Rueda de La Fortuna' and orientacion == 'reversed':
        print('La transformación se efectuará dificultosamente pero se hará de todos')
        print('modos. Progreso retardado, Retroceso.')
    elif tirada == 'La Fuerza' and orientacion == 'normal':
        print('[XI] La Fuerza Sublimación o regulación de las pasiones y bajos')
        print('instintos. Poder, energía, gran amor. El espíritu que domina la materia.')
        print('Acción, coraje, éxito. Poderosa voluntad y gran fuerza física. La fuerza')
        print('interior que domestica la bestia. Poder sobre los animales.')
    elif tirada == 'La Fuerza' and orientacion == 'reversed':
        print('Discordia, ruina. Debilidad, testarudez, abuso de poder. Impaciencia,')
        print('temeridad, grosería, insensibilidad. dureza, crueldad, furor.')
    elif tirada == 'El Colgado' and orientacion == 'normal':
        print('[XII] El Colgado Fortaleza, sabiduría. Limitaciones auto impuestas.')
        print('Iniciación, prueba. Redención a través del sacrificio, pérdida. Poder')
        print('profético. Decisiones suspendidas. Elección que requiere contemplación.')
    elif tirada == 'El Colgado' and orientacion == 'reversed':
        print('Arrogancia, egotismo, resistencia a las influencias espirituales.')
        print('Materialismo. Esfuerzo desperdiciado. Falsa profecía. Fracaso. Falta de')
        print('límites, falta de franqueza, carencia de sacrificio.')
    elif tirada == 'La Muerte' and orientacion == 'normal':
        print('[XIII] La Muerte Transformación completa. Muerta y renacimiento. El')
        print('fin de algo. Evolución desde un estado a otro superior. Cambio')
        print('provechoso.')
    elif tirada == 'La Muerte' and orientacion == 'reversed':
        print('Estancamiento, muerte, petrificación. Enfermedad incurable.')
        print('Matrimonio roto. Falta de oportunidades, esperanza deshecha.')
    elif tirada == 'La Templanza' and orientacion == 'normal':
        print('[XIV] La Templanza Consideración cuidadosa, paciencia, moderación,')
        print('adaptación, compostura, reflexión. Paciencia uniendo dos opuestos,')
        print('combinándolos cuidadosamente. Buen matrimonio. Trabajando en')
        print('armonía con otros, habilidad directiva. Algo se está preparando. Gran')
        print('talento y creatividad. Luchando por trascendencia a través del trabajo.')
        print('Alquimia. La unión de los opuestos refinada por el fuego de la voluntad.')
    elif tirada == 'La Templanza' and orientacion == 'reversed':
        print('Desorden, conflicto, mala combinación, peleas. Posibilidad de naufragio.')
        print('Desarreglos.')
    elif tirada == 'El Diablo' and orientacion == 'normal':
        print('[XV] El Diablo Destino (bueno o malo). Poder de seducción, impulso')
        print('ciego, tentación, obsesión. Desviación sexual. Un estado mental')
        print('confusional. Las pasiones carnales descontroladas.')
    elif tirada == 'El Diablo' and orientacion == 'reversed':
        print('Carta dañina, fatalidad, mal uso de la fuerza. Debilidad, ceguera,')
        print('desorden. Efectos maléficos. La patética condición humana que prefiere')
        print('la ilusión a la verdad.')
    elif tirada == 'La Torre' and orientacion == 'normal':
        print('[XVI La Torre Cambios repentinos sin otra alternativa. Colapso, escape')
        print('de la prisión o liberación de ataduras, accidente. Los planes fracasarán,')
        print('las intenciones no se realizarán. El "dedo de Dios". Bancarrota. Muerte')
        print('súbita.')
    elif tirada == 'La Torre' and orientacion == 'reversed':
        print('Confusión completa. Ganar la libertad a un gran costo. Falsas')
        print('acusaciones, opresión. Castigo que resulta de los excesos cometidos,')
        print('enfermedad. Error presuntuoso que no sabe rectificarse a tiempo.')
    elif tirada == 'La Estrella' and orientacion == 'normal':
        print('[XVII] La Estrella Esperanza, ayuda inesperada, perspicacia y claridad')
        print('de visión, inspiración, flexibilidad. Un gran amor será dado y recibido.')
        print('Buena salud. Carta totalmente espiritual.')
    elif tirada == 'La Estrella' and orientacion == 'reversed':
        print('Arrogancia, pesimismo, testarudez. enfermedad, error de juicio.')
        print('Impotencia psíquica, reestructuración, privación y abandono.')
    elif tirada == 'La Luna' and orientacion == 'normal':
        print('[XVIII] La Luna Intuición, umbral de un importante cambio, camino')
        print('difícil y oscuro, desarrollo de poderes psíquicos. Navegación,')
        print('experimentación, trabajo penoso.')
    elif tirada == 'La Luna' and orientacion == 'reversed':
        print('Peligros no vistos, enemigos ocultos, alucinación, autoengaño, histeria,')
        print('desorientación. Inestabilidad, embustes, trampas, falso saber, carácter')
        print('neurótico. Escándalo, secreto que se hace público, chantajista.')
    elif tirada == 'El Sol' and orientacion == 'normal':
        print('[XIX] El Sol Gloria. Felicidad material. Matrimonio o relación feliz,')
        print('colaboración. Exito. Placer, energía, motivación, inspiración.')
    elif tirada == 'El Sol' and orientacion == 'reversed':
        print('Molestias, disimulos, arrogancia, vanidad. Compromiso o trabajo')
        print('perdido. Tanteo en la oscuridad, desorientación. Deseo de figurar.')
    elif tirada == 'El Juicio' and orientacion == 'normal':
        print('[XX] El Juicio Cambio radical, resurección a una vida nueva. Trabajo (o')
        print('vida) bien hecha. Voluntad para iniciar algo nuevo. Buen juicio y')
        print('discernimiento. Poder creativo e influencia sobre la familia y la carrera')
        print('laboral. Capacidad de perdonar. Despertar. Dictámen judiciale')
        print('favorable.')
    elif tirada == 'El Juicio' and orientacion == 'reversed':
        print('Vacilación espiritual, debilidad, juicio o decisión equivocada.')
        print('Enfermedad, separación. Dictamen juidicial adverso. Error sobre sí')
        print('mismo y sobre los otros. Decisión postergada.')
    elif tirada == 'El Mundo' and orientacion == 'normal':
        print('[XXI] El Mundo Suceso garantizado. Recompensas recibidas. Viaje,')
        print('emigración (dentro del mismo continente), cambio de lugar de')
        print('residencia. Compra o venta de tierras.')
    elif tirada == 'El Mundo' and orientacion == 'reversed':
        print('Obstáculos, estancamiento, estorbos. Necesidad de trabajar muy duro')
        print('para alcanzar el éxito.')
    elif tirada == 'El Loco' and orientacion == 'normal':
        print('[0] El Loco Carencia de sentido común. Potencial fuerza de voluntad y')
        print('destreza. El espíritu en busca de experiencia. Audacia, extravagancia.')
        print('Negligencia, poca reflexión. Desorientación, inmadurez, desequilibrio.')
        print('Ligereza. Indiscreción y superficialidad.')
    elif tirada == 'El Loco' and orientacion == 'reversed':
        print('Pasiones y obsesiones, indecisión, irracionalidad, apatía,')
        print('complicaciones. Decisiones equivocadas, caída, abandono,')
        print('inmovilización. Locura. Desborde psíquico y/o emocional. Viaje')
        print('obstaculizado.')


title = input('Como te llamas?\n')

print('''\n\n\n\n------- Nombre--------\n\n'''+title+'\n\n')


##TEST APP
#rev1='reversed'
#tarot1='El Mago'
#definicion(tarot1,rev1)
tarot= ['El Mago','La Sacerdotista','La Emperatriz','El Emperador','El Papa','Los Enamorados','El Carro','La Justicia','El Ermitaño','La Rueda de La Fortuna','La Fuerza','El Colgado','La Muerte','La Templanza','El Diablo','La Torre','La Estrella','La Luna','El Sol','El Juicio','El Mundo','El Loco']
### EL PASADO###
print('---EL PASADO---')
tarot1=random.choice(tarot)
print(tarot1)
print('')
print('Sentido de la carta: ',rev1)
print('')
definicion(tarot1,rev1)
print('')
###EL PRESENTE###
print('---EL PRESENTE---')
tarot2=random.choice(tarot)
if tarot2==tarot1:
    tarot2=random.choice(tarot)
    print(tarot2)
else:
    print(tarot2)
print('')
print('Sentido de la carta: ', rev2)
print('')
definicion(tarot2,rev2)
print('')
###EL FUTURO###
print('---EL FUTURO---')
tarot3=random.choice(tarot)
if tarot3==tarot1 or tarot3==tarot2:
    tarot3=random.choice(tarot)
    print(tarot3)
else:
    print(tarot3)
print('')
print('Sentido de la carta: ',rev3)
print('')
definicion(tarot3,rev3)
