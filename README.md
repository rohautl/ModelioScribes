# ModelioScribes
Scripts for modelio

Notre groupe (Anton Possylkine APO, Ludovic Rohaut LRT) a choisis le projet ParaScribe. L'architecture du dépôt est la même que celle du dépôt depuis lequel nous l'avons forké. Le travail effectué se trouve donc dans le dossier plugin/ParaScribe

# ParaScribe
Traduction de diagramme de classe en texte clair

Ce projet s'appuie sur :
- https://github.com/megaplanet/Modelio3WorkspaceGenOCL-G99 by https://github.com/megaplanet

Pour traduire un diagramme de classe en texte, il est nécessaire de traduire chaque concept de classe en phrases descriptives.
Une classe est composée d’attributs, de méthodes, d’associations et d’héritage.


| Concept                                          | Syntaxe                                        | Example             |
|--------------------------------------------------|------------------------------------------------|---------------------|
| Attribut                                         | Le {nom attribut} de {nom classe} est un {type attribut}                             | Le name de Residence est un string            |
| Méthode                                          | Pour un(e) {nom classe} donne il est possible de : (-{nom méthode} )*         | Pour un(e) Residence donne il est possible de : -bedrooms -usefulBedrooms -bathrooms  |
| Association                                      | 
Un(e) {nom classe} {nom association} {type association} {nom classe associée}
L’élément {nom rôle associée} de {nom association} est un {nom classe associée}
L’élément {rôle association} de {nom association} est un {nom classe}
                                 |
| Héritage                                         | {nom classe} est aussi un(e): (-un(e) {nomclasse mère})*                             |



