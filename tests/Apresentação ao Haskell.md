# Apresentação ao Haskell

### Geral
- **GHC**
	- É o compilador, ele gera código executável
	- Tem o ambiente interativo GHCi, que permite a avaliação de expressões de forma interativa
- **Módulos**
	- Os programas em Haskell são organizados em módulo
	- Um módulo é formado por um conjunto de definições (tipos, funções, ...)
- **Comentários:** uma linha -- e múltiplas linhas {- ... -}
- **Biblioteca padrão**
	- Formada por um conjunto de módulos disponíveis automaticamente para todos os programas em .hs
		- É o módulo Prelude, importado automaticamente em todos os módulos de uma apliação .hs
	- Oferece funções aritméticas, manipulações de listas...
### Funções
- No lugar de parênteses usamos o espaço
	- $f(a,b) + c\times d$ vira `f a b + c * d`
	- $f(x)f(y)$ fira `f x * f y` ou `(f x) * (f y)`
- **Definição de funções**
	- Formato: `<nome><lista de parâmetros> = <expressão>`
	- Exemplo: `multiplica x y = x * y`
- Podemos salvar funções em scripts (.hs)
	- Exemplo: `module Operacoes where` daí declara funções
	- Assim, no GHCi podemos carregar o módulo com `:l Operacoes` e usar as funções
	- Recomenda-se que o módulo tenha o mesmo nome do script
- Um módulo pode importar funções de outros módulos
	- Exemplo: 
		```
	  module Calculadora
	  where import Operacoes...
		```
- Convenção de nomes
	- Funções: minúsculo, pode conter letras, dígitos, sublinhado e '
	- Parâmetros de função: tudo em minúsculo
### Tipos
- Coleção de valores relacionados
- Devem ter nome começando com letra maiúscula
- Tipos numéricos
	- Int (precisão fixa, limitado), Integer (precisão arbitrária, ilimitado), Float, Double
- Tipos de caractere e lógico
	- Bool (`True, False`)
	- Char ('a', 'b'), String ("ABC", que é \['A', 'B', 'C'])
	- \[t\] (sequência de valores do mesmo tipo, lista, \[1, 2, 3])
	- ($t_1$...$t_2$) (sequência de valores possivelmente de tipos diferentes, tupla, não pode ter só 1 componente)
- Assinaturas de tipo
	- Qualquer expressão pode ter seu tipo anotado
	- Formato: `abc :: String`
	- :: tem precedência menor que os demais operadores
	- No GHCi o comando `:type` ou `:t`exibe o tipo de uma expressão
- Variáveis de tipo
	- Quando um tipo pode ser de qualquer tipo da linguagem, é representado por uma variável de tipo
	- Exemplo: `head :: [a] -> a`, recebe uma lista de elementos de um certo tipo e seu retorno tem esse mesmo tipo
	- Devem começar com letra minúscula, geralmente denominadas `a, b, c...`
- Erros de tipo
	- Toda expressão tem seu tipo calculado em tempo de compilação, se não for possível, ocorre um *erro de tipo*
	- A aplicação de uma função a um argumento de tipo errado é um *erro de tipo*
- Checagem de tipos
	- É *fortemente tipada*, sistema de tipos avançado
	- Todos os possíveis erros de tipo são em tempo de compilação
		- Tipagem estática
	- Dá segurança e velocidade ao programa

### Tipos e funções
- É possível anotar o tipo de uma função
	- Exemplo: `x :: Int -> Float -> Bool -> Float`
		- A função de nome $x$ recebe 3 argumentos (Int, Float, Bool) e retorna Float
	- O retorno é o último tipo, os demais são argumentos
- O sinal de *igual* não representa atribuição, mas definição
	- `x=3`: "x é uma função que não recebe parâmetros e retorna um inteiro constante"
- Função polimórfica
	- O seu tipo contém uma ou mais *variáveis de tipo*
	  
