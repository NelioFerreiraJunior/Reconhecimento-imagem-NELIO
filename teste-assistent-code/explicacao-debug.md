# Explicação dos Erros - debug.py

## Erros Encontrados

### 1. **Linha 5 - String sem aspas**
```python
item1 = float(input(Preço do item 1? ))
```
**Problema**: Falta aspas na string `"Preço do item 1? "`. Python trata `Preço` como uma variável indefinida.
**Solução**: Adicionar aspas: `float(input("Preço do item 1? "))`

---

### 2. **Linha 35 - F-string ausente**
```python
print(" Item 2:        R$ {total_item2:.2f}")
```
**Problema**: A string não possui o prefixo `f`, então `{total_item2:.2f}` não é interpolado e será exibido literalmente.
**Solução**: Adicionar `f` antes da string: `print(f" Item 2:        R$ {total_item2:.2f}")`

---

### 3. **Linha 23 - Tipo de dados incorreto**
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```
**Problema**: `input()` retorna uma string, mas a variável é usada em cálculos matemáticos (linha 24) e comparação (linha 41).
**Solução**: Converter para número: `float(input(...))`

---

### 4. **Linha 41 - Indentação incorreta**
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```
**Problema**: O `print` está sem indentação correta após o `if`. Python espera um bloco indentado.
**Solução**: Indentar corretamente o `print` com 4 espaços.

---

## Resumo
- 1 erro de sintaxe (aspas faltando)
- 1 erro de formatação (f-string faltando)
- 1 erro de tipo de dados (string em vez de float)
- 1 erro de indentação (if statement)
