 
import streamlit as st

### python -m streamlit run app.py

#------------------------------------------------------ Sidebar

st.sidebar.image("logo.png")
st.sidebar.title('petvolgue')


#-----------------------------------------------------------------Principal 
st.title('petvolgue')

st.markdown('🐾 PetVolgue – Moda e Estilo para o seu Pet!')

st.markdown('A PetVolgue é um site especializado na venda de roupas e acessórios exclusivos para pets, unindo conforto, qualidade e estilo. Nossa missão é trazer o melhor da moda pet para deixar cães e gatos ainda mais charmosos e protegidos em todas as ocasiões.')

st.markdown('👗 Roupas para Pets: Peças modernas, divertidas e funcionais, que vão desde camisetas casuais até roupinhas elegantes para eventos especiais.')

st.markdown('🎀 Acessório: Coleiras, laços, bandanas, camas e muito mais, tudo pensado para combinar estilo com praticidade no dia a dia.')


st.title('🐾 Por que escolher a PetVolgue?')

left, middle, right = st.columns(3, border=True)

left.markdown("✨ Qualidade & Conforto: Trabalhamos apenas com materiais premium, que garantem durabilidade e conforto ao seu pet. Nossas roupas são desenvolvidas com modelagens especiais, respeitando os movimentos naturais de cães e gatos. Cada peça é pensada para oferecer praticidade no dia a dia, unindo estilo e bem-estar.")
middle.markdown("🎀 Estilo Exclusivo: A PetVolgue acompanha as tendências da moda, trazendo coleções exclusivas para todas as estações. Roupas e acessórios que vão do casual divertido ao elegante sofisticado, perfeitos para qualquer ocasião. Peças únicas que transformam o visual do seu pet e destacam a sua personalidade.")
right.markdown("💖 Confiança & Praticidade: Plataforma online simples, rápida e segura para suas compras. Oferecemos atendimento personalizado, com dicas para ajudar a escolher o produto ideal. Garantimos entrega ágil e uma experiência de compra sem complicações.")

st.image('cachorros.png')

st.image('filhotes_gatos.png')

st.title('🐾 Junte-se à Família PetVolgue!')

st.markdown('Na PetVolgue, acreditamos que cada pet merece estar confortável, protegido e cheio de estilo. Nossas roupas e acessórios foram pensados para trazer qualidade, personalidade e alegria ao dia a dia do seu companheiro.')

st.markdown('✨ Explore nossas coleções, descubra peças exclusivas e transforme o visual do seu pet.')
st.markdown('💖 Porque aqui, cuidar do seu pet é também celebrar seu estilo.')

st.markdown('Siga-nos nas redes sociais e fique por dentro de lançamentos, promoções e dicas para deixar seu pet sempre fashion!')

st.markdown('📧 Assine nossa newsletter e receba novidades diretamente no seu e-mail.')

sentiment_mapping = ["one", "two", "three", "4", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"você {sentiment_mapping[selected]} estrelas.")