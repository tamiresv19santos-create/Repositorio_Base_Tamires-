import streamlit as st

# python -n strealit rum app.py

#------------------------------------------------------------ sidebar

st.sidebar.image("logo.png")
st.sidebar.title('Vih Playlist')

# Generos Musicais 
generos_musicais  = ["Pagode", "Sertanejo", "Pop", "Reggaeton"]

# cantores por genero
cantor_por_genero = {
    "Pagode": ["Mumuzinho"],
    "Sertanejo": ["Jorge & Mateus"],
    "Pop": ["Bruno Mars"],
    "Reggaeton": ["Maluma","Ozuna"]
}
        
# Selectbox para escolher o gênero                
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos_musicais)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    cantor_selecionado= st.sidebar.selectbox(
        "Selecione o cantor :", 
        cantor_por_genero [genero_selecionado]
    )

# Mostrar apenas o genero selecionado
if genero_selecionado and cantor_selecionado:
    st.write(f"** Cantor  selecionado:** {cantor_selecionado}")
    st.write(f"**Gênero musical:** {genero_selecionado}")
    st.image(f"{cantor_selecionado}.png", width=500)

if genero_selecionado == "Pagode" and cantor_selecionado == "Mumuzinho":
 st.markdown('### Mumuzinho(1983-)')    
 st.markdown('Mumuzinho (Márcio da Costa Batista) é cantor e ator brasileiro de pagode e samba, famoso por sucessos como Te Amo e por participar do programa “Esquenta!”.')
 st.video('https://www.youtube.com/watch?v=cs5D2eUSZDY')
 st.link_button(url="https://open.spotify.com/intl-pt/artist/34dfPo3Zi55yM6oV46q4y7", label="Spotify")

elif genero_selecionado == "Sertanejo" and cantor_selecionado == "Jorge & Mateus":
 st.markdown('### jorge(1982-),Mateus(1986)')    
 st.markdown('Jorge & Mateus são uma dupla de sertanejo universitário de Goiás, famosa por hits românticos como Pode Chorar e Sosseguei, ativos desde 2005.')
 st.video('https://www.youtube.com/watch?v=nSSceWPREBA')
 st.link_button(url="https://open.spotify.com/intl-pt/artist/1elUiq4X7pxej6FRlrEzjM",label="Spotify")

elif genero_selecionado == "Pop" and cantor_selecionado == "Bruno Mars":
 st.markdown('### Bruno Mars (1985- ) ')    
 st.markdown('Bruno Mars (Peter Gene Hernandez) é cantor e compositor americano, famoso por hits como Uptown Funk e 24K Magic.')
 st.video('https://www.youtube.com/watch?v=fLexgOxsZu0')
 st.link_button(url="https://open.spotify.com/intl-pt/artist/0du5cEVh5yTK9QJze8zA0C",label="Spotify")

elif  genero_selecionado == "Reggaeton" and cantor_selecionado == "Maluma":
 st.markdown('### Maluma (1994- ) ')    
 st.markdown('Maluma (Juan Luis Londoño) é cantor colombiano de reggaeton e pop latino, famoso por hits como *Felices los 4* e *Hawái*.')
 st.video('https://www.youtube.com/watch?v=t_jHrUE5IOk')
 st.link_button(url="https://open.spotify.com/intl-pt/artist/1r4hJ1h58CWwUQe3MxPuau",label="Spotify")

elif  genero_selecionado == "Reggaeton" and cantor_selecionado == "Ozuna":
 st.markdown('### Ozuna(1992- ) ')    
 st.markdown('**Ozuna** é cantor porto-riquenho de reggaeton e música urbana, famoso por hits desde 2016 e álbuns como *Odisea*.')
 st.video('https://www.youtube.com/watch?v=VqEbCxg2bNI')
 st.link_button(url="https://open.spotify.com/intl-pt/artist/0tcds3GTbuaG8HjTL60Ozt",label="Spotify")