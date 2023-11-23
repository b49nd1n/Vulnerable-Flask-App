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

## Exemples d'URLs pour Tester le WAF

| URL d'Exemple                                  | Attaque Détectée        | Réponse Attendue                                      | Explications et Commentaires                                     |
|-----------------------------------------------|------------------------|-------------------------------------------------------|-----------------------------------------------------------------|
| `http://127.0.0.1:5000/?param=select`         | SQL Injection          | `{"error": "Blocked by WAF: SQLInjection"}`           | Tentative d'injection SQL avec le mot-clé `select` dans l'URL   |
| `http://127.0.0.1:5000/?param=<script>`       | XSS                    | `{"error": "Blocked by WAF: XSS"}`                   | Tentative d'injection de script XSS dans l'URL                |
| `http://127.0.0.1:5000/?param=;ls`            | Command Injection      | `{"error": "Blocked by WAF: CommandInjection"}`      | Tentative d'injection de commande avec le point-virgule       |
| `http://127.0.0.1:5000/?param=../../etc/passwd`| Path Traversal         | `{"error": "Blocked by WAF: PathTraversal"}`         | Tentative de traversée de chemin vers /etc/passwd             |
| `http://127.0.0.1:5000/?param=file:///etc/passwd`| Remote Code Execution | `{"error": "Blocked by WAF: RemoteCodeExecution"}` | Tentative d'exécution de code à distance avec `file://`       |
| `http://127.0.0.1:5000/?param=%0D%0ASet-Cookie`| HTTP Response Splitting| `{"error": "Blocked by WAF: HTTPResponseSplitting"}`| Tentative de division de la réponse HTTP avec des caractères spéciaux |
| `http://127.0.0.1:5000/?param=<!ENTITY`        | XML External Entity    | `{"error": "Blocked by WAF: XMLExternalEntity"}`    | Tentative d'injection d'entité XML externe                    |
| `http://127.0.0.1:5000/?param=http://localhost`| Server Side Request Forgery | `{"error": "Blocked by WAF: ServerSideRequestForgery"}` | Tentative de requête côté serveur avec une URL locale         |
| `http://127.0.0.1:5000/?param=_csrf_token`     | Cross-Site Request Forgery | `{"error": "Blocked by WAF: CrossSiteRequestForgery"}` | Tentative de CSRF avec un paramètre `_csrf_token`             |
| `http://127.0.0.1:5000/?param=%0D%0A`          | HTTP Response Splitting | `{"error": "Blocked by WAF: HTTPResponseSplitting"}`| Tentative de division de la réponse HTTP avec des caractères spéciaux |
| `http://127.0.0.1:5000/?param=<?php echo "Hello"; ?>` | Server Side Scripting | `{"error": "Blocked by WAF: ServerSideScripting"}`  | Tentative d'injection de script côté serveur avec PHP         |
| `http://127.0.0.1:5000/?param={{2+2}}`         | Server Side Template Injection | `{"error": "Blocked by WAF: ServerSideTemplateInjection"}` | Tentative d'injection de template côté serveur avec Jinja2 |
| `http://127.0.0.1:5000/?param=pickle.loads`    | Insecure Deserialization | `{"error": "Blocked by WAF: InsecureDeserialization"}` | Tentative d'injection de désérialisation non sécurisée avec Pickle |
| `http://127.0.0.1:5000/?param=/etc/passwd`     | Insecure Direct Object Reference | `{"error": "Blocked by WAF: InsecureDirectObjectReference"}` | Tentative d'accéder à un objet direct sans validation |
| `http://127.0.0.1:5000/?param=redirect:`      | Unvalidated Redirects and Forwards | `{"error": "Blocked by WAF: UnvalidatedRedirectsAndForwards"}` | Tentative de redirection non validée avec le préfixe `redirect:` |
| `http://127.0.0.1:5000/?param=ng-bind-html`   | Cross-Site Scripting AngularJS | `{"error": "Blocked by WAF: CrossSiteScriptingAngularJS"}` | Tentative d'injection XSS avec ng-bind-html dans AngularJS     |
| `http://127.0.0.1:5000/?param=dangerouslySetInnerHTML` | Cross-Site Scripting React | `{"error": "Blocked by WAF: CrossSiteScriptingReact"}` | Tentative d'injection XSS avec dangerouslySetInnerHTML dans React |
| `http://127.0.0.1:5000/?param=%7B%7B2%2B2%7D%7D` | Server Side Template Injection (Encoded) | `{"error": "Blocked by WAF: ServerSideTemplateInjection"}` | Tentative d'injection de template côté serveur encodée avec URL |
| `http://127.0.0.1:5000/?param=pickle.dumps`   | Autres Méthodes Pickle  | `{"error": "Blocked by WAF: InsecureDeserialization"}` | Tentative d'utilisation d'autres méthodes de Pickle pour contourner la désérialisation sécurisée |

