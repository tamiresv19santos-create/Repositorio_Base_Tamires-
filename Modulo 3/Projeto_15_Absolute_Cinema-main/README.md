# 🎬 PROJETO: ABSOLUTE CINEMA
![Cinema](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGJuOTBlcnFmdXFtbzF4dWQ1ZmJwZHMxaHdxdDBreXV3OWh2M291byZlcD12MV9naWZzX3NlYXJjaCZjdD1n/JUXGVpncYAU8NJ6BWz/giphy.gif)

## 📋 ENUNCIADO DO PROJETO

### 🏢 CONTEXTO

**Você foi contratado pela MFLIX**, uma startup inovadora no segmento de streaming que está revolucionando a forma como os jovens consomem conteúdo cinematográfico. A empresa identificou que o público adolescente (15-17 anos) busca uma experiência mais interativa, visual e personalizada para descobrir novos filmes.

### 🎯 DESAFIO

Desenvolver uma **plataforma web moderna e atraente** que apresente os 250 melhores filmes de todos os tempos segundo o IMDb, com funcionalidades de filtragem inteligente e sistema de recomendações personalizadas.

---

## 📊 REQUISITOS DO PROJETO

### 🎨 INTERFACE (Front-end)
- [ ] **Design moderno e responsivo** que funcione em desktop e mobile
- [ ] **Layout em grid** com cards para cada filme
- [ ] **Sistema de navegação** entre páginas
- [ ] **Filtro por gênero** na sidebar
- [ ] **Botões interativos** para acessar informações do IMDb

### 🎬 CONTEÚDO DOS CARDS
Cada filme deve exibir:
- [ ] **Poster** do filme (imagem)
- [ ] **Posição no ranking** IMDb
- [ ] **Título** e **ano** de lançamento
- [ ] **Nota** (rating) do IMDb
- [ ] **Duração** do filme
- [ ] **Gênero** principal
- [ ] **Botão/link** para página oficial no IMDb

### 🔧 FUNCIONALIDADES
- [ ] **Página principal** com catálogo completo
- [ ] **Sistema de filtros** por gênero
- [ ] **Página de sugestões** com filme aleatório
- [ ] **Layout responsivo** (3 colunas em desktop)
- [ ] **Navegação fluida** entre seções

### 📁 ESTRUTURA TÉCNICA
- [ ] **Arquivo principal**: `app.py`
- [ ] **Página separada**: `pages/2_🎲_Sugerir_Filme.py`
- [ ] **Base de dados**: `filmes.csv`
- [ ] **Framework**: Streamlit
- [ ] **Processamento de dados**: Pandas

---

## 🛠️ TECNOLOGIAS PERMITIDAS

| Tecnologia | Versão | Finalidade |
|------------|---------|------------|
| **Python** | 3.8+ | Linguagem principal |
| **Streamlit** | 1.28+ | Framework web |
| **Pandas** | 2.0+ | Manipulação de dados |
| **CSV** | - | Armazenamento de dados |

---

## 📚 RECURSOS FORNECIDOS

### 🎬 BASE DE DADOS
A MFLIX fornece o arquivo `filmes.csv` contendo:
- **250 filmes** do ranking IMDb
- **8 colunas** de informações por filme
- **Dados completos**: título, ano, nota, duração, gênero, links

### 🎨 DESIGN SYSTEM
**Cores da marca MFLIX:**
- 🔴 Vermelho: `#FF4B4B`
- ⚫ Preto: `#0E1117` 
- ⚪ Branco: `#FFFFFF`

**Tipografia:**
- Títulos: Font bold
- Texto: Font regular
- Botões: Rounded corners

---

## 🐛 DESAFIOS TÉCNICOS ESPERADOS

### 🔍 PROBLEMA: Títulos com vírgulas no CSV
**Solução:** Usar aspas nos títulos problemáticos no arquivo CSV

### 🖼️ PROBLEMA: Imagens com tamanhos diferentes
**Solução:** Definir largura fixa para padronização visual

### 📱 PROBLEMA: Layout responsivo
**Solução:** Usar sistema de colunas do Streamlit com containers

### 🔄 PROBLEMA: Navegação entre páginas
**Solução:** Utilizar a funcionalidade nativa de pages do Streamlit

---

## 💡 DICAS DE DESENVOLVIMENTO

### 🎨 PARA O DESIGN
```python
# Use containers para organizar o layout
with st.container():
    st.image(...)
    st.subheader(...)
```

### 📊 PARA OS DADOS
```python
# Carregue o CSV uma vez só
filmes = pd.read_csv('filmes.csv')
```

### 🔧 PARA OS FILTROS
```python
# Filtro simples por gênero
filmes_filtrados = filmes[filmes['Genre'] == genero_escolhido]
```

### 🎯 PARA A SUGESTÃO ALEATÓRIA
```python
# Escolha aleatória com filtros
filme_sugerido = filmes_filtrados.sample(1).iloc[0]
```

---

## 🚀 COMEÇANDO O PROJETO

### 📥 INSTALAÇÃO
```bash
# 1. Instale as dependências
pip install streamlit pandas

# 2. Execute o projeto
streamlit run app.py
```

### 🏗️ ESTRUTURA INICIAL
```python
# app.py - Esqueleto básico
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Absolute Cinema", page_icon="🎬")
filmes = pd.read_csv('filmes.csv')

st.title("🎬 Absolute Cinema")
st.write("Bem-vindo à sua plataforma de filmes!")
```

---

## 🌟 IDEIAS PARA PERSONALIZAÇÃO

### 🎨 MELHORIAS VISUAIS
- Adicione suas cores favoritas
- Crie um tema escuro/claro
- Adicione animações CSS
- Personalize os ícones e emojis

### 🔧 FUNCIONALIDADES EXTRAS
- Sistema de favoritos
- Busca por título
- Filtro por década
- Compartilhamento nas redes sociais
- Reviews e comentários

### 📱 FEATURES AVANÇADAS
- Integração com API do YouTube para trailers
- Sistema de playlists personalizadas
- Recomendações baseadas em machine learning
- Versão mobile app

---

## 📞 SUPORTE TÉCNICO MFLIX

**Equipe de Desenvolvimento:**
- 📧 Email: dev.support@mflix.com
- 💬 Discord: MFLIX Dev Community
- 📚 Documentação: docs.mflix.com

**Horário de Suporte:**
- Segunda a Sexta: 9h-18h
- Plantão de Dúvidas: Quartas 14h-16h

---

## 🎬 PALAVRAS FINAIS DA MFLIX

> "Estamos muito animados para ver como vocês, jovens desenvolvedores, vão transformar a experiência cinematográfica para a nova geração. Este não é apenas um projeto técnico - é uma oportunidade de impactar como milhões de pessoas descobrem e se conectam com grandes histórias."

**Equipe de Inovação MFLIX**  
*Transformando o futuro do entretenimento*

---

<div align="center">

## 🚀 MÃO NA MASSA!

**Hora de codar! Lembre-se: cada grande filme começa com uma única cena, e cada grande projeto começa com uma única linha de código.**

```python
# Sua jornada começa aqui...
import streamlit as st

st.title("🎬 Bem-vindo ao Absolute Cinema!")
st.write("Vamos criar algo incrível juntos!")
```

**Bom projeto!** 🎉🎬

</div>
