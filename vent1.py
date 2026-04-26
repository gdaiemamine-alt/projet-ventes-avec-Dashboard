import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

# ---------------------------
# CONFIG
# ---------------------------
st.set_page_config(page_title="Dashboard Ventes", layout="wide")

st.title("📊 Dashboard des ventes")

# ---------------------------
# INPUT UTILISATEUR
# ---------------------------
nb_lignes = st.slider("Nombre de lignes", 10, 5000, 100)

# ---------------------------
# GÉNÉRATION DATA
# ---------------------------
random.seed(42)

data = []
for i in range(nb_lignes):
    prix = round(random.uniform(5, 100), 2)
    quantite = random.randint(1, 50)
    remise = random.randint(0, 100)

    ca_brut = prix * quantite
    ca_net = ca_brut * (1 - remise / 100)

    data.append({
        "ID": 100 + i,
        "Prix": prix,
        "Quantite": quantite,
        "Remise": remise,
        "CA_Brut": round(ca_brut, 2),
        "CA_Net": round(ca_net, 2)
    })

df = pd.DataFrame(data)

# ---------------------------
# KPI
# ---------------------------
st.subheader("📈 Indicateurs clés")

col1, col2, col3 = st.columns(3)

col1.metric("💰 CA Total", round(df["CA_Net"].sum(), 2))
col2.metric("📦 Quantité totale", int(df["Quantite"].sum()))
col3.metric("🏷️ Remise moyenne", round(df["Remise"].mean(), 2))

# ---------------------------
# TABLE
# ---------------------------
st.subheader("📋 Données")
st.dataframe(df)

# ---------------------------
# GRAPHIQUES
# ---------------------------
st.subheader("📊 Visualisations")

# Limite affichage
df_plot = df.head(100)

# Bar chart
fig1, ax1 = plt.subplots()
ax1.bar(df_plot["ID"], df_plot["CA_Net"])
ax1.set_title("CA Net par produit")
st.pyplot(fig1)

# Courbe
fig2, ax2 = plt.subplots()
ax2.plot(df_plot["ID"], df_plot["CA_Net"], marker='o')
ax2.set_title("Evolution du CA")
st.pyplot(fig2)

# Histogramme
fig3, ax3 = plt.subplots()
ax3.hist(df["Quantite"], bins=20)
ax3.set_title("Distribution des quantités")
st.pyplot(fig3)

# Scatter
fig4, ax4 = plt.subplots()
ax4.scatter(df["Prix"], df["CA_Net"])
ax4.set_title("Prix vs CA Net")
st.pyplot(fig4)

# Top 5
st.subheader("🏆 Top 5 produits")
top5 = df.sort_values(by="CA_Net", ascending=False).head(5)
st.table(top5)