📊 Dashboard des Ventes (Streamlit)
🧾 Description

Ce projet est un dashboard interactif de visualisation des ventes développé avec Streamlit.
Il génère des données simulées et permet d’analyser facilement les performances commerciales via des indicateurs clés et des graphiques.

🚀 Fonctionnalités
Génération dynamique de données de ventes
Calcul automatique :
💰 Chiffre d'affaires brut et net
📦 Quantités vendues
🏷️ Remises appliquées
Affichage des KPI principaux
Table interactive des données
Visualisations :
Histogramme des quantités
Évolution du chiffre d'affaires
Corrélation Prix vs CA Net
Bar chart du CA Net
Top 5 des produits les plus performants
🛠️ Technologies utilisées
Python
Streamlit
Pandas
Matplotlib
📦 Installation
Cloner le projet :
git clone https://github.com/ton-repo/dashboard-ventes.git
cd dashboard-ventes
Installer les dépendances :
pip install -r requirements.txt
▶️ Lancer l'application
streamlit run app.py

Puis ouvrir le navigateur à l'adresse indiquée (généralement http://localhost:8501)

⚙️ Utilisation
Ajuster le nombre de lignes via le slider
Explorer les indicateurs clés
Analyser les graphiques
Identifier les meilleurs produits via le Top 5
📊 Structure des données

Chaque ligne contient :

Colonne	Description
ID	Identifiant produit
Prix	Prix unitaire
Quantite	Nombre d’unités vendues
Remise	Remise (%)
CA_Brut	Chiffre d'affaires brut
CA_Net	Chiffre d'affaires après remise
📈 Exemple de KPI
CA Total (somme du CA Net)
Quantité totale vendue
Remise moyenne
🔮 Améliorations possibles
Ajout de filtres (prix, remise, quantités)
Export des données en CSV
Graphiques interactifs avec Plotly
Connexion à une base de données réelle
Ajout de catégories produits
👤 Auteur

Amine Gdaiem / maymoun aouay

📄 Licence

Ce projet est libre d'utilisation à des fins éducatives.
