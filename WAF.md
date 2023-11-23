#  WAF

Pour utiliser le script Flask WAF (Web Application Firewall) que nous avons créé, suivez ces étapes :

Installation de Flask : Assurez-vous que Flask est installé. Vous pouvez l'installer en utilisant la commande suivante dans votre terminal ou invite de commande :

```
pip install Flask
```

Copiez le Code : Copiez le code du script dans un fichier Python avec une extension .py. Par exemple, vous pouvez créer un fichier nommé app.py et y coller le code.

Exécution du Script : Exécutez le script en utilisant la commande suivante dans votre terminal ou invite de commande :

```
python app.py
```

Cela démarrera le serveur Flask.

Accédez à l'Application : Ouvrez votre navigateur et accédez à l'URL http://127.0.0.1:5000/ (ou à l'URL spécifiée dans la console après avoir démarré le serveur).

**Testez le WAF :**

Vous pouvez tester le WAF en accédant à différentes URLs qui incluent des motifs d'attaque spécifiés dans le script. Par exemple, essayez d'accéder à http://127.0.0.1:5000/?param=<script> pour tester la protection contre les attaques XSS.

**Observez la Réponse du WAF :**

Si une attaque est détectée, le serveur Flask renverra une réponse JSON indiquant que la requête a été bloquée par le WAF, ainsi qu'un code d'erreur HTTP 403.

**Personnalisez le WAF (Facultatif) :**

Si nécessaire, vous pouvez personnaliser la liste attack_patterns dans le script en ajoutant ou supprimant des motifs d'attaque selon vos besoins spécifiques.

N'oubliez pas que ce script est un exemple basique et ne couvre pas tous les aspects de la sécurité d'une application. Dans un environnement de production, vous voudrez peut-être explorer des solutions de sécurité plus robustes et bien établies, en utilisant des outils tels que des pare-feu applicatifs Web (WAF) tiers, des services de sécurité gérés, etc
