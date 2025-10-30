# 🤖 Reconnaissance de la Langue des Signes avec TinyML

## 🧩 Description
Ce projet a pour objectif de **reconnaître la langue des signes américaine (ASL)** en temps réel à l’aide de **modèles légers** basés sur **FastKAN** et **TinyML**.  
Le modèle est optimisé pour être déployé sur **microcontrôleurs** grâce à des techniques de **pruning** et **quantization**.

---

## ⚙️ Technologies utilisées
- 🐍 Python  
- 🤖 TensorFlow / Keras  
- 🔥 PyTorch  
- ⚡ FastKAN  
- 🧠 TinyML  
- 👁️ OpenCV  
- 🧮 NumPy, Pandas, Matplotlib  

---

## 📂 Jeu de données
J’ai fusionné plusieurs datasets publics (principalement Kaggle) contenant des images de signes ASL.  
Chaque image a été renommée et nettoyée via un script Python (`rename_dataset.py`).  
⚠️ *Le dataset complet (≈9 Go) n’est pas inclus dans ce repo pour des raisons de taille.*

---

## 🚀 Étapes du projet
1. **Collecte et préparation des données**
   - Fusion de plusieurs jeux de données ASL.
   - Nettoyage et renommage automatique des fichiers.
2. **Prétraitement**
   - Redimensionnement des images.
   - Normalisation et augmentation des données.
3. **Entraînement du modèle**
   - Modèle **FastKAN** pour TinyML.
   - Comparaison avec CNN et MLP classiques.
4. **Optimisation**
   - Pruning et quantization pour réduire la taille du modèle.
5. **Évaluation**
   - Accuracy, Loss, Confusion Matrix.
6. **Déploiement (TinyML)**
   - Conversion du modèle en format compatible microcontrôleur.

---

## 📊 Résultats
- Accuracy du modèle : **94.3%**
- Taille après compression : **< 1 Mo**
- Temps d’inférence : **≈20 ms**

---

## 🧠 Exemple visuel
![Training Accuracy](images/training_accuracy.png)

---

## 🔗 Auteurs
👩‍💻 **Sara Souhail**  
Étudiante en Master Intelligence Artificielle et Technologies Émergentes  
📧 [souhailsara31@gmail.com](mailto:souhailsara31@gmail.com)

---

## 🧰 Installation
```bash
git clone https://github.com/sarasouhail/ASL-TinyML-FastKAN.git
cd ASL-TinyML-FastKAN
pip install -r requirements.txt
