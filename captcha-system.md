Aujourd'hui je vous propose un système de captcha pour votre serveur en version bouton.
VARIABLE OBLIGATOIRE : nom : captcha / Value=
UNIQUEMENT EN BDScript 2 / BDFD

COMMANDE UNIQUEMENT EN SLASH COMMANDE
MERCI DE FAIRE CECI :
CHOIX PREDEFINIS :
Nom : role-id
Description : Insérer l'ID du rôle au captcha.



Trigger : </set-captcha:1>

$setUserVar[captcha;$message[role-id]]
$nomention
$title[Captcha]
$color[ff0000]
$description[
__**Merci d'accepter ce captcha afin de pouvoir accéder à la discussion.**__]
$addButton[no;captcha;✅️;success;no]



Trigger : $onInteraction[captcha]

$nomention
$var[role-id;$getUserVar[captcha]]
$ephemeral
$removeButtons
Rôle ajouté avec succès !
$if[$hasRole[$authorID;$var[role-id]]==false]
Tu as eu accès au rôle et à la discussion !
$roleGrant[$authorID;+$var[role-id]]
$else
$endif
