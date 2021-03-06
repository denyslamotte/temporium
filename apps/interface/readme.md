interface
=====

### installation
_depuis le terminal_
- aller dans le dossier `cd ~/temporim/apps/interface/`
- installer les modules nodejs `npm install`
- création les dossiers pour les médias dans le dossier `interface/public/` 
	- `exposure`, l’emplacement des images capturées par l’appareil
	- `images`, l’emplacement pour l’image à exposer `nega.png` et du flash gris `flash.png`

- ajouter le film dans `/video/immersion.mov`

### configuration du montage dynamique

- le fichier `score.csv` ([/public/score.csv](https://github.com/dcfvg/temporium/blob/panorama/apps/interface/public/score.csv)) permet de modifier les paramètres du montage dynamique.

| champ  | description |
| ------ | ----------- |
| id     | numéro d'évenement unique                    |
| title  | étiquette pour repérer les plans                      |
| mode   | in (avant contamination) / out (après contamination)
| at_min:at_sec | mode in : moment ou une interruption du plan est possible|
|        | mode out : moment avant lequel la lecture doit avoir reprise (mode out )|
| jump   | saut max en avant ou en arriere suivant le mode |
| life_speed | vitesse de défilement du timelapse — 1=vitesse normale / 8=ralenti 8 fois | 
| life_zoom  | grossisement de l'image 1-5 | 

> Le temps du vivant est figuré dans le film par un cache vert de 4 secondes.

### préparation des media

**film**
- exporte en H264 avec un débit entre 8-10 Mb/s
- format 1.35 ( 1920 × 1036 px ), pas de bandes noires

**image à exposer**
- `public/images/nega.png`
- photogramme en png
- format fullHD ( 1920 x 1080 px)
- négatif, miroir, contraste/niveaux adaptés

**flash**
- `public/images/flash.png`
- format fullHD ( 1920 x 1080 px)

## démarrage 

_depuis le terminal_
- aller dans le dossier `cd ~/temporim/apps/interface/`
- démarrer le serveur node `node server.js`

_depuis le navigateur_
- ouvrir `localhost:8080/player` pour afficher le film
- ouvrir `localhost:8080/exposure` pour afficher l’image à exposer
- **attendre** (plusieurs minutes) la disparition du message de pré-préchargement du film `loading …`.

_depuis le vivant_
- envoyer le message `seance_start`
- envoyer le taux de formation en réponse à `/image_capture/public/000XX.jpg`

## démarrage exposer-flasher uniquement

_depuis le terminal_
- aller dans le dossier `cd ~/temporim/apps/interface/`
- démarrer le script `bash bin/capture.sh`
- quitter le script `ctrl` + `c`

## utilisation

### player
La console du navigateur permet de suivre l’état du player.

_raccourcits clavier_

- `m` montrer le film
- `l` montrer l’image live 
- `k` afficher le timecode courant dans la console
- `j` avancer le film de 10 s
- `h` avancer le film de 30 s

### exposure

La page `/exposure` peut être déporté sur un autre poste en consultant `xxx.xxx.xxx.xxx:8080/exposure/` avec `xxx.xxx.xxx.xxx` l'ip du serveur sur le réseau local. .

