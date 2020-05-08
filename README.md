# Se_aprofundando_em_Python
 material de aprendizagem 

Aula 7

Operadores Aritméticos

   5 + 2 == 7 <-- adição              5 ** 2 == 25 <-- potencialização
   5 - 2 == 3 <-- subtração             5 // 2 == 4 <-- divisão inteira
   5 * 2 == 10 <-- multiplicação            5 % 2 == 1 <-- resto
   5 / 2 == 2,5 <-- divisão

Ordem de precêdencia 

      1º ()
      2° **
      3º *, /, //, %
      4º +, -

Exemplos

    5 + 3 * 2 == 11
    3 * 5 + 4 ** 2 == 31
    3 * (5 + 4) ** 2 == 243

   o comando "n\" quebra a linha, enquanto o "end=''" continua na mesma linha

Aula 8

Utilizando Módulos

para importar algo para o seu programa é necessario utilizar o comando:

IMPORT "NOMEDAIMPORTAÇÃO" => TODOSOSRESULTADO

esse comando é utilizado para tudo o que tem na importação "NOMEDAIMPORTAÇÃO", para selecionar apenas um campo da importação, utilize:

FROM "NOMEDAIMPORTAÇÃO" IMPORT => RESULTADOESPECIFICO

Aula 9

Manipulando texto

   Uma das maneiras de manipulação de textos é utilizando o nome da variável criada, é coloca "[]" o numero da letra, ou frase que você precisa.

      Fatiamento

   Exemplo

frase = ('Curso em Vídeo Python)
               
`print (frase[3])`

   O resultado seria a letra 3, que seria o `"s"`, lembrando que sempre a começa com 0.

   Com isso em mente, existem outras funcionalidades para ter o resultado mais preciso.

frase = ('Curso em Vídeo Python')

`frase[9:13]`

   Já essa maneira, ele vai pegar da palavra 9 e vai até a 12, ele exclui o 13, ou seja, se fosse realizado o comando, o resultado seria "Víde".

`frase[9:13:2]`

   O último número (":2") é usado para pular casas, o resultado seria "Vd"

`frase[:14]`


   Já esse comando, por não ter o primeiro número antes do ":", ele vai buscar do primeiro caractere, até o 13, já que o 14 ele exclui, o resultado seria "Curso em Vídeo"

`frase[15:]`

   Da mesma forma que o anterior, só que esse vai começar do caractere 14, e vai até o último caractere, o resultado seria "Python"

`frase[7::4]`

   Seguindo a mesma linha de raciocíonio, a string começaria do 7, e vai até o final, já que não houve específicação depois do "7:", e por último, pularia de 4 em 4 casas, o resultado seria "mdPo"

      Análise

`len(frase)`

   O comando `"len"` é utilizado para saber a quantidade caracteres dentro de uma string.

`count.frase('o')`

   O comando `"count"` descobre a quantidade específica de um caractere, por exemplo a letra `"o"`, ele vai procurar quantos "o" tem detro da string, sendo o resultado de 3.
      Pode ser utilizado o comando `"count"`, junto com o fatiamento.

`count.frase('0',0,13)`

   O sistema vai encontrar a letra `"o"`, do caractere 0, até o caractere 12, o resultado será apenas 1 `"o"`, lembrando que o caractere 13 é exluído. 

`frase.find('íde')`

   Já o comando `"find"`, ele procura as letras selecionadas no comando, e irá infomar, em qual caractere ela começa da string, sendo o resultado acima, de 10.
      Caso procure uma frase, ou letra que não esteja na string, o sistema irá retornar `"-1"`, informando que não existe.

`('Curso') in frase`

   Já o comando `"in"` é usado para perguntar ao sistema se existe a frase ou não em uma string, vendo o exemplo, o resultado seria `"True"`.

      Transformação

`frase.replace('Python','Android')`

   O comando "replace" substitui, no exemplo, ele não vai salvar a alteração, ele somente irá mostra a substituição, mas não será salvo, no resultado, apareceria "Curso em Vídeo Android".

`frase.upper()`

   O comando `"upper()"` deixa todos os caracteres em maiúsculos, o resultado seria "CURSO EM VÍDEO PYTHON".

`frase.lower()`

   O comando `"lower()"` tem a mesma função que o "upper", só que ele deixa todos os caracteres em minúsculo, o resultado seria "curso em vídeo python".

`frase.capitalize()`
   O comando `"capitalize()"` irá deixa todas os caracteres em minúsculo, somente o primeiro caractere ficará maiúsculo, o resulto será "Curso em vídeo python".

`frase.title()`

   O comando `"title()"` irá deixar todos os caracteres depois do espaço, eles faz uma quebra, e a primeira palavra, depois do espaço, será maiúscula, as demais ficarão minúscula, o resultado será "Curso Em Vídeo Python".

`frase1 = ('   Aprenda Python   ')`

`frase1.strip()`

   O comando `"strip()"` apaga os espaços vazios antes de iniciar os caracteres, e os últimos caracteres depois de terminar a frase, muito comum na área de tecnologia, o resultado será `"Aprenda Pyhton"`, e não "   Aprenda Pyhton   ".

`frase1.rstrip()`

   "rstrip()" tem a mesma funcionalidade que o `"strip()"`, o que muda é que ele apagará somente o espaços vazios do final, o resultado será "   Aprenda Python".

`frase1.lstrip()`

   Assim como os anteriores, o comando `"lstrip"` irá exluir somente os primeiros espaços vazios da string, o resultado será "Aprenda Python   "


      Disisão

`frase.split()`

O comando `"split()"` faz uma divisão em toda sua string depois do espaço, considerando a string "Curso em Vídeo Pyhton" o `"split()"` irá dividir a string em 4 listas, o resultado seria "Curso" como 1 lista, "em" como 2 lista, "Vídeo" como 3 lista, e "Python" como 4 lista.

      Junção

`'-'.join(frase)`
 
   O Comando `"join"` faz a junção da string, com algo, como espaço, traços, etc, o resultado seria "C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n".