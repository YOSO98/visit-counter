# Guide — Pousser le projet sur GitHub

## Étape 1 — Créer un compte GitHub (si pas encore fait)
https://github.com/signup

## Étape 2 — Créer un nouveau repository

1. Va sur https://github.com/new
2. Repository name : `visit-counter`
3. Visibilité : **Public** (important pour l'entretien)
4. Ne coche rien (pas de README, pas de .gitignore)
5. Clique **Create repository**

## Étape 3 — Initialiser Git et pousser depuis PowerShell

```powershell
cd D:\visit-counter

# Initialiser Git
git init
git add .
git commit -m "feat: compteur de visites Flask + Redis + Docker"

# Connecter au repo GitHub (remplace TON_USERNAME)
git remote add origin https://github.com/TON_USERNAME/visit-counter.git
git branch -M main
git push -u origin main
```

## Étape 4 — Vérifier le pipeline

1. Va sur ton repo GitHub
2. Clique sur l'onglet **Actions**
3. Tu verras le workflow "CI — Build & Test" tourner automatiquement
4. Après ~1 minute : badge vert ✅ = succès

## Étape 5 — Tester que le CI se déclenche

Fais une modification, par exemple change le titre dans index.html, puis :

```powershell
git add .
git commit -m "style: mise à jour titre"
git push
```

Retourne sur GitHub Actions → un nouveau workflow se lance automatiquement !

## Ce que tu montres en entretien

- Repo GitHub public avec README soigné
- Onglet Actions avec pipeline vert
- Expliquer chaque étape du ci.yml
- Montrer l'app tourner en local avec docker ps
