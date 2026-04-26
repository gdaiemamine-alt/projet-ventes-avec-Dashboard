"""
📊 PROJET : Analyse et Visualisation des Ventes

👨‍💻 Auteurs :
- Amine Gdaiem
- Maymoun Aouaya

------------------------------------------------------------

🧾 Description :
Ce script Python permet de simuler, analyser et visualiser
des données de ventes.

Il génère un fichier CSV, effectue des calculs statistiques
et affiche plusieurs graphiques pour faciliter l’analyse.

Une version interactive peut être utilisée avec Streamlit.

------------------------------------------------------------

⚙️ Fonctionnalités :

1. Génération des données
   - Création de "ventes.csv"
   - Données : ID, Prix, Quantité, Remise

2. Lecture des données
   - Chargement du fichier CSV
   - Conversion des types (int, float)

3. Analyse
   - Chiffre d’affaires total (CA)
   - Quantité totale vendue
   - Remise moyenne
   - Produit le plus rentable

4. Export
   - Création de "resultats_final.csv"
   - Ajout : CA Brut et CA Net

5. Visualisation
   - Diagramme en barres
   - Courbe d’évolution
   - Histogramme
   - Scatter plot
   - Camembert (Top 5 produits)

------------------------------------------------------------

🛠️ Technologies utilisées :
- Python 3
- csv
- random
- matplotlib
- streamlit (optionnel)

------------------------------------------------------------

▶️ Exécution :

Mode console :
    python vent.py

Mode Streamlit :
    streamlit run vent1.py

------------------------------------------------------------

📁 Fichiers générés :
- ventes.csv
- resultats_final.csv

------------------------------------------------------------

⚠️ Remarques :
- matplotlib est utilisé pour les graphiques
- Streamlit nécessite la commande :
      streamlit run vent1.py

------------------------------------------------------------

🎯 Objectif :
Apprendre à manipuler des données, faire des analyses
et créer des visualisations avec Python.

------------------------------------------------------------
"""